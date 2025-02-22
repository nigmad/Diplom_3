import allure
from selenium.common import NoSuchElementException
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
        self.click_on_element(OrderFeedLocators.ORDER_IN_FEED)

    @allure.step('Подождать открытия окна с информацией о заказе')
    def wait_for_order_details_window(self):
        self.wait_for_element(OrderFeedLocators.ORDER_DETAILS_WINDOW_COMPOUND_LIST)

    @allure.step('Взять номер заказа из истории заказов в ленте')
    def get_order_number_from_order_feed_history(self):
        self.get_text_on_element(OrderFeedLocators.ORDER_NUMBER_IN_LIST)


    @allure.step('Найти окно с деталями заказа')
    def find_order_details_window(self):
        try:
            return self.driver.find_element(*OrderFeedLocators.ORDER_DETAILS_WINDOW_COMPOUND_LIST)
        except NoSuchElementException:

            raise AssertionError("not found")


    @allure.step('Найти номер заказа в окне В работе или Выполнено')
    def find_order_number_in_work_list(self):
        try:
            # Пытаемся найти номер заказа в окне "В работе"
            order_number = self.driver.find_element(*OrderFeedLocators.ORDER_IN_WORK_LIST).text
            return order_number
        except NoSuchElementException:
            # Если не нашли в "В работе", пытаемся найти в окне "Выполнено"
            try:
                order_number = self.driver.find_element(*OrderFeedLocators.ORDER_NUMBER_IN_DONE_LIST).text
                return order_number
            except NoSuchElementException:
                raise AssertionError("Номер заказа не найден ни в окне 'В работе', ни в окне 'Выполнено'")



    @allure.step('Найти счетчик в окне Выполнено за все время')
    def find_counter_in_orders_done_all_time(self):
        try:
            return self.driver.find_element(*OrderFeedLocators.ALL_ORDERS_DONE_COUNT).text
        except NoSuchElementException:

            raise AssertionError("not found")

    @allure.step('Найти счетчик в окне Выполнено за сегодня')
    def find_counter_in_orders_done_today(self):
        try:
            return self.driver.find_element(*OrderFeedLocators.TODAY_ORDERS_DONE_COUNT).text
        except NoSuchElementException:

            raise AssertionError("not found")

    @allure.step('Скролл до Выполнено за сегодня')
    def scroll_to_orders_done_today(self):
        self.scroll_to_element(OrderFeedLocators.TODAY_ORDERS_DONE_COUNT)


    @allure.step('Подождать количество заказов в ленте из счетчика')
    def wait_for_order_details_window(self):
        self.wait_for_element(OrderFeedLocators.ALL_ORDERS_DONE_COUNT)

