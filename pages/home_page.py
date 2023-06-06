import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_accounts(self):
        accounts_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Accounts']")))
        time.sleep(3)
        accounts_button.click()

    def logout(self):
        drop = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "dropdown-menu-user")))
        drop.click()
        self.driver.find_element(By.XPATH, "//i[@class='glyphicon glyphicon-off margin-right-10']").click()