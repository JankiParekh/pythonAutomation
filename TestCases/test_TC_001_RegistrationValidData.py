from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from BaseFiles import InitialDriver
from Libraries import configReader
from Pages import RegistrationPage
from DataGenerator import dataGenrate
import pytest

@pytest.mark.parametrize('data', dataGenrate.dataGenerator())
def test_validate_registration(data):
    driver = InitialDriver.startBrowser()
    register = RegistrationPage.RegistrationClass(driver)
    register.fillupRegistrationForm(data)
