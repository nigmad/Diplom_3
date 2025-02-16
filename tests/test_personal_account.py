import allure
from curl import Url
from locators.login_page_locators import LoginPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:
    @allure.title('Test click on Personal Account button by unauthorized user')
    def test_personal_account_page_redirect_unauthorized_user(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.click_on_personal_account()
        login_page.wait_for_enter_header()

        assert Url.LOGIN_URL in login_page.get_current_url()

    @allure.title('Test click on Personal Account button by registered user')
    def test_personal_account_page_redirect_registered_user(self, driver, login_fixture):
        login_data = login_fixture
        main_page = MainPage(driver)

        main_page.click_on_personal_account()
        login_page = LoginPage(driver)
        login_page.fill_login_data_form(login_data)
        login_page.click_on_login_button()
        login_page.wait_overlay_to_disappear_login()

        main_page = MainPage(driver)
        main_page.wait_for_personal_account_button()
        main_page.click_on_personal_account()

        personal_page = PersonalAccountPage(driver)
        personal_page.wait_for_profile_button()
        assert Url.PERSONAL_ACCOUNT_URL in personal_page.get_current_url()




    @allure.title('Test click on Order History')
    def test_order_history_redirect(self, driver, login_and_go_to_personal_account):
        personal_page = login_and_go_to_personal_account

        personal_page.wait_for_order_history_button()
        personal_page.click_on_order_history_button()
        personal_page.wait_overlay_to_disappear_personal()

        assert Url.ORDER_HISTORY_URL in personal_page.get_current_url()

    @allure.title('Test exit from personal account')
    def test_exit_from_personal_account(self, driver, login_and_go_to_personal_account):
        personal_page = login_and_go_to_personal_account

        personal_page.wait_for_exit_button()
        personal_page.click_on_exit_button()
        personal_page.wait_for_element_not_visible(PersonalAccountLocators.OVERLAY)

        login_page = LoginPage(driver)

        login_page.wait_for_element_not_visible(LoginPageLocators.OVERLAY)
        import time
        time.sleep(10)

        assert Url.LOGIN_URL in login_page.get_current_url()























