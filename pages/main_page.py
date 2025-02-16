import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Кликнуть на Конструктор')
    def click_on_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть на Лента заказов')
    def click_on_order_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликнуть на Личный кабинет')
    def click_on_personal_account(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликнуть на Войти в аккаунт')
    def click_on_enter_account_button(self):
        self.click_on_element(MainPageLocators.ENTER_BUTTON)

    @allure.step('Подождать появления кнопки Личный кабинет')
    def wait_for_personal_account_button(self):
        self.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Подождать исчезновение оверлэй')
    def wait_overlay_to_disappear_main(self):
        self.wait_for_overlay_to_disappear(MainPageLocators.OVERLAY)

    @allure.step('Подождать появления кнопки Конструктор')
    def wait_for_constructor_button(self):
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_BUTTON)










