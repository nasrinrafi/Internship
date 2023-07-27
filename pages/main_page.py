from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    POP_UP_CLOSE = (By.XPATH, "//button[@class='popup-close']")
    def open_page(self):
        self.open_url('https://shop.cureskin.com')
        self.wait_for_element_click(*self.POP_UP_CLOSE)
