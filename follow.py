from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import sample
from time import sleep
from tkinter import *
win = Tk()
driver = webdriver.Chrome()  # Create the driver
enter_user = None
enter_pass = None
def enter_account():  # Enter to the account
    username = enter_user.get()
    password = enter_pass.get()
    win.destroy()
    driver.get('https://www.instagram.com/')
    sleep(2)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)  # Add username
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)  # Add password
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()  # click on log in
    sleep(3)
    # Go to explorer page to pass the welcome massage
    driver.get('https://www.instagram.com/explore/')
    finder()
def finder():  # Search name to find profiles
    name = list("abcdefghijklmnopqrstuvwxyz")
    search = "".join(sample(name, 4))  # Create the word
    sleep(2)
    # Find the search bar and write the word
    driver.find_element_by_xpath('//input[@placeholder="Search"]').send_keys(search)
    links = []  # Get acoount links
    while len(links) == 0:
        sleep(0.5)
        lst = driver.find_elements_by_tag_name(
            'a')  # Find all elements that have link
        for i in lst:  # Just get the account links
            if search in i.get_attribute('href') and "tags" not in i.get_attribute('href') and "locations" not in i.get_attribute('href'):
                links.append(i.get_attribute('href'))
    follow(links)
def follow(links):  # Go to links and follow
    sleep(1)
    for i in links:
        driver.get(i)
        sleep(0.5)
        f_1 = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
        if len(f_1) == 1:  # Check that account wasnt private
            f_1[0].click()  # Follow
def tkinter(): # make gui to get account
    win.title("Instagram")
    win.geometry("700x600")
    Label(win,text = "<< Instagram BOT >>",fg = "purple",font = ("Aryal",32,'bold')).pack()
    Label(win,text = "Enter the Username : ",font = ("Aryal",32,'bold')).pack()
    global enter_user
    enter_user = Entry(win,font = ("Aryal",32,'bold'),bg = "pink")
    enter_user.pack()
    Label(win,text = "Enter the Password : ",font = ("Aryal",32,'bold')).pack()
    global enter_pass
    enter_pass = Entry(win,font = ("Aryal",32,'bold'),bg = "pink")
    enter_pass.pack()
    Label(win,text = " ",font = ("Aryal",32,'bold')).pack()
    but = Button(win,text = "ENTER",bg = "green",font = ("Aryal" ,25,'bold'))
    but.config(bd = 10 ,padx = 25 ,pady = 15 ,command = enter_account ,activebackground = "red")
    but.pack()
    mainloop()
#Start the program
tkinter()
sleep(10)
driver.quit()  # Close the site