# Selenium - is a suite of tools which automates browser or we can say automates the control of browser.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_browser = webdriver.Chrome()

# chrome_browser.fullscreen_window() #open fullscreen chrome
# chrome_browser.maximize_window() #maximize the chrome tab
# time.sleep(10) #keep browser on for 10 sec.

chrome_browser.get("https://www.selenium.dev/documentation/webdriver/") #go to specific website endpoint

# print("WebDriver" in chrome_browser.title) #check if the given text exists in browser title.
# assert 'WebDriver' in chrome_browser.title #same as above
# sec_index = chrome_browser.find_element(By.CLASS_NAME, "section-index")
# print(sec_index.get_attribute('innerHTML'))

user_message = chrome_browser.find_element(By.CLASS_NAME, "DocSearch-Input")
user_message.clear()
user_message.send_keys('I ma extra Cool')

chrome_browser.fullscreen_window() #open fullscreen chrome
chrome_browser.maximize_window() #maximize the chrome tab
time.sleep(10) #keep browser on for 10 sec.

chrome_browser.close()
chrome_browser.quit()