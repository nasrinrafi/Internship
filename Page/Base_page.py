
class Pages:


def click(self, *locator):
    self.driver.find_element(*locator).click()


def open_web(self, Url):
    self.driver.get(Url)


def input_text(self, text, *locator):
    self.driver.find_element(*locator).send_keys(text)


def verify_text(self, expected_text, *locator):
    actual_text = self.driver.find_element(*locator).text
    assert expected_text == actual_text, \
        f"Error! Actual text {actual_text} did not match Expected {expected_text}"
