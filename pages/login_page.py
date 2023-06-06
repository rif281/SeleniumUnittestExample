import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("website_url")

    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, "loginEmail")
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "loginPassword")
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, "//span[@ng-show='!loginForm.$submitted']")
        login_button.click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

