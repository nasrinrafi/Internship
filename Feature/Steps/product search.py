from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from behave import given, when, then
from time import sleep
from selenium import webdriver


SEARCH_INPUT = (By.NAME, 'q')
Add_card =(By.NAME,'ADD')
Search_BTN=(By.CSS_SELECTOR,'button[type="submit"]')


@given('Open Cure website')
def open_web(context):
   # context.driver = webdriver.Chrome(executable_path='./chromedriver')
    context.browser = webdriver.Firefox(executable_path="geckodriver 2")
    context.driver.maximize_window()
   # context.driver.get("https://shop.cureskin.com")

    context.app.main_page.open_page()

@when('Input cure in the  search field')
def input_search(context):
    # search = context.driver.find_element(*SEARCH_INPUT)
   # search.clear()
   # search.send_keys('cure Skin gel')
  #  sleep(4)
    context.app.Header_page.input_search()


@then('Click on search icon')
def click_search_icon(context):
   #  context.driver.find_element_by_css_selector(*Search_BTN).click()
   # sleep(1)
   context.app.Header_page.click_search()


@then('click on product')
def click_product(context):
    context.driver.find_element_by_css_selector("a[hraf='/products/under-eye-gel?_pos=1&_sid=026b9ffc5&_ss=r']").click()
    sleep(4)


@then('add to card')
def add_to_card(context):
    context.driver.find_element(*Add_card)





#@then('Verify that 23 products are returned')
#def verify_23_product(context):
   # expected_product_count = 23
  #  actual_product_count = len(*SEARCH_INPUT)

  #  if actual_product_count == expected_product_count:
   #     print(f"Number of products returned: {actual_product_count}")
   #     print("Verification successful!")
  #  else:
    #    print(f"Expected {expected_product_count} products, but found {actual_product_count}")
    #    print("Verification failed!")

# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#  assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
