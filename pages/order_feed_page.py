import allure
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage




class OrderFeedPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def order_feed_page_loading_wait(self):
        self.wait_for_element_hide(OrderFeedLocators.OVERLAY)

    @allure.step('Подождать заголовка Лента Заказов')
    def wait_for_order_feed_header(self):
        self.wait_for_element(OrderFeedLocators.ORDER_FEED_HEADER)

    @allure.step('Кликнуть на заказ')
    def click_on_order(self):
        self.order_feed_page_loading_wait()
        self.wait_for_element(OrderFeedLocators.ORDER_IN_FEED)
        self.put_cursor_and_click_on_element(OrderFeedLocators.ORDER_IN_FEED)
        self.order_feed_page_loading_wait()



    @allure.step('Взять номер заказа из истории заказов в ленте')
    def get_order_number_from_order_feed_history(self):
        self.order_feed_page_loading_wait()
        self.get_text_on_element(OrderFeedLocators.ORDER_NUMBER_IN_LIST)


    @allure.step('Найти окно с деталями заказа')
    def find_order_details_window(self):
        self.wait_for_element(OrderFeedLocators.ORDER_DETAILS_WINDOW_COMPOUND_LIST)
        element = self.find_element(OrderFeedLocators.ORDER_DETAILS_WINDOW_COMPOUND_LIST)
        return element


    @allure.step('Найти номер заказа в окне В работе или Выполнено')
    def find_order_number_in_work_list(self):
        self.order_feed_page_loading_wait()
        # Пытаемся найти номер заказа в окне "В работе"
        order_in_work  = self.find_element(OrderFeedLocators.ORDER_IN_WORK_LIST)
        if order_in_work is not None:
            return order_in_work.text.strip()
            # Если не нашли в "В работе", пытаемся найти в окне "Выполнено"
        order_in_done = self.find_element(OrderFeedLocators.ORDER_NUMBER_IN_DONE_LIST)
        if order_in_done is not None:
            return order_in_done.text.strip()
        raise AssertionError





    @allure.step('Найти счетчик в окне Выполнено за все время')
    def find_counter_in_orders_done_all_time(self):
        self.order_feed_page_loading_wait()
        self.wait_for_element(OrderFeedLocators.ALL_ORDERS_DONE_COUNT)
        element = self.find_element(OrderFeedLocators.ALL_ORDERS_DONE_COUNT).text
        return element


    @allure.step('Найти счетчик в окне Выполнено за сегодня')
    def find_counter_in_orders_done_today(self):
        self.order_feed_page_loading_wait()
        self.wait_for_element(OrderFeedLocators.TODAY_ORDERS_DONE_COUNT)
        self.scroll_to_element(OrderFeedLocators.TODAY_ORDERS_DONE_COUNT)
        element = self.find_element(OrderFeedLocators.TODAY_ORDERS_DONE_COUNT).text
        return element



