print("hello")

# Selenium - 3 - Dis adv
# 1. We need to setup teh browserDrivers - to local machine
# Dis adv of sel 3
# We need to set up browser drivers

# Selenium 4
# W3C protocol, Selenium manager - Which automatically download browser driver
# Follow W3C Protocol, contains selenium manager - which will automatically download the browser driver
# QA- Focus on Writing Automation test cases
from selenium import webdriver


def test_open_login():
    driver = webdriver.Chrome()
    #Create session with POST Request (API POST Request).
    #Fresh Chrome will open,Session ID, is created
    # Session ID - Close ID will be created 68614348f0cb4f521b963ed00eefbd0a
    driver.get("https://app.vwo.com")
    print(driver.title)

#Quit browser and quit all windows
#Session id = null
    driver.quit()

