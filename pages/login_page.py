import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage




class LoginPage(BasePage):

    @allure.step('Подождать заголовка Вход')
    def wait_for_enter_header(self):
        self.wait_for_element(LoginPageLocators.ENTER_HEADER)

    @allure.step('Заполнить форму для логина')
    def fill_login_data_form(self, login_data):
        self.send_keys_to_input(LoginPageLocators.EMAIL_FIELD, login_data['email'])
        self.send_keys_to_input(LoginPageLocators.PASSWORD_FIELD, login_data['password'])

    @allure.step('Кликнуть на кнопку Войти')
    def click_on_login_button(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Подождать исчезновение оверлэй')
    def wait_overlay_to_disappear_login(self):
        self.wait_for_overlay_to_disappear(LoginPageLocators.OVERLAY)



