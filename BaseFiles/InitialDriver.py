from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Libraries import configReader

def startBrowser():
    global driver
    if((configReader.readConfigData('Details', 'Browser')) == "Chrome"):
        driver = Chrome()
    elif((configReader.readConfigData('Details', 'Browser')) == "Firefox"):
        driver = Firefox()
    else:
        driver = Chrome()
    driver.get(configReader.readConfigData('Details', 'Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()
