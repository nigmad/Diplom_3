import allure

from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage




class PasswordRecoveryPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def password_page_loading_wait(self):
        self.wait_for_element_hide(PasswordRecoveryLocators.OVERLAY)

    @allure.step('Подождать заголовка Восстановление пароля')
    def wait_for_password_recovery_header(self):
        self.wait_for_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_HEADER)

    @allure.step('Подождать отображения кнопки Восстановление пароля')
    def wait_for_password_recovery_button(self):
        self.wait_for_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Кликнуть на кнопку Восстановить пароль')
    def click_on_password_recovery_button(self):
        self.click_on_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Подождать появления поля ввода пароля')
    def wait_for_password_field(self):
        self.wait_for_element(PasswordRecoveryLocators.PASSWORD_FIELD)

    @allure.step('Кликнуть на иконку показать пароль')
    def click_on_unhide_password_icon(self):
        self.click_on_element(PasswordRecoveryLocators.HIDE_UNHIDE_PASSWORD_ICON)

    @allure.step('Кликнуть на кнопку под полем email Восстановить')
    def click_on_recovery_button(self):
        self.click_on_element(PasswordRecoveryLocators.RECOVERY_BUTTON)


    @allure.step('Найти подсвечивание поля пароля')
    def find_password_highlighted_field(self):
        return self.find_element(PasswordRecoveryLocators.PASSWORD_FIELD_HIGHLIGHTED)

    @allure.step('Подождать подсвечивание поля пароля')
    def wait_for_password_field_highlighted(self):
        self.wait_for_element(PasswordRecoveryLocators.PASSWORD_FIELD_HIGHLIGHTED)






