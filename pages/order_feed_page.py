import allure

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage




class OrderFeedPage(BasePage):

    @allure.step('Подождать заголовка Восстановление пароля')
    def wait_for_password_recovery_header(self):
        self.wait_for_element(OrderFeedLocators.ORDER_FEED_HEADER)

    @allure.step('Кликнуть на заказ')
    def click_on_order(self):
        self.click_on_element(OrderFeedLocators.ORDER_FEED_HISTORY)

    @allure.step('Подождать открытия окна с информацией о заказе')
    def wait_for_order_details_window(self):
        self.wait_for_element(OrderFeedLocators.ORDER_DETAILS_WINDOW_COMPOUND_LIST)

    @allure.step('Взять номер заказа из истории заказов в ленте')
    def get_order_number_from_order_feed_history(self):
        self.get_text_on_element(OrderFeedLocators.ORDER_NUMBER_IN_LIST)

    @allure.step('Подождать исчезновение оверлэй')
    def wait_overlay_to_disappear_order_feed(self):
        self.wait_for_overlay_to_disappear(OrderFeedLocators.OVERLAY)

