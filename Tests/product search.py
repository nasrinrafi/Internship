from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')


@given('Open cure skin website')
def open_google(context):
    context.driver.get('https://shop.cureskin.com/')


@when('Input cure in the  search field')
def input_search(context):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys('cure')
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element_by_css_selector('button[type="submit"]').click()
    sleep(1)


@then('Verify that 23 products are returned')
def verify_23_product(context):
    expected_product_count = 23
    actual_product_count = len(*SEARCH_INPUT)

    if actual_product_count == expected_product_count:
        print(f"Number of products returned: {actual_product_count}")
        print("Verification successful!")
    else:
        print(f"Expected {expected_product_count} products, but found {actual_product_count}")
        print("Verification failed!")

# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#  assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
