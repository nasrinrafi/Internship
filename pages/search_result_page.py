from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
  SEARCH_RESULT = (By.CSS_SELECTOR,'a[href="/products/under-eye-gel?_pos=1&_sid=ccfdfc2ac&_ss=r]' )

  def verify_search_result(self):
      actual_result = self.driver.find_element(*self.SEARCH_RESULT).text
      expected_result = 'CureSkin gel'
      assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'