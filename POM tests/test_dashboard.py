from pages.login_page import LoginPage

def test_user_lands_on_dashboard_after_login(driver):
    login = LoginPage(driver)
    dashboard = login.login_and_go_to_dashboard("Artix14", "Moloko2024!")
    assert dashboard.get_title() == "Welcome to Jenkins!"