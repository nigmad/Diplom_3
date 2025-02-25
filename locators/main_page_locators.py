from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Лента Заказов']")

    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")

    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")



    BUNS_SECTION_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and text()='Булки']")
    BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']")

    SOUS_SECTION_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and text()='Соусы']")
    SOUS_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")]//span[text()="Соусы"]')

    FILLING_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")]//span[text()="Начинки"]')
    FILLING_SECTION_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and text()='Начинки']")

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary__1O7Bx') and text()='Оформить заказ']")

    BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    BUN_INGREDIENT_1 = (By.XPATH, "//*[contains(@alt, 'Флюоресцентная булка R2-D3')]")
    SOUS_INGREDIENT_1 = (By.XPATH, "//*[contains(@alt, 'Соус Spicy-X')]")
    FILLING_INGREDIENT_1 = (By.XPATH, "//*[contains(@alt, 'Мясо бессмертных моллюсков Protostomia')]")

    INGREDIENT_DETAILS_WINDOW_HEADER = (By.XPATH, "//*[text()='Детали ингредиента']")
    INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON = (By.XPATH, "//*[contains(@fill-rule, 'evenodd')]")


    YOUR_ORDER_IN_WORK_WINDOW = (By.XPATH, "//*[text()='Ваш заказ начали готовить']")
    ORDER_CONFIRMATION_WINDOW_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]")
    YOUR_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow') and contains(@class, 'Modal_modal__title__2L34m')]")









