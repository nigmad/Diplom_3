import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout=20):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout=30):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=20):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Переключиться на новое окно')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидать URL, содержащий подстроку')
    def wait_for_url_contains(self, substring, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(substring))

    @allure.step('Ожидать появления указанного числа окон')
    def wait_for_number_of_windows(self, number, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(number))

    @allure.step('Найти элемент')
    def find_element(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
            return self.driver.find_element(*locator)
        except TimeoutException:
            raise AssertionError(f"Элемент {locator} не найден или не кликабелен")

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, source_locator, target_locator):

        source_element = self.wait_for_element(source_locator)
        target_element = self.wait_for_element(target_locator)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    @allure.step('Подождать исчезновение оверлей')
    def wait_for_overlay_to_disappear(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until( EC.invisibility_of_element_located(locator))

    @allure.step('Подождать исчезновение всех оверлеев')
    def wait_for_all_overlays_to_disappear(self, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")))

    @allure.step('Клик элементу за оверлей')
    def click_on_overlaid_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        self.click_on_element(locator)

    @allure.step('Подождать исчезновение элемента')
    def wait_for_element_to_disappear(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Подождать, пока элемент обновится')
    def wait_for_element_to_update(self, locator, initial_value, timeout=30):

        WebDriverWait(self.driver, timeout).until(lambda driver: self.get_text_on_element(locator) != initial_value)

    @allure.step('Подождать исчезновение оверлей')
    def wait_for_element_not_visible(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))