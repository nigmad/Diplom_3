from selenium.webdriver.common.by import By



class CreateOrderLocators:
    BUNS_SECTION_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and text()='Булки']")
    BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]//span[text()='Булки']")

    SOUS_SECTION_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and text()='Соусы']")
    SOUS_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")]//span[text()="Соусы"]')

    FILLING_BUTTON = (By.XPATH, '//div[contains(@class, "tab_tab__1SPyG")]//span[text()="Начинки"]')
    FILLING_SECTION_TEXT = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and text()='Начинки']")

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary__1O7Bx') and text()='Оформить заказ']")

    DROP_N_DRAG_BUN_HERE_PLACE = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num__3nue1')]")

    BUN_INGREDIENT_1 = (By.XPATH, "//*[contains(@alt, 'Флюоресцентная булка R2-D3')]")
    SOUS_INGREDIENT_1 = (By.XPATH, "//*[contains(@alt, 'Соус Spicy-X')]")
    FILLING_INGREDIENT_1 = (By.XPATH, "//*[contains(@alt, 'Мясо бессмертных моллюсков Protostomia')]")

    INGREDIENT_DETAILS_WINDOW_HEADER = (By.XPATH, "//*[text()='Детали ингредиента']")
    INGREDIENT_DETAILS_WINDOW_CLOSE_BUTTON = (By.XPATH, "//*[contains(@fill-rule, 'evenodd')]")


    YOUR_ORDER_IN_WORK_WINDOW = (By.XPATH, "//*[text()='Ваш заказ начали готовить']")
    ORDER_CONFIRMATION_WINDOW_CLOSE_BUTTON = (By.XPATH, "//path[contains(@d, 'M3.29289 3.29289')]")
    YOUR_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow') and contains(@class, 'Modal_modal__title__2L34m')]")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")





