import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl import Url
from data import MethodsForApi, register_new_user
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture(scope="session", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        # Настройки для Chrome
        options = Options()
        service = Service("/Users/diananigma/Downloads/WebDriver/bin/chromedriver")
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Url.MAIN_SITE_URL)
    elif request.param == "firefox":
        # Настройки для Firefox
        options = FirefoxOptions()
        service = Service("/Users/diananigma/Downloads/WebDriver/bin/geckodriver")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        driver.set_window_size(1920, 1080)
        driver.get(Url.MAIN_SITE_URL)
        profile = webdriver.FirefoxProfile()
        profile.set_preference("dom.drop.enabled", True)
        profile.set_preference("dom.dragging.enabled", True)
        options.headless = False

    yield driver
    driver.quit()



@pytest.fixture
def generate_registered_user():
    user_data = register_new_user()
    return {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"]
    }




@pytest.fixture
def generate_user_fixture(driver, generate_registered_user):
    user_data = generate_registered_user
    response = MethodsForApi().register_user(user_data)
    assert response.status_code == 200
    assert response.json().get("success") is True

    login_response = MethodsForApi().login_user(user_data)
    assert login_response.status_code == 200
    assert login_response.json().get("success") is True
    return user_data



@pytest.fixture
def login_fixture(driver, generate_registered_user):
    user_data = generate_registered_user
    response = MethodsForApi().register_user(user_data)
    assert response.status_code == 200
    assert response.json().get("success") is True

    login_response = MethodsForApi().login_user(user_data)
    assert login_response.status_code == 200
    assert login_response.json().get("success") is True

    main_page = MainPage(driver)
    main_page.click_on_personal_account()
    main_page.main_page_loading_wait()
    login_page = LoginPage(driver)
    login_page.login_page_loading_wait()
    login_page.fill_login_data_form(user_data)
    login_page.put_cursor_and_click_on_login_button()
    login_page.login_page_loading_wait()

    main_page = MainPage(driver)
    main_page.main_page_loading_wait()
    main_page.wait_for_personal_account_button()
    main_page.click_on_constructor()

    yield MainPage(driver)

    login_response = MethodsForApi().login_user(user_data)
    token = login_response.json().get("accessToken")
    print(f"Generated Token: {token}")
    delete_response = MethodsForApi().delete_user(token)
    assert delete_response.status_code == 202


@pytest.fixture
def open_password_recovery_page(driver):
    password_recovery_page = PasswordRecoveryPage(driver)
    driver.get(Url.PASSWORD_RECOVERY_URL)
    return password_recovery_page


@pytest.fixture
def login_and_place_order_fixture(driver, login_fixture):
    main_page = login_fixture

    main_page = MainPage(driver)
    main_page.main_page_loading_wait()
    main_page.scroll_to_ingredient()
    main_page.wait_for_ingredient()

    main_page.get_counter_on_ingredient()
    main_page.bun_drag_and_drop()
    main_page.main_page_loading_wait()
    time.sleep(1)
    main_page.scroll_to_place_order_button()
    main_page.click_on_place_order_button()
    time.sleep(2)
    main_page.main_page_loading_wait()
    main_page.wait_for_placed_order_window()
    main_page.main_page_loading_wait()

    order_number = main_page.find_created_order_number()
    print(f'order number: {order_number}')

    return order_number


@pytest.fixture
def registered_user_placed_order(driver, login_and_place_order_fixture):
    order_number = login_and_place_order_fixture
    main_page = MainPage(driver)
    main_page.main_page_loading_wait()
    main_page.scroll_to_close_order_button()
    main_page.put_cursor_and_click_on_close_order_window()
    time.sleep(2)

    main_page.main_page_loading_wait()
    print(f'order number: {order_number}')

    return order_number

@pytest.fixture
def get_amount_of_orders_before_new_order(driver):
    main_page = MainPage(driver)
    main_page.click_on_order_feed()
    main_page.main_page_loading_wait()

    order_feed_page = OrderFeedPage(driver)
    order_feed_page.order_feed_page_loading_wait()
    order_feed_page.wait_for_order_details_window()
    counter_before = order_feed_page.find_counter_in_orders_done_all_time()

    return counter_before

@pytest.fixture
def get_all_time_count_before_and_place_order(driver, get_amount_of_orders_before_new_order, login_and_place_order_fixture):
    counter_before = get_amount_of_orders_before_new_order
    print(f"Orders before new order: {counter_before}")

    order_number = login_and_place_order_fixture
    main_page = MainPage(driver)
    main_page.main_page_loading_wait()
    main_page.scroll_to_close_order_button()
    main_page.put_cursor_and_click_on_close_order_window()
    time.sleep(2)

    main_page.main_page_loading_wait()
    print(f'order number: {order_number}')

    return order_number, counter_before





@pytest.fixture
def get_today_amount_of_orders_before_new_order(driver):
    main_page = MainPage(driver)
    main_page.click_on_order_feed()
    main_page.main_page_loading_wait()

    order_feed_page = OrderFeedPage(driver)
    order_feed_page.order_feed_page_loading_wait()
    order_feed_page.wait_for_order_details_window()
    order_feed_page.scroll_to_orders_done_today()
    counter_before = order_feed_page.find_counter_in_orders_done_today()

    return counter_before



@pytest.fixture
def get_today_count_before_and_place_order(driver, get_today_amount_of_orders_before_new_order, login_and_place_order_fixture):
    counter_before = get_today_amount_of_orders_before_new_order
    print(f"Orders today before new order: {counter_before}")

    order_number = login_and_place_order_fixture
    main_page = MainPage(driver)
    main_page.main_page_loading_wait()
    main_page.scroll_to_close_order_button()
    main_page.put_cursor_and_click_on_close_order_window()
    time.sleep(2)

    main_page.main_page_loading_wait()
    print(f'order number: {order_number}')

    return order_number, counter_before
