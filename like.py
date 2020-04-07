from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

name = input("enter the hashtag : ")
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
sleep(4)
driver.find_element_by_xpath('//input[@name="username"]').send_keys('selenium__py')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('1379bk@15')
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
sleep(2)

driver.get('https://www.instagram.com/explore/tags/{}/'.format(name))
sleep(2)
lst = driver.find_elements_by_tag_name('a')
links = []
for i in lst:
    if 'com/p/' in i.get_attribute('href'):
        links.append(i.get_attribute('href'))
for i in links:
    driver.get(i)
    sleep(0.5)
    driver.find_element_by_class_name('wpO6b').click()
sleep(10)
driver.quit()