from selenium.webdriver.common.by import By
from Page.Base_page import Pages


class Header(Pages):

   SEARCH_INPUT = (By.NAME,'q')
   Add_card =(By.NAME,'ADD')
   Search_BTN=(By.CSS_SELECTOR,'button[type="submit"]')


   def input_search(self):
      self.input_text('cure Skin gel', *self.SEARCH_INPUT)


   def click_search(self):
        self.click(*self.Search_BTN)

