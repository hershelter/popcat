from selenium import webdriver
import time

chrome = webdriver.Chrome('C:\python\py\爬蟲,機器人\chromedriver.exe') //chromedriver位置
chrome.get("https://popcat.click/")

time.sleep(5)
login=chrome.find_element_by_class_name("title") 

while 1==1:
    login.click()
    
