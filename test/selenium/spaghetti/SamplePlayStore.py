import unittest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SamplePlayStoreTest(unittest.TestCase):

    def setUp(self):

        # options = Options()
        # options.add_argument('--headless')
        #
        # self.driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/local/bin/chromedriver')

        self.driver = webdriver.Firefox(
            executable_path='/usr/local/bin/geckodriver')

    def tearDown(self):
        self.driver.close()

    def test_PlayStoreでアプリの詳細画面に遷移(self):
        driver = self.driver
        driver.get("https://play.google.com/store")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".id-corpus-nav-list :nth-child(2) a")
            )
        )
        driver.find_element_by_css_selector(
            ".id-corpus-nav-list :nth-child(2) a").click()

        WebDriverWait(driver, 10).until(
            EC.title_is("Google Play の Android アプリ")
        )
        assert "https://play.google.com/store/apps" in driver.current_url

        driver.execute_script('window.scrollTo(0, 400);')
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".id-card-list :nth-child(1) div a")
            )
        )
        element.click()

        WebDriverWait(driver, 10).until(
            EC.title_contains("Google Play の Android アプリ")
        )
        assert "https://play.google.com/store/apps/details" \
               in driver.current_url


if __name__ == "__main__":
    unittest.main()
