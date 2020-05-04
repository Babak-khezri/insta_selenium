from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import sample , randint
from time import sleep
from tkinter import Tk ,Label ,Entry ,Button, mainloop
win = Tk()
driver = webdriver.Chrome()  # Create the driver
enter_user = None
enter_pass = None


def enter_account():  # Enter to the account
    username = enter_user.get()
    password = enter_pass.get()
    if username  == "" or password == "": # Make sure that user and pass are not empty
        enter_account()
    win.destroy() # Close the gui
    driver.get('https://www.instagram.com/')
    sleep(2)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)  # Add username
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)  # Add password
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()  # click on log in
    sleep(3)
    # Go to explorer page to pass the welcome massage
    while True:
        driver.get('https://www.instagram.com/{}/'.format(username))
        finder()


def finder():  # Search name to find profiles
    name = list("abcdefghijklmnopqrstuvwxyz")
    search = "".join(sample(name, randint(3,4)))  # Create the word
    sleep(2)
    # Find the search bar and write the word
    driver.find_element_by_xpath('//input[@placeholder="Search"]').send_keys(search)
    links = []  # Get acoount links
    while len(links) == 0: # Make sure find accounts
        sleep(0.5)
        lst = driver.find_elements_by_tag_name('a')  # Find all elements that have link
        for i in lst:  # Just get the account links
            if search in i.get_attribute('href') and "tags" not in i.get_attribute('href') and "locations" not in i.get_attribute('href'):
                links.append(i.get_attribute('href')) # 'href' is the link of element
    follow(links)


def follow(links):  # Go to links and follow
    sleep(1)
    for i in links:
        driver.get(i) # Go to the account
        sleep(0.5)
        follow_but = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
        if len(follow_but) == 1:  # Check that account wasnt private
            follow_but[0].click()  # Follow


def tkinter():  # make gui to get account
    win.title("Instagram") # Title
    win.geometry("700x550") # Size of window
    Label(win, text="<< Instagram BOT >>", fg="#cc0099",font=("Aryal", 32, 'bold')).pack() # First comment
    Label(win, text="Enter the Username : ",fg = '#003300', font=("Aryal", 32, 'bold')).pack() # comment
    global enter_user
    enter_user = Entry(win, font=("Aryal", 32, 'bold'), bg="pink") # space for enter the username
    enter_user.pack()
    Label(win, text="Enter the Password : ",fg = '#003300' ,font=("Aryal", 32, 'bold')).pack() # comment
    global enter_pass
    enter_pass = Entry(win, font=("Aryal", 32, 'bold'), bg="pink") # space for enter the password
    enter_pass.pack()
    Label(win, text="", font=(32)).pack() # Free space
    but = Button(win, text="LOG IN", bg="#800080", font=("Aryal", 25, 'bold')) # button to start program and end GUI
    but.config(bd=20, padx=25, pady=15,command=enter_account, activebackground="red")
    but.pack()
    mainloop()


# Start the program
tkinter()
driver.quit()  # Close the site
