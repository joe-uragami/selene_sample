import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# class SampleGoogleTest(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
#
#     def test_Googleで検索する(self):
#         driver = self.driver
#         driver.get('http://google.com')
#
#         expected = "Hello world"
#         driver.find_element_by_id('lst-ib').send_keys(expected)
#         driver.find_element_by_css_selector('input[type="submit"]').click()
#
#         assert expected in driver.title
#
#     def tearDown(self):
#         self.driver.close()

class SamplePlayStoreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

    def tearDown(self):
        self.driver.close()

    def test_PlayStoreでアプリの詳細画面に遷移(self):
        driver = self.driver
        driver.get("https://play.google.com/store")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".id-corpus-nav-list :nth-child(2) a"))
        )
        driver.find_element_by_css_selector(".id-corpus-nav-list :nth-child(2) a").click()

        WebDriverWait(driver, 10).until(
            EC.title_is("Google Play の Android アプリ")
        )
        assert "https://play.google.com/store/apps" in driver.current_url

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".id-card-list :nth-child(1) div a"))
        )
        element.click()

        WebDriverWait(driver, 10).until(
            EC.title_contains("Google Play の Android アプリ")
        )
        assert "https://play.google.com/store/apps/details" in driver.current_url


if __name__ == "__main__":
    unittest.main()
