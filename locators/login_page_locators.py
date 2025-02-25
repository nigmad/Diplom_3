from selenium.webdriver.common.by import By

class LoginPageLocators:
    ENTER_HEADER = (By.XPATH, "//h2[text()='Вход']")

    EMAIL_FIELD = (By.XPATH,
             "//div[@class='input pr-6 pl-6 input_type_text input_size_default']//input[contains(@class, 'input__textfield')]")

    PASSWORD_FIELD = (By.NAME, "Пароль")

    LOGIN_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")




