from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Header(Page):
    Search_BTN=(By.CSS_SELECTOR,".icon.icon-search.modal__toggle-open")
    Search_product_icon=(By.CSS_SELECTOR,"button[type='submit']")
    SEARCH_BOX = (By.NAME, 'q')

    def click_search(self):
     #  self.wait_for_element_click(*self.Search_BTN)

        self.click(*self.Search_BTN)
            #sleep(6)
    def input_search(self,text):
        #self.wait_for_element_click(*self.Search_BTN)
       # self.wait_for_element_appear(*self.SEARCH_BOX).send_key(text)
        #self.click(*self.Search_BTN)
       self.input_text(text, *self.SEARCH_BOX)
        # sleep(8)

    def click_search_product(self):
         # self.wait_for_element_click(*self.Search_product_icon)
           self.click(*self.Search_product_icon)


