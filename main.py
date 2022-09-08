from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("start!")
driver = webdriver.Chrome("C:/Users/82109/Desktop/chromedriver_win32/chromedriver.exe")

driver.implicitly_wait(3)
driver.get("https://kr.indeed.com/jobs?q=python&l=&vjk=d364360d1e0368e3")
