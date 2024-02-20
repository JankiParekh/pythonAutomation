from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from Libraries import configReader

class RegistrationClass:

    def __init__(self, obj):
        global driver
        driver = obj

    def fillupRegistrationForm(self, data):
        driver.find_element(By.XPATH, configReader.readElementLocators('Registration', 'registration_btn')).click()
        first_name = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, configReader.readElementLocators('Registration', 'firstNameLocator'))))
        #first_name.send_keys(configReader.readData('Registration', 'firstNameData'))
        first_name.send_keys(data[0])
        #driver.find_element(By.XPATH,configReader.readElementLocators('Registration', 'lastNameLocator'))\
         #   .send_keys(configReader.readData('Registration', 'lastNameData'))
        driver.find_element(By.XPATH,configReader.readElementLocators('Registration', 'lastNameLocator'))\
            .send_keys(data[1])
        driver.find_element(By.XPATH,configReader.readElementLocators('Registration', 'emailLocator'))\
            .send_keys(configReader.readData('Registration', 'emailData'))
        driver.find_element(By.XPATH, configReader.readElementLocators('Registration', 'reEnterEmailLocator'))\
            .send_keys(configReader.readData('Registration', 'emailData'))
        password = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID,configReader.readElementLocators('Registration', 'passwordLocator') )))
        password.send_keys(configReader.readData('Registration', 'passwordData'))
        month = Select(driver.find_element(By.XPATH,configReader.readElementLocators('Registration', 'monthLocator') ))
        month.select_by_index(0)
        date = Select(driver.find_element(By.NAME, configReader.readElementLocators('Registration', 'dateLocator')))
        date.select_by_value(configReader.readData('Registration', 'dateData'))
        year = Select(driver.find_element(By.ID, configReader.readElementLocators('Registration', 'yearLocator')))
        year.select_by_visible_text(configReader.readData('Registration', 'yearData'))
        driver.find_element(By.XPATH, configReader.readElementLocators('Registration', 'genderFemaleLocator')).click()
        driver.execute_script("window.scrollTo(0,500);")
        time.sleep(2)
        driver.get_screenshot_as_file("C:/Users/tjpar/PycharmProjects/FrameworkStructureAutomation/firstScreenshot.png")
