from selenium import webdriver
import time

def test_open_login():
    Chrome_options = webdriver.ChromeOptions()
    # Give some extra argument or extension or anything to chrome.
    # Chrome_options - Chrome with extension,window size,proxy Js disabled.

    extension_path = "/users/Aishwarya/Downloads/Addblocker.crx"
    Chrome_options.add_extension(extension_path)

    Chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=Chrome_options)  # Fresh chrome which doesn't have any extensions
    driver.get("https://app.vwo.com")

    print(driver.title)
    time.sleep(1000)
    #driver.quit() #Quit browsers and close all windows
