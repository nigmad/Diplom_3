import allure

from curl import Url

from pages.create_order_page import CreateOrderPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage




class TestMainPage:
    @allure.title('Test click on Constructor button')
    def test_click_on_constructor_button_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_personal_account_button()
        main_page.click_on_personal_account()
        main_page.wait_overlay_to_disappear_main()

        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.wait_overlay_to_disappear_personal()

        main_page = MainPage(driver)
        main_page.wait_for_constructor_button()
        main_page.click_on_constructor()
        main_page.wait_overlay_to_disappear_main()

        assert Url.MAIN_SITE_URL in main_page.get_current_url()




    @allure.title('Test click on Order feed button')
    def test_click_on_order_feed_button_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        main_page.wait_overlay_to_disappear_main()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_overlay_to_disappear_order_feed()

        assert Url.ORDER_FEED_URL in order_feed_page.get_current_url()



    @allure.title('Test pop up window with ingredient details by clicking on ingredient')
    def test_click_ingredient_popup_window(self, driver):
        create_order_page = CreateOrderPage(driver)
        create_order_page.scroll_to_ingredient()
        create_order_page.wait_for_ingredient()
        create_order_page.click_on_ingredient()

        create_order_page.wait_overlay_to_disappear_order()
        create_order_page.wait_for_ingredient_details_window()

        ingredient_details_header = create_order_page.find_ingredient_details_header()
        assert ingredient_details_header.is_displayed()

    @allure.title('Test close pop up window clicking on x icon')
    def test_click_on_x_icon_in_ingredient_details_window(self, driver):
        create_order_page = CreateOrderPage(driver)
        create_order_page.scroll_to_ingredient()
        create_order_page.wait_for_ingredient()
        create_order_page.click_on_ingredient()

        create_order_page.wait_overlay_to_disappear_order()

        create_order_page.wait_for_ingredient_details_window_x_button()
        create_order_page.find_x_button_on_ingredient_details_popup()

        create_order_page.click_x_icon_on_popup_ingredient_window()
        create_order_page.wait_overlay_to_disappear_order()

        create_order_page.wait_for_ingredient_popup_to_disappear()

        ingredient_details_header = create_order_page.find_ingredient_details_header()
        assert len(ingredient_details_header) == 0

    @allure.title('Test adding ingredient to order increase the counter')
    def test_click_ingredient_popup_window(self, driver):
        create_order_page = CreateOrderPage(driver)
        create_order_page.scroll_to_ingredient()
        create_order_page.wait_for_ingredient()
        initial_counter = int(create_order_page.get_counter_on_ingredient())

        create_order_page.bun_drag_and_drop()
        create_order_page.wait_overlay_to_disappear_order()
        create_order_page.wait_for_counter_to_update(initial_counter)

        updated_counter = int(create_order_page.get_counter_on_ingredient())

        assert updated_counter == initial_counter + 2

    @allure.title('Test registered user can place an order')
    def test_place_order_by_registered_user(self, driver, login_and_go_to_personal_account):
        personal_page = login_and_go_to_personal_account
        personal_page.click_on_constructor_from_personal_account()
        personal_page.wait_overlay_to_disappear_personal()

        create_order_page = CreateOrderPage(driver)
        create_order_page.wait_overlay_to_disappear_order()
        create_order_page.scroll_to_ingredient()
        create_order_page.wait_for_ingredient()

        create_order_page.get_counter_on_ingredient()
        create_order_page.bun_drag_and_drop()
        create_order_page.wait_overlay_to_disappear_order()

        create_order_page.scroll_to_place_order_button()
        create_order_page.click_on_place_order_button()
        create_order_page.wait_overlay_to_disappear_order()
        create_order_page.wait_for_placed_order_window()
        create_order_page.wait_overlay_to_disappear_order()

        order_confirmation = create_order_page.find_order_number()
        assert order_confirmation.is_displayed()





























