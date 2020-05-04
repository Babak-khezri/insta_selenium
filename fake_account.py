from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import sample , randint
from time import sleep
name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ123456789"
email = "".join(sample(name,8)) + '@gmail.com'
fullname = 'acount' + ''.join(sample(list(map(str,range(10))),3))
username = 'real' + "".join(sample(name,5))
password = "".join(sample(name,10))
print(username)
driver = webdriver.Chrome()  # Create the driver
driver.get('https://www.instagram.com/')
sleep(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span').click()
sleep(2)
driver.find_element_by_xpath('//input[@name="emailOrPhone"]').send_keys(email)
driver.find_element_by_xpath('//input[@name="fullName"]').send_keys(fullname)
driver.find_element_by_xpath('//input[@name="username"]').send_keys(username)
driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[16]').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button').click()