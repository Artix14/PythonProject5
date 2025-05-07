from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage  # импортируем

class LoginPage(BasePage):
    USERNAME = (By.ID, "j_username")
    PASSWORD = (By.ID, "j_password")
    SUBMIT = (By.NAME, "Submit")

    def open(self):
        self.driver.get("http://localhost:8080")

    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def login_and_go_to_dashboard(self, username, password):
        self.open()
        self.login(username, password)
        return DashboardPage(self.driver)

    def login_and_go_to_dashboard(self, username, password):
        print(">>> login_and_go_to_dashboard called")  # отладка
        self.open()
        self.login(username, password)
        return DashboardPage(self.driver)