from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.dashboard_page import DashboardPage


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find(locator)
        element.click()

    def fill(self, locator, value):
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.find(locator).text

    def get_title(self):
        return self.driver.title

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False