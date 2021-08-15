from selenium import webdriver
import time
chrome = webdriver.Chrome('C:\\Users\\user\\Desktop\\新增資料夾\\chromedriver.exe')
chrome.get("https://popcat.click/")
time.sleep(3)

login=chrome.find_element_by_class_name("title") 

while 1==1:
    login.click()
    
