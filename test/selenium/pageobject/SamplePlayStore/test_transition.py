import unittest
from selenium import webdriver

from test.selenium.pageobject.SamplePlayStore.pages.store_top import TopPage


class test_transition(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

    def tearDown(self):
        self.driver.close()

    def test_PlayStoreでアプリの詳細画面に遷移(self):

        top_page = TopPage(self.driver)
        top_page.open()

        app_top_page = top_page.click_app_tub()
        assert app_top_page.URL in app_top_page.get_url()

        first_app_detail_page = app_top_page.click_first_appcard()
        assert first_app_detail_page.URL in first_app_detail_page.get_url()






