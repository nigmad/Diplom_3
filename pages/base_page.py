import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from seletools.actions import drag_and_drop
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать видимость элемента')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))

        return self.driver.find_element(*locator)


    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text




    @allure.step('Найти видимость элемента')
    def find_element(self, locator):
        try:

            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)
        except TimeoutException:
            return None

    @allure.step('Получить текущую ссылку')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Drop ingredient into basket')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Drop ingredient into basket')
    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()



    @allure.step('Навести курсор на элемент и кликнуть')
    def put_cursor_and_click_on_element(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()



    @allure.step('Клик элементу за оверлей')
    def click_on_overlaid_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.click_on_element(locator)

    @allure.step('Подождать исчезновение элемента')
    def wait_for_element_to_disappear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))


    @allure.step('Подождать исчезновение оверлей')
    def wait_for_element_not_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Подождать, пока значение элемента обновится')
    def wait_for_element_to_update(self, locator, initial_value, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda driver: int(self.get_text_on_element(locator)) != initial_value)