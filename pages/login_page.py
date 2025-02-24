import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage




class LoginPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def login_page_loading_wait(self):
        self.wait_for_element_hide(LoginPageLocators.OVERLAY)


    @allure.step('Найти заголовок Вход')
    def find_enter_header(self):
        self.login_page_loading_wait()
        self.wait_for_element(LoginPageLocators.ENTER_HEADER)
        self.find_element(LoginPageLocators.ENTER_HEADER)


    @allure.step('Заполнить форму для логина')
    def fill_login_data_form(self, login_data):
        self.login_page_loading_wait()
        self.send_keys_to_input(LoginPageLocators.EMAIL_FIELD, login_data['email'])
        self.send_keys_to_input(LoginPageLocators.PASSWORD_FIELD, login_data['password'])


    @allure.step('Навести курсор на элемент и кликнуть')
    def put_cursor_and_click_on_login_button(self):
        self.put_cursor_and_click_on_element(LoginPageLocators.LOGIN_BUTTON)
        self.login_page_loading_wait()





