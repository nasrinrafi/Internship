from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as firefoxOption
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import service
from selenium.webdriver.firefox.options import Options
from App.application import Application

#Options = firefoxOption()


def browser_init(context,test_name):
    """
    :param context: Behave context
    """
   # context.driver = webdriver.Chrome(executable_path="chromedriver")
    # context.browser = webdriver.Safari()
    context.browser = webdriver.Firefox(executable_path="geckodriver 2")
    context.driver = webdriver.firefox(service=service)
    #Options.add_argument("--Headless")
    #context.driver = webdriver.firefox(firefoxOption=Options, service=service)

    context.driver.wait = WebDriverWait(context.driver, 10)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
   # context.app = Application(driver=context.driver)

    desired_cap = {
         'browser': 'firefox',
         'browser_version': '91',
         'os': 'Windows',
         'os_version': '10',
          'name':test_name
    }
    Bs_user = 'nasrin11'
    Bs_key = 'ysFMjRqHpQSSoSrhMQfT'
    url = f'http://{Bs_user}:{Bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()



#allure result test#
#behave -f allure_behave.formatter:AllureFormatter -o test_results/ feature/Tests"