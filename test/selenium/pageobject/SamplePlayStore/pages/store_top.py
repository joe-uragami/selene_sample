from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test.selenium.pageobject.SamplePlayStore.pages.app_top import AppTopPage


class TopPage:
    URL = "https://play.google.com/store"

    APP_TUB_SELECTER = ".id-corpus-nav-list :nth-child(2) a"

    def __init__(self, driver=None):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def click_app_tub(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.APP_TUB_SELECTER))
        )
        self.driver.find_element_by_css_selector(self.APP_TUB_SELECTER).click()
        return AppTopPage(self.driver)

