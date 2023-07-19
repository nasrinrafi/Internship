from selenium.webdriver.common.by import By
from Page.Base_page import Pages


class MainPage(Pages):

    def open_page(self):
        self.open_web('https://shop.cureskin.com')
