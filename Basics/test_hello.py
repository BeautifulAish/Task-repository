print("hello")

# Selenium - 3 - Dis adv
# 1. We need to setup teh browserDrivers - to local machine
# Dis adv of sel 3
# We need to set up browser drivers

# Selenium 4
# W3C protocol, Selenium manager - Which automatically download browser driver
#Follow W3C Protocol, contains selenium manager- which will automatially download the browser driver
# QA- Focus on Writing Automation test cases
from selenium import webdriver

def test_open_login():
    driver = webdriver.Chrome()
    #It will create Basics session with post request(API POST request)
    # Open fresh chrome browser, session id is created
    #Session ID - 68614348f0cb4f521b963ed00eefbd0a
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    print(driver.title)

    time.sleep(5)
    driver.close() #Close will close the current window(tab)
    #It will not close other tabs
    #Session id =! null
    time.sleep(200)
