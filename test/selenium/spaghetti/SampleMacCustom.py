import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SampleMacCustomTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

    def tearDown(self):
        self.driver.close()

    def test_iMacのプロセッサを変えて値段変更(self):
        driver = self.driver
        driver.get("https://www.apple.com/jp/shop/buy-mac/imac?product=MNDY2J/A&step=config#")

        i5_current_price = driver.find_element_by_css_selector(".current_price").text
        assert "142,800" in i5_current_price

        driver.execute_script('window.scrollTo(0, 600);')
        driver.find_element_by_xpath(
            # '//*[@id="configuration-form"]/div[1]/div[2]/div/div[4]/div[1]/div[1]/div/div/fieldset/ul/li[2]'
            '//*[@id="configuration-form"]/div[1]/div[2]/div/div[4]/div[1]/div[1]/div/div/fieldset/div/div[2]'
        ).click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH,'//*[@id="configuration-form"]/div[1]/div[2]/div/div[3]/div[1]/div/ul/li[1]/span'),
                "Intel Core i7プロセッサ"
            )
        )
        i7_current_price = driver.find_element_by_css_selector(".current_price").text
        assert "175,800" in i7_current_price


if __name__ == "__main__":
    unittest.main()