from pages.login_page import LoginPage

def test_user_can_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("Artix14", "Moloko2024!")

    assert login_page.get_welcome_text() == "Welcome to Jenkins!"