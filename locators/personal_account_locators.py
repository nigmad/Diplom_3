from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    PROFILE_TEXT_BUTTON = (By.XPATH, "//a[text()='Профиль']")
    ORDERS_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    ORDER_HISTORY_WINDOW = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby")
    EXIT_BUTTON = (By.XPATH, "//button[contains(@class, 'text_type_main-medium') and text()='Выход']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Лента Заказов']")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")

    ORDER_HISTORY_ORDER_NUMBER = (By.XPATH, "//p[@class='text text_type_digits-default']")


