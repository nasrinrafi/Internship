from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):

   SEARCH_INPUT = (By.NAME,'q')
   Add_card =(By.NAME,'ADD')
   Search_BTN=(By.CSS_SELECTOR,".icon.icon-search.modal__toggle-open")


   def input_search(self):
      self.input_text('cure Skin gel', *self.SEARCH_INPUT)


   def click_search(self):
        self.wait_for_element_click(*self.Search_BTN)

