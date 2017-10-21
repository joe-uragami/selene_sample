from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppDetailPage:

    TITLE_SUFFIX = "Google Play の Android アプリ"
    URL = "https://play.google.com/store/apps/details"

    def __init__(self, driver=None):
        self.driver = driver
        WebDriverWait(self.driver, 10).until(
            EC.title_contains(self.TITLE_SUFFIX)
        )

    def get_url(self):
        return self.driver.current_url
