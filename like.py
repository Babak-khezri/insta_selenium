from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
from time import sleep
from pyautogui import typewrite
driver = webdriver.Chrome()


def Enter_account():
    driver.get('https://www.instagram.com/')
    sleep(4)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys('selenium__py')
    driver.find_element_by_xpath('//input[@name="password"]').send_keys('1379bk@15')
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
    Search_hashtag()


def Search_hashtag():
    sleep(2)
    links = []
    name = 'animals'
    while len(links) == 0:
        driver.get('https://www.instagram.com/explore/tags/{}/'.format(name))
        lst = driver.find_elements_by_tag_name('a')
        for i in lst:
            if 'com/p/' in i.get_attribute('href'):
                links.append(i.get_attribute('href'))
    Like(links)


def Like(links):
    for i in links:
        driver.get(i)
        sleep(1)
        driver.find_element_by_class_name('wpO6b').click()
        Thread(target=comment).start()
        sleep(2.5)
    sleep(10)
    driver.quit()


def comment():
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea').click()
    typewrite("It's beautiful")
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[3]/div/form/button').click()


Enter_account()
