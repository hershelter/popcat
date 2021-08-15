from selenium import webdriver
import time

chrome = webdriver.Chrome('C:\python\py\爬蟲,機器人\chromedriver.exe')
chrome.get("https://popcat.click/")
sum_t=0
time.sleep(5)
login=chrome.find_element_by_class_name("title") 
time_start = time.time()
while 1==1:
    login.click()
    
    test = chrome.find_element_by_class_name('counter rot-l').text
    if test==100:
        break
    

time_end = time.time()    #結束計時

sum_t=(time_end - time_start)+sum_t   #執行所花時間
print('time cost', sum_t, 's')