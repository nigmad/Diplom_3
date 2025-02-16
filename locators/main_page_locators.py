from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Лента Заказов']")
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a[@aria-current='page' and contains(@class, 'active')]//svg")
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")

    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")






