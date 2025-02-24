import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage





class MainPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть на Конструктор')
    def click_on_constructor(self):
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.main_page_loading_wait()

    @allure.step('Кликнуть на Лента заказов')
    def click_on_order_feed(self):
        self.main_page_loading_wait()
        self.wait_for_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.put_cursor_and_click_on_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.main_page_loading_wait()

    @allure.step('Кликнуть на Личный кабинет')
    def click_on_personal_account(self):
        self.main_page_loading_wait()
        self.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.put_cursor_and_click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.main_page_loading_wait()

    @allure.step('Кликнуть на Войти в аккаунт')
    def click_on_enter_account_button(self):
        self.wait_for_element(MainPageLocators.ENTER_BUTTON)
        self.put_cursor_and_click_on_element(MainPageLocators.ENTER_BUTTON)
        self.main_page_loading_wait()



    @allure.step('Скролл до ингредиента')
    def scroll_to_ingredient(self):
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT_1)
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT_1)

    @allure.step('Кликнуть на Лента заказов')
    def click_on_ingredient(self):
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT_1)
        self.click_on_element(MainPageLocators.BUN_INGREDIENT_1)
        self.main_page_loading_wait()



    @allure.step('Перетащить соус в заказ')
    def sous_drag_and_drop(self):
        self.drag_and_drop(MainPageLocators.SOUS_INGREDIENT_1,
                           MainPageLocators.BASKET)

    @allure.step('Перетащить начинку в заказ')
    def put_ingredient_into_basket(self):
        self.main_page_loading_wait()
        ingredient = self.find_element(locator=MainPageLocators.BUN_INGREDIENT_1)
        basket = self.find_element(locator=MainPageLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)



    @allure.step('Найти окно Детали ингредиента на странице')
    def find_ingredient_details_window(self):
        self.wait_for_element(MainPageLocators.INGREDIENT_DETAILS_WINDOW_HEADER)
        element = self.find_element(MainPageLocators.INGREDIENT_DETAILS_WINDOW_HEADER)
        return element



    @allure.step('Проверка нахождения окна Детали ингредиента на странице')
    def ingredient_details_window_check(self):
        return self.try_to_find_element(MainPageLocators.INGREDIENT_DETAILS_WINDOW_HEADER)


    @allure.step('Навести курсор на кнопку закрыть и кликнуть')
    def close_ingredient_details_popup(self):
        self.put_cursor_and_click_on_element(MainPageLocators.INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON)
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_DETAILS_WINDOW_HEADER)






    @allure.step('взять значение счетчика')
    def get_ingredient_count(self):
        self.scroll_to_element(MainPageLocators.INGREDIENT_COUNTER)
        result = self.get_text_on_element(MainPageLocators.INGREDIENT_COUNTER)
        return result


    @allure.step('Подождать всплывающего окна об успешном заказе')
    def wait_for_placed_order_window(self):
        self.wait_for_element(MainPageLocators.YOUR_ORDER_IN_WORK_WINDOW)


    @allure.step('Найти номер заказа')
    def find_created_order_number(self):
        self.main_page_loading_wait()
        element = self.find_element(MainPageLocators.YOUR_ORDER_NUMBER).text
        return element



    @allure.step('Навести курсор на кнопку закрыть и кликнуть')
    def put_cursor_and_click_on_close_order_window(self):
        self.main_page_loading_wait()
        self.scroll_to_element(MainPageLocators.ORDER_CONFIRMATION_WINDOW_CLOSE_BUTTON)
        self.put_cursor_and_click_on_element(MainPageLocators.ORDER_CONFIRMATION_WINDOW_CLOSE_BUTTON)
        self.main_page_loading_wait()


    @allure.step('Навести курсор на кнопку Оформить заказ и кликнуть')
    def put_cursor_and_click_on_place_order_button(self):
        self.scroll_to_element(MainPageLocators.PLACE_ORDER_BUTTON)
        self.put_cursor_and_click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)
        self.main_page_loading_wait()

    @allure.step('Создать заказ')
    def place_order(self):
        self.click_on_constructor()
        self.scroll_to_ingredient()
        self.put_ingredient_into_basket()
        self.put_cursor_and_click_on_place_order_button()
        self.wait_for_placed_order_window()
        self.find_created_order_number()
        self.put_cursor_and_click_on_close_order_window()





