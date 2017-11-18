import unittest
from selenium import webdriver

from test.selenium.pageobject.SampleAppleStore.pages.imac_custom_page import iMacCustomPage


class test_custom_price(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

    def tearDown(self):
        self.driver.close()

    def test_iMacのプロセッサをアップして価格変更(self):

        custom_page = iMacCustomPage(self.driver)
        custom_page.open()

        assert "142,800" in custom_page.get_price()

        custom_page.select_i7()

        assert "175,800" in custom_page.get_price()



