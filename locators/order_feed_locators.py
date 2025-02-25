from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    ALL_ORDERS_DONE_HEADER =(By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='Выполнено за все время:']")
    ALL_ORDERS_DONE_COUNT = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ.text.text_type_digits-large")

    TODAY_ORDERS_DONE_HEADER = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='Выполнено за сегодня:']")
    TODAY_ORDERS_DONE_COUNT = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')

    ORDER_NUMBER_IN_DONE_LIST = (By.XPATH, "//ul[@class='OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")
    ORDER_IN_WORK_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default')]")
    ORDER_NUMBER_IN_WORK_WINDOW = (By.XPATH, "//li[@class='text text_type_digits-default mb-2']")

    ORDER_NUMBER_IN_LIST = (By.XPATH, "//p[@class='text text_type_digits-default']")

    ORDER_IN_WORK_HEADER = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='В работе:']")
    ORDER_FEED_HISTORY = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__0Lh59')]")
    ORDER_IN_FEED = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']")

    ORDER_DETAILS_WINDOW_COMPOUND_LIST = (By.CSS_SELECTOR, "ul.Modal_list__2sHWc li.Modal_listItem__3K1Kj")
    ORDER_DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[.//path[contains(@d, 'M3.29289 3.29289')]]")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")













