from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    ALL_ORDERS_DONE_HEADER =(By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='Выполнено за все время:']")
    ALL_ORDERS_DONE_COUNT = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ.text.text_type_digits-large")

    TODAY_ORDERS_DONE_HEADER = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='Выполнено за сегодня:']")
    TODAY_ORDERS_DONE_COUNT = (By.CSS_SELECTOR, "div.someContainer p.OrderFeed_number__2MbrQ.text.text_type_digits-large")

    ORDER_IN_WORK_HEADER = (By.XPATH, "//p[contains(@class, 'text') and contains(@class, 'text_type_main-medium') and text()='В работе:']")
    ORDER_IN_WORK_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default')]")


    ORDER_NUMBER_IN_LIST = (By.XPATH, "//p[@class='text text_type_digits-default']")
    ORDER_FEED_HISTORY = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__0Lh59')]")
    ORDER_DETAILS_WINDOW_COMPOUND_LIST = (By.CSS_SELECTOR, "ul.Modal_list__2sHWc li.Modal_listItem__3K1Kj")
    ORDER_DETAILS_CLOSE_BUTTON = (By.CSS_SELECTOR, 'svg[xmlns="http://www.w3.org/2000/svg"]')
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")













