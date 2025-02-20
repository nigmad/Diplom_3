import time

import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeedPage:
    @allure.title('Test click on order opens Order details pop up window')
    def test_open_pop_up_order_details_by_clicking_on_order(self, driver, login_and_place_order_fixture):
        main_page = login_and_place_order_fixture
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.scroll_to_close_order_button()
        main_page.put_cursor_and_click_on_close_order_window()
        time.sleep(2)
        main_page.main_page_loading_wait()

        main_page.wait_for_order_feed_button()
        main_page.click_on_order_feed()
        main_page.main_page_loading_wait()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.order_feed_page_loading_wait()

        order_feed_page.click_on_order()
        order_feed_page.order_feed_page_loading_wait()
        order_feed_page.wait_for_order_details_window()
        order_details = order_feed_page.find_order_details_window()

        assert order_details.is_displayed()





    @allure.title('Test order number from history is shown in order feed')
    def test_order_from_history_shown_in_feed(self, driver, login_and_place_order_fixture):
        main_page = login_and_place_order_fixture
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.scroll_to_close_order_button()
        main_page.put_cursor_and_click_on_close_order_window()
        time.sleep(2)

        main_page.main_page_loading_wait()

        main_page.wait_for_personal_account_button()
        main_page.click_on_personal_account()
        time.sleep(2)

        main_page.main_page_loading_wait()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_overlay_to_disappear_personal()

        personal_account_page.click_on_order_history_button()
        personal_account_page.wait_overlay_to_disappear_personal()

        personal_account_page.wait_for_oder_history_list()
        personal_account_page.find_order_number_from_history()
        order_in_history = personal_account_page.get_order_number_from_order_feed_history()

        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        main_page.main_page_loading_wait()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.order_feed_page_loading_wait()

        order_in_feed = order_feed_page.get_order_number_from_order_feed_history()

        assert order_in_history == order_in_feed

    @allure.title('Test created order number appears in order feed work list')
    def test_order_number_appears_in_work_list(self, driver, registered_user_placed_order):
        order_number = registered_user_placed_order

        main_page = MainPage(driver)

        main_page.click_on_order_feed()
        main_page.main_page_loading_wait()
        time.sleep(1)

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.order_feed_page_loading_wait()

        order_number_in_work_list = order_feed_page.find_order_number_in_work_list()
        time.sleep(1)

        print(f'order number in list: {order_number_in_work_list}')
        assert f'0{order_number}' == order_number_in_work_list

    @allure.title('Test counter Orders done all time is increasing when new order has been created')
    def test_counter_orders_done_all_time_increasing_due_to_new_order(self, driver, get_all_time_count_before_and_place_order):
        counter_before = get_all_time_count_before_and_place_order[1]

        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.wait_for_order_feed_button()
        main_page.click_on_order_feed()
        main_page.main_page_loading_wait()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.order_feed_page_loading_wait()
        time.sleep(1)
        counter_after = order_feed_page.find_counter_in_orders_done_all_time()
        print(f"Orders after new order: {counter_after}")

        assert int(counter_before) < int(counter_after)

    @allure.title('Test counter Orders done today is increasing when new order has been created')
    def test_counter_orders_done_today_increasing_due_to_new_order(self, driver, get_today_count_before_and_place_order):
        counter_before = get_today_count_before_and_place_order[1]

        main_page = MainPage(driver)
        main_page.main_page_loading_wait()
        main_page.wait_for_order_feed_button()
        main_page.click_on_order_feed()
        main_page.main_page_loading_wait()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.order_feed_page_loading_wait()
        time.sleep(1)
        order_feed_page.scroll_to_orders_done_today()
        counter_after = order_feed_page.find_counter_in_orders_done_today()
        print(f"Orders after new order: {counter_after}")

        assert int(counter_before) < int(counter_after)












