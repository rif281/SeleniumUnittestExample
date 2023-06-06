import sys
sys.path.append("..")
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.accounts_page import AccountsPage


class PendingAccountsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_pending_accounts(self):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.login("username", "password")

        home_page = HomePage(self.driver)
        home_page.navigate_to_accounts()

        accounts_page = AccountsPage(self.driver)
        init_incorrect_accounts = accounts_page.get_incorrect_credentials_accounts()
        init_count = len(init_incorrect_accounts)
        accounts_page.update_user_credentials(init_incorrect_accounts)
        final_incorrect_accounts = accounts_page.get_incorrect_credentials_accounts()
        final_count = len(final_incorrect_accounts)

        home_page.logout()

        self.assertTrue(init_count == final_count, "Initial and final accounts count are not equal")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
