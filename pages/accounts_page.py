import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test = ""

class AccountsPage():

    def __init__(self, driver):
        self.driver = driver

    def get_incorrect_credentials_accounts(self):
        account_lines = self.driver.find_elements(By.XPATH, "//*[@id='managed-accounts']/table/tbody//tr")
        pencil_buttons = []
        for i in range(1, len(account_lines) + 1):
            access_button = self.driver.find_element(
                By.XPATH, f"//*[@id='managed-accounts']/table/tbody/tr[{i}]/td[11]/account-analysis-actions2/div")
            msg = access_button.get_attribute('data-original-title')

            if msg == "The client provided incorrect credentials. Please click here for more details.":
                pencil_buttons.append(f"//*[@id='managed-accounts']/table/tbody/tr[{i}]//td[12]/a/i")

        return pencil_buttons

    def open_accounts_from_credential(self):
        accounts_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='tab-icon ng-binding' and text()='Accounts']")))
        time.sleep(3)
        accounts_button.click()

    def update_user_credentials(self, buttons_list):
        for button in buttons_list:
            self.driver.find_element(By.XPATH, button).click()

            self.driver.find_element(By.XPATH, "//a[@class='btn text-14 btn-light-blue text-uppercase']").click()

            self.driver.find_element(By.ID, "LOGIN").send_keys("test_userid") # Fill user ID
            self.driver.find_element(By.ID, "PASSWORD").send_keys("test_password") # Fill password

            # Some credentials UI does not contain login options, only user-ID and password
            try:
                self.driver.find_element(By.ID, "OP_OPTION").click() # Open login options
                self.driver.find_element(
                    By.XPATH, "//option[@label='One-Time Password']").click() # Choose One-Time Password
            except:
                pass

            sub_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "account-login-btn")))
            sub_button.click()

            # Wait until connection attempt ends
            WebDriverWait(self.driver, 120).until_not(EC.visibility_of_element_located((By.ID, "account-login-btn")))

            print(f"Output {buttons_list.index(button)} : ",  WebDriverWait(self.driver, 120).until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='text-18 red bold ng-binding ng-scope']"))).text)

            self.open_accounts_from_credential()




