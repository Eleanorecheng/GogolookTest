from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except Exception as e:
                raise e


