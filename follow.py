from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import sample
from time import *
driver = webdriver.Chrome() # create the driver
def open_ins():
    driver.get('https://www.instagram.com/')
    enter_acc()
def enter_acc():
    sleep(2)
    driver.find_element_by_xpath('//input[@name="username"]').send_keys('selenium__py')
    driver.find_element_by_xpath('//input[@name="password"]').send_keys('1379bk@15')
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
    sleep(3)
    driver.get('https://www.instagram.com/explore/')
    finder()
def finder():
    name = list("abcdefghijklmnopqrstuvwxyz")
    search = "".join(sample(name,4))
    sleep(2)
    driver.find_element_by_xpath('//input[@placeholder="Search"]').send_keys(search)
    links = []
    while len(links) == 0:
        sleep(0.5)
        lst = driver.find_elements_by_tag_name('a')
        for i in lst:
            if search in i.get_attribute('href') and "tags" not in i.get_attribute('href') and "locations" not in i.get_attribute('href'):
                links.append(i.get_attribute('href'))
    follow(links)
def follow(links):
    sleep(1)
    for i in links:
        driver.get(i)
        sleep(0.5)
        f_1 = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
        if len(f_1) == 1:
            f_1[0].click()
for i in range(10):
    open_ins()
sleep(10)
driver.quit()
