import allure


from pages.create_order_page import CreateOrderPage





class TestOrderFeedPage:
    @allure.title('Test click on order opens Order details pop up window')
    def test_open_pop_up_order_details_by_clicking_on_order(self, driver, login_and_place_order_fixture):
        create_order_page = login_and_place_order_fixture
        create_order_page = CreateOrderPage(driver)
        create_order_page.wait_overlay_to_disappear_order()
        create_order_page.find_order_close_button()
        create_order_page.click_on_close_order_button()

