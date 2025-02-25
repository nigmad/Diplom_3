import allure
from curl import Url
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage



class TestPasswordRecovery:
    @allure.title('Test open Password recovery page by clicking on Password recovery button')
    def test_password_recovery_page_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_enter_account_button()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_on_password_recovery_button()
        password_recovery_page.wait_for_password_recovery_header()
        assert Url.PASSWORD_RECOVERY_URL in password_recovery_page.get_current_url()

    @allure.title('Test enter email and click on Recovery button')
    def test_click_on_recover_button_with_entered_email(self, driver, open_password_recovery_page):
        password_recovery_page = open_password_recovery_page
        password_recovery_page.fill_email_field()
        password_recovery_page.click_on_recovery_button()
        password_recovery_page.wait_for_password_field()
        assert Url.RESET_PASSWORD_URL in password_recovery_page.get_current_url()

    @allure.title('Test click on hide/unhide password icon makes the password field highlighted')
    def test_click_on_unhide_password_icon_highlight_password_field(self, driver, open_password_recovery_page):
        password_recovery_page = open_password_recovery_page
        password_recovery_page.fill_email_field()
        password_recovery_page.click_on_recovery_button()
        password_recovery_page.wait_for_password_field()
        password_recovery_page.click_on_unhide_password_icon()
        highlighted_field = password_recovery_page.find_password_highlighted_field()
        assert highlighted_field.is_displayed()







