import time

import allure

from curl import Url
from data import DataForUser
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage



class TestPasswordRecovery:
    @allure.title('Test open Password recovery page by clicking on Password recovery button')
    def test_password_recovery_page_redirect(self, driver):
        main_page = MainPage(driver)
        password_recovery_page = PasswordRecoveryPage(driver)

        main_page.click_on_enter_account_button()
        password_recovery_page.wait_for_password_recovery_button()
        password_recovery_page.click_on_password_recovery_button()
        password_recovery_page.wait_for_password_recovery_header()

        assert Url.PASSWORD_RECOVERY_URL in password_recovery_page.get_current_url()

    @allure.title('Test enter email and click on Recovery button')
    def test_click_on_recover_button_with_entered_email(self, driver, open_password_recovery_page):
        password_recovery_page = open_password_recovery_page

        password_recovery_page.wait_for_password_recovery_header()
        password_recovery_page.send_keys_to_input(PasswordRecoveryLocators.EMAIL_FIELD, DataForUser.EMAIL)
        password_recovery_page.click_on_recovery_button()
        password_recovery_page.password_page_loading_wait()
        password_recovery_page.wait_for_password_field()

        assert Url.RESET_PASSWORD_URL in password_recovery_page.get_current_url()

    @allure.title('Test click on hide/unhide password icon makes the password field highlighted')
    def test_click_on_unhide_password_icon_highlight_password_field(self, driver, open_password_recovery_page):
        password_recovery_page = open_password_recovery_page
        password_recovery_page.wait_for_password_recovery_header()

        password_recovery_page.send_keys_to_input(PasswordRecoveryLocators.EMAIL_FIELD, DataForUser.EMAIL)

        password_recovery_page.click_on_recovery_button()
        password_recovery_page.password_page_loading_wait()
        password_recovery_page.wait_for_password_field()

        password_recovery_page.click_on_overlaid_element(PasswordRecoveryLocators.HIDE_UNHIDE_PASSWORD_ICON)

        password_recovery_page.wait_for_password_field_highlighted()
        time.sleep(1)
        highlighted_field = password_recovery_page.find_password_highlighted_field()
        assert highlighted_field.is_displayed()







