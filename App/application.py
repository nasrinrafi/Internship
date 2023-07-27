
from pages.header_page import Header
from pages.main_page import MainPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header_page = Header(self.driver)


#app =Application('driver')
#app.main_page.open_page()
#app.Header.click_search()

