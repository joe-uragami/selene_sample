
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class iMacCustomPage:

    TITLE = "iMacをカスタマイズ - Apple（日本）"
    URL = "https://www.apple.com/jp/shop/buy-mac/imac?product=MNDY2J/A&step=config#"
    I7_TEXT = "Intel Core i7プロセッサ"

    WAIT_SECOND = 10

    PRICE_SELECTOR = ".current_price"
    SCROLL_SCRIPT = 'window.scrollTo(0, 600);'
    # I7_BUTTON_XPATH = '//*[@id="configuration-form"]/div[1]/div[2]/div/div[4]/div[1]/div[1]/div/div/fieldset/ul/li[2]'
    I7_BUTTON_XPATH = '//*[@id="configuration-form"]/div[1]/div[2]/div/div[4]/div[1]/div[1]/div/div/fieldset/div/div[2]'
    SPECK_TEXT_XPATH = '//*[@id="configuration-form"]/div[1]/div[2]/div/div[3]/div[1]/div/ul/li[1]/span'

    def __init__(self, driver=None):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def get_price(self):
        return self.driver.find_element_by_css_selector(self.PRICE_SELECTOR).text

    def select_i7(self):
        self.driver.execute_script(self.SCROLL_SCRIPT)
        self.driver.find_element_by_xpath(self.I7_BUTTON_XPATH).click()

        WebDriverWait(self.driver, self.WAIT_SECOND).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, self.SPECK_TEXT_XPATH),self.I7_TEXT
            )
        )




