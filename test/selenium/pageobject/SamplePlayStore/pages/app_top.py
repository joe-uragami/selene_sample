
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test.selenium.pageobject.SamplePlayStore.pages.app_detail import AppDetailPage


class AppTopPage:

    TITLE = "Google Play の Android アプリ"
    URL = "https://play.google.com/store/apps"

    APP_1ST_DETAIL_SELECTER = ".id-card-list :nth-child(1) div a"

    def __init__(self, driver=None):
        self.driver = driver
        WebDriverWait(self.driver, 10).until(
            EC.title_is(self.TITLE)
        )

    def get_url(self):
        return self.driver.current_url

    def click_first_appcard(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.APP_1ST_DETAIL_SELECTER))
        )
        element.click()
        return AppDetailPage(self.driver)
