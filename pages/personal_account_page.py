import allure

from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def personal_page_loading_wait(self):
        self.wait_for_element_hide(PersonalAccountLocators.OVERLAY)

    @allure.step('Подождать заголовка Профиль')
    def wait_for_profile_button(self):
        self.wait_for_element(PersonalAccountLocators.PROFILE_TEXT_BUTTON)

    @allure.step('Подождать кнопки История заказов')
    def wait_for_order_history_button(self):
        self.wait_for_element(PersonalAccountLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Кликнуть на История заказов')
    def click_on_order_history_button(self):
        self.click_on_overlaid_element(PersonalAccountLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Кликнуть на История заказов')
    def click_on_order_feed_button(self):
        self.click_on_overlaid_element(PersonalAccountLocators.ORDER_FEED_BUTTON)

    @allure.step('Подождать список с историей заказов')
    def wait_for_oder_history_list(self):
        self.wait_for_element(PersonalAccountLocators.ORDER_HISTORY_WINDOW)

    @allure.step('Подождать появления кнопки Выйти')
    def wait_for_exit_button(self):
        self.wait_for_element(PersonalAccountLocators.EXIT_BUTTON)

    @allure.step('Кликнуть на кнопку Выйти')
    def click_on_exit_button(self):
        self.click_on_overlaid_element(PersonalAccountLocators.EXIT_BUTTON)


    @allure.step('Подождать исчезновение оверлэй')
    def wait_overlay_to_disappear_personal(self):
        self.wait_for_overlay_to_disappear(PersonalAccountLocators.OVERLAY, timeout=30)

    @allure.step('Кликнуть на Конструктор')
    def click_on_constructor_from_personal_account(self):
        self.click_on_element(PersonalAccountLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Найти номер заказа в всплывающем окне об успешном заказе')
    def find_order_number_from_history(self):
        return self.find_element(PersonalAccountLocators.ORDER_HISTORY_ORDER_NUMBER)

    @allure.step('Взять номер заказа из истории заказов в ленте')
    def get_order_number_from_order_feed_history(self):
        self.get_text_on_element(PersonalAccountLocators.ORDER_HISTORY_ORDER_NUMBER)





