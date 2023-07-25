
from Page.Header_page import Header
from Page.main_page import MainPage


class Application:
    def _init_(self, driver):
        self.driver = driver
        self.main_page = MainPage
        self.Header = Header


#app =Application('driver')
#app.main_page.open_page()
#app.Header.click_search()

