import allure
from selenium.common import NoSuchElementException

from locators.create_order_locators import CreateOrderLocators
from pages.base_page import BasePage




class CreateOrderPage(BasePage):

    @allure.step('Скролл до ингредиента')
    def scroll_to_ingredient(self):
        self.scroll_to_element(CreateOrderLocators.BUN_INGREDIENT_1)

    @allure.step('Кликнуть на Лента заказов')
    def click_on_ingredient(self):
        self.click_on_element(CreateOrderLocators.BUN_INGREDIENT_1)

    @allure.step('Подождать всплывающего окна с информацией об ингредиенте')
    def wait_for_ingredient(self):
        self.wait_for_element(CreateOrderLocators.BUN_INGREDIENT_1)

    @allure.step('Подождать всплывающего окна с информацией об ингредиенте')
    def wait_for_ingredient_details_window(self):
        self.wait_for_element(CreateOrderLocators.INGREDIENT_DETAILS_WINDOW_HEADER)

    @allure.step('Подождать кнопку закрыть окна с информацией об ингредиенте')
    def wait_for_ingredient_details_window_x_button(self):
        self.wait_for_element(CreateOrderLocators.INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON)

    @allure.step('Кликнуть на крестик всплывающего окна с информацией об ингредиенте')
    def click_x_icon_on_popup_ingredient_window(self):
        self.click_on_element(CreateOrderLocators.INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON)

    @allure.step('Кликнуть на кнопку Оформить заказ')
    def click_on_place_order_button(self):
        self.click_on_element(CreateOrderLocators.PLACE_ORDER_BUTTON)

    @allure.step('Получить значение количества ингредиента')
    def get_counter_on_ingredient(self):
        counter_element = self.wait_for_element(CreateOrderLocators.INGREDIENT_COUNTER)
        counter_text = counter_element.text.strip()
        if counter_text.isdigit():
            return int(counter_text)
        else:
            raise AssertionError(f"Counter text is not a valid number: {counter_text}")

    @allure.step('Перетащить булочку в заказ')
    def bun_drag_and_drop(self):
        self.drag_and_drop(CreateOrderLocators.BUN_INGREDIENT_1, CreateOrderLocators.DROP_N_DRAG_BUN_HERE_PLACE)

    @allure.step('Перетащить соус в заказ')
    def sous_drag_and_drop(self):
        self.drag_and_drop(CreateOrderLocators.SOUS_INGREDIENT_1,
                           CreateOrderLocators.DROP_N_DRAG_BUN_HERE_PLACE)

    @allure.step('Перетащить начинку в заказ')
    def filling_drag_and_drop(self):
        self.drag_and_drop(CreateOrderLocators.FILLING_INGREDIENT_1,
                           CreateOrderLocators.DROP_N_DRAG_BUN_HERE_PLACE)

    @allure.step('Кликнуть на кнопку Заказать')
    def click_on_order_button(self):
        self.click_on_element(CreateOrderLocators.PLACE_ORDER_BUTTON)

    @allure.step('Подождать исчезновение оверлэй')
    def wait_overlay_to_disappear_order(self):
        self.wait_for_overlay_to_disappear(CreateOrderLocators.OVERLAY)

    @allure.step('Найти заголовок Детали ингредиента на странице')
    def find_ingredient_details_header(self):
        try:
            return self.driver.find_element(*CreateOrderLocators.INGREDIENT_DETAILS_WINDOW_HEADER)
        except NoSuchElementException:

            raise AssertionError("Ingredient details header not found")

    @allure.step('Найти кнопку закрыть в окне Детали ингредиента')
    def find_x_button_on_ingredient_details_popup(self):
        try:
            return self.driver.find_element(*CreateOrderLocators.INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON)
        except NoSuchElementException:

            raise AssertionError("Close button in details window not found")

    @allure.step('Подождать, пока окно Детали ингредиента закроется')
    def wait_for_ingredient_popup_to_disappear(self):
        self.wait_for_element_to_disappear(*CreateOrderLocators.INGREDIENT_DETAILS_WINDOW_HEADER)
        self.wait_for_element_to_disappear(*CreateOrderLocators.OVERLAY)

    @allure.step('Подождать, пока каунтер ингредиента обновится')
    def wait_for_counter_to_update(self, initial_counter, timeout=10):
        self.wait_for_element_to_update(CreateOrderLocators.INGREDIENT_COUNTER, str(initial_counter), timeout)

    @allure.step('Скролл до кнопки Оформить заказ')
    def scroll_to_place_order_button(self):
        self.scroll_to_element(CreateOrderLocators.PLACE_ORDER_BUTTON)

    @allure.step('Подождать всплывающего окна об успешном заказе')
    def wait_for_placed_order_window(self):
        self.wait_for_element(CreateOrderLocators.YOUR_ORDER_IN_WORK_WINDOW)

    @allure.step('Найти номер заказа в всплывающем окне об успешном заказе')
    def find_order_number(self):
        return self.find_element(CreateOrderLocators.YOUR_ORDER_NUMBER)

    @allure.step('Кликнуть на кнопку Закрыть окно подтверждения заказа')
    def click_on_close_order_button(self):
        self.click_on_element(CreateOrderLocators.ORDER_CONFIRMATION_WINDOW_CLOSE_BUTTON)

    @allure.step('Найти номер заказа в всплывающем окне об успешном заказе')
    def find_order_close_button(self):
        return self.find_element(CreateOrderLocators.ORDER_CONFIRMATION_WINDOW_CLOSE_BUTTON)
