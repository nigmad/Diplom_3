import allure
from selenium.common import NoSuchElementException
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage





class MainPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step('Кликнуть на Конструктор')
    def click_on_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть на Лента заказов')
    def click_on_order_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Кликнуть на Личный кабинет')
    def click_on_personal_account(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Кликнуть на Войти в аккаунт')
    def click_on_enter_account_button(self):
        self.click_on_element(MainPageLocators.ENTER_BUTTON)

    @allure.step('Подождать появления кнопки Личный кабинет')
    def wait_for_personal_account_button(self):
        self.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)


    @allure.step('Подождать появления кнопки Конструктор')
    def wait_for_constructor_button(self):
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Подождать появления кнопки Лента Заказов')
    def wait_for_order_feed_button(self):
        self.wait_for_element(MainPageLocators.ORDER_FEED_BUTTON)



    @allure.step('Скролл до ингредиента')
    def scroll_to_ingredient(self):
        self.scroll_to_element(MainPageLocators.BUN_INGREDIENT_1)

    @allure.step('Кликнуть на Лента заказов')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.BUN_INGREDIENT_1)

    @allure.step('Подождать всплывающего окна с информацией об ингредиенте')
    def wait_for_ingredient(self):
        self.wait_for_element(MainPageLocators.BUN_INGREDIENT_1)

    @allure.step('Подождать всплывающего окна с информацией об ингредиенте')
    def wait_for_ingredient_details_window(self):
        self.wait_for_element(MainPageLocators.INGREDIENT_DETAILS_WINDOW_HEADER)

    @allure.step('Подождать кнопку закрыть окна с информацией об ингредиенте')
    def wait_for_ingredient_details_window_x_button(self):
        self.wait_for_element(MainPageLocators.INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON)



    @allure.step('Кликнуть на кнопку Оформить заказ')
    def click_on_place_order_button(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)


    @allure.step('Перетащить булочку в заказ')
    def bun_drag_and_drop(self):
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT_1, MainPageLocators.BASKET)

    @allure.step('Перетащить соус в заказ')
    def sous_drag_and_drop(self):
        self.drag_and_drop_element(MainPageLocators.SOUS_INGREDIENT_1,
                           MainPageLocators.BASKET)

    @allure.step('Перетащить начинку в заказ')
    def filling_drag_and_drop(self):
        self.drag_and_drop_element(MainPageLocators.FILLING_INGREDIENT_1,
                           MainPageLocators.BASKET)

    @allure.step('Кликнуть на кнопку Заказать')
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)



    @allure.step('Найти заголовок Детали ингредиента на странице')
    def find_ingredient_details_header(self):
        try:
            return self.driver.find_element(*MainPageLocators.INGREDIENT_DETAILS_WINDOW_HEADER)
        except NoSuchElementException:

            raise AssertionError("Ingredient details header not found")



    @allure.step('Скролл до кнопки Оформить заказ')
    def scroll_to_close_button_on_ingredient_details_popup(self):
        self.scroll_to_element(MainPageLocators.INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON)

    @allure.step('Навести курсор на элемент и кликнуть')
    def put_cursor_and_click_on_close_on_ingredient_details_popup(self):
        self.put_cursor_and_click_on_element(MainPageLocators.INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON)



    @allure.step('Подождать, пока каунтер ингредиента обновится')
    def wait_for_counter_to_update(self, initial_counter, timeout=30):
        print(f"Initial counter: {initial_counter}")
        super().wait_for_element_to_update(MainPageLocators.INGREDIENT_COUNTER, initial_counter, timeout)


    @allure.step('Получить значение количества ингредиента')
    def get_counter_on_ingredient(self):
        counter_element = self.wait_for_element(MainPageLocators.INGREDIENT_COUNTER)
        counter_text = counter_element.text.strip()
        if counter_text.isdigit():
            return int(counter_text)
        else:
            raise AssertionError(f"Counter text is not a valid number: {counter_text}")

    @allure.step('Скролл до кнопки Оформить заказ')
    def scroll_to_place_order_button(self):
        self.scroll_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Подождать всплывающего окна об успешном заказе')
    def wait_for_placed_order_window(self):
        self.wait_for_element(MainPageLocators.YOUR_ORDER_IN_WORK_WINDOW)


    @allure.step('Найти номер заказа')
    def find_created_order_number(self):
        try:
            return self.driver.find_element(*MainPageLocators.YOUR_ORDER_NUMBER).text
        except NoSuchElementException:
            raise AssertionError("not found")


    @allure.step('Скролл до кнопки Оформить заказ')
    def scroll_to_close_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_CONFIRMATION_WINDOW_CLOSE_BUTTON)

    @allure.step('Навести курсор на элемент и кликнуть')
    def put_cursor_and_click_on_close_order_window(self):
        self.put_cursor_and_click_on_element(MainPageLocators.ORDER_CONFIRMATION_WINDOW_CLOSE_BUTTON)


    @allure.step('Навести курсор на элемент и кликнуть')
    def put_cursor_and_click_on_place_order_button(self):
        self.put_cursor_and_click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)






