from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    PASSWORD_RECOVERY_BUTTON = (By.LINK_TEXT, "Восстановить пароль")
    PASSWORD_RECOVERY_HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")

    EMAIL_FIELD = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")

    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")

    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password'].text.input__textfield.text_type_main-default")
    ENTER_CODE_FROM_EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='text'].text.input__textfield.text_type_main-default")
    SAVE_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Сохранить']")

    HIDE_UNHIDE_PASSWORD_ICON = (By.XPATH, ".//div[contains(@class, 'input__icon input__icon-action')]")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")

    PASSWORD_FIELD_HIGHLIGHTED = (By.CSS_SELECTOR, "div.input.input_status_active")















