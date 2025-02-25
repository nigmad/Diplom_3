import allure
from curl import Url
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage




class TestMainPage:
    @allure.title('Test click on Constructor button')
    def test_click_on_constructor_button_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.personal_page_loading_wait()
        main_page = MainPage(driver)
        main_page.click_on_constructor()

        assert Url.MAIN_SITE_URL in main_page.get_current_url()




    @allure.title('Test click on Order feed button')
    def test_click_on_order_feed_button_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.order_feed_page_loading_wait()

        assert Url.ORDER_FEED_URL in order_feed_page.get_current_url()



    @allure.title('Test pop up window with ingredient details by clicking on ingredient')
    def test_click_ingredient_popup_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_details_header = main_page.find_ingredient_details_window()
        assert ingredient_details_header.is_displayed()

    @allure.title('Test close pop up window by clicking on close icon')
    def test_click_on_close_button_in_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.close_ingredient_details_popup()
        result = main_page.ingredient_details_window_check()
        assert result ==False



    @allure.title('Test adding ingredient to order increase the counter')
    def test_adding_ingredient_to_order_increase_counter(self, driver):
        main_page = MainPage(driver)
        initial_counter = main_page.get_ingredient_count()

        main_page.put_ingredient_into_basket()
        main_page.main_page_loading_wait()
        updated_counter = main_page.get_ingredient_count()
        assert int(initial_counter) < int(updated_counter)


    @allure.title('Test registered user can place an order')
    def test_place_order_by_registered_user(self, driver, login_fixture):
        main_page = login_fixture
        main_page = MainPage(driver)

        main_page.scroll_to_ingredient()
        main_page.put_ingredient_into_basket()

        main_page.put_cursor_and_click_on_place_order_button()
        main_page.wait_for_placed_order_window()
        order_confirmation = main_page.find_created_order_number()

        assert order_confirmation != ""





























