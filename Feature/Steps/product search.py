from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from behave import given, when, then
from time import sleep
from selenium import webdriver




@given('Open Cure website')
def open_web(context):
    context.app.main_page.open_page()


@then('click on search icon')
def click_search(context):

     context.app.header_page.click_search()


@when('Input {text} in the  search field')
def input_search(context,text):
    # search = context.driver.find_element(*SEARCH_INPUT)
   # search.clear()
   # search.send_keys('cure Skin gel')

    context.app.header_page.input_search(text)
    sleep(4)

@then('Click on search product')
def click_search_icon(context):
   #  context.driver.find_element_by_css_selector(*Search_BTN).click()
   # sleep(1)
    context.app.header_page.click_search_product()

@then('Verify products are returned')
def verify_product(context):
    pass

#