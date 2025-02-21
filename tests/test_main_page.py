import time

import allure
from curl import Url
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage




class TestMainPage:
    @allure.title('Test click on Constructor button')
    def test_click_on_constructor_button_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_personal_account_button()
        main_page.click_on_personal_account()
        main_page.main_page_loading_wait()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.personal_page_loading_wait()

        main_page = MainPage(driver)
        main_page.wait_for_constructor_button()
        main_page.click_on_constructor()
        main_page.main_page_loading_wait()

        assert Url.MAIN_SITE_URL in main_page.get_current_url()




    @allure.title('Test click on Order feed button')
    def test_click_on_order_feed_button_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        main_page.main_page_loading_wait()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.order_feed_page_loading_wait()

        assert Url.ORDER_FEED_URL in order_feed_page.get_current_url()



    @allure.title('Test pop up window with ingredient details by clicking on ingredient')
    def test_click_ingredient_popup_window(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_ingredient()
        main_page.wait_for_ingredient()
        main_page.click_on_ingredient()

        main_page.main_page_loading_wait()
        main_page.wait_for_ingredient_details_window()

        ingredient_details_header = main_page.find_ingredient_details_header()
        assert ingredient_details_header.is_displayed()

    @allure.title('Test close pop up window clicking on close icon')
    def test_click_on_close_button_in_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_ingredient()
        main_page.wait_for_ingredient()
        main_page.click_on_ingredient()

        main_page.main_page_loading_wait()
        main_page.wait_for_ingredient_details_window_x_button()
        main_page.scroll_to_close_button_on_ingredient_details_popup()

        main_page.put_cursor_and_click_on_close_on_ingredient_details_popup()
        main_page.main_page_loading_wait()
        time.sleep(1)

        ingredient_details_window = main_page.find_ingredient_details_header()
        ingredient_details_window.is_displayed()
        assert ingredient_details_window.is_displayed()==False



    @allure.title('Test adding ingredient to order increase the counter')
    def test_adding_ingredient_to_order_increase_counter(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_ingredient()
        main_page.wait_for_ingredient()
        initial_counter = int(main_page.get_counter_on_ingredient())
        print(f"Initial counter: {initial_counter}")

        main_page.bun_drag_and_drop()
        main_page.main_page_loading_wait()

        main_page.wait_for_counter_to_update(initial_counter)
        main_page.main_page_loading_wait()
        time.sleep(2)

        updated_counter = int(main_page.get_counter_on_ingredient())
        print(f"updated_counter: {updated_counter}")
        assert initial_counter < updated_counter


    @allure.title('Test registered user can place an order')
    def test_place_order_by_registered_user(self, driver, login_fixture):
        main_page = login_fixture
        main_page = MainPage(driver)

        main_page.main_page_loading_wait()

        main_page.scroll_to_ingredient()
        main_page.wait_for_ingredient()

        main_page.get_counter_on_ingredient()
        main_page.bun_drag_and_drop()
        main_page.main_page_loading_wait()

        main_page.scroll_to_place_order_button()
        main_page.put_cursor_and_click_on_place_order_button()
        main_page.main_page_loading_wait()
        main_page.wait_for_placed_order_window()
        main_page.main_page_loading_wait()

        order_confirmation = main_page.find_created_order_number()
        print(f'order number: {order_confirmation}')

        assert order_confirmation != ""





























