from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage

class LoginPage(BasePage):
    USERNAME = (By.ID, "j_username")
    PASSWORD = (By.ID, "j_password")
    SUBMIT = (By.NAME, "Submit")
    WELCOME_TEXT = (By.XPATH, "//h1[text()='Welcome to Jenkins!']")  # Пример XPath, если элемент с таким текстом

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

    def get_welcome_text(self):
        return self.get_text(self.WELCOME_TEXT)  # Получаем текст с элемента с XPath, который содержит текст "Welcome to Jenkins!"