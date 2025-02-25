import allure
import pytest

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeedPage:
    @allure.title('Test click on order opens Order details pop up window')
    def test_open_order_details_by_clicking_on_order(self, driver, registered_user_placed_order):
        place_order = registered_user_placed_order
        main_page = MainPage(driver)
        main_page.click_on_order_feed()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_order()
        order_details = order_feed_page.find_order_details_window()
        assert order_details.is_displayed()


    @allure.title('Test order number from history is shown in order feed')
    def test_order_from_history_shown_in_feed(self, driver, registered_user_placed_order):
        place_order = registered_user_placed_order
        main_page = MainPage(driver)
        main_page.click_on_personal_account()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_on_order_history_button()
        personal_account_page.find_order_number_from_history()
        order_in_history = personal_account_page.get_order_number_from_history()

        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_in_feed = order_feed_page.get_order_number_from_order_feed_history()
        assert order_in_history == order_in_feed

    @allure.title('Test created order number appears in order feed work list')
    def test_order_number_appears_in_work_list(self, driver, registered_user_placed_order):
        order_number = registered_user_placed_order
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_number_in_work_list = order_feed_page.find_order_number_in_work_list()
        assert f'0{order_number}' == order_number_in_work_list






    @pytest.mark.parametrize(
        "counter_before_fixture, counter_after_method",
        [
            ("get_today_count_of_orders_before_new_order", "find_counter_in_orders_done_today"),
            ("get_all_time_count_orders_before_new_order", "find_counter_in_orders_done_all_time"),
        ]
    )
    @allure.title('Test counter Orders is increasing when new order has been created')
    def test_counter_increasing_due_to_new_order(self, driver, request, counter_before_fixture, counter_after_method, login_logout_fixture):
        counter_before = request.getfixturevalue(counter_before_fixture)
        main_page = login_logout_fixture

        main_page = MainPage(driver)
        main_page.place_order()
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        counter_after = getattr(order_feed_page, counter_after_method)()

        assert int(counter_before) < int(counter_after)













