import ..

#Chrome -- #Chrome Options
#Edge - Edge options
# Firefox - Firefox options

def test_open_login():
    driver= webdriver.Chrome()
    driver.get("https://google.com")
    print(driver.title)

    time.sleep(5)
    driver.close() #Close will close current window(tab)
    #It will not close other tabs

    driver.quit()
    #Close all the tabs
    #Session ==None
