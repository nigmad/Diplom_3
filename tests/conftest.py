import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl import Url
from data import register_new_user
from helper import MethodsForApi
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage
from webdriver_manager.firefox import GeckoDriverManager

from pages.personal_account_page import PersonalAccountPage


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
    MethodsForApi().register_user(user_data)
    MethodsForApi().login_user(user_data)
    return user_data



@pytest.fixture(scope='function')
def login_fixture(driver, generate_registered_user):
    user_data = generate_registered_user
    MethodsForApi().register_user(user_data)
    MethodsForApi().login_user(user_data)

    main_page = MainPage(driver)
    main_page.click_on_personal_account()

    login_page = LoginPage(driver)
    login_page.fill_login_data_form(user_data)
    login_page.put_cursor_and_click_on_login_button()

    main_page = MainPage(driver)
    main_page.main_page_loading_wait()

    yield MainPage(driver)

    login_response = MethodsForApi().login_user(user_data)
    token = login_response.json().get("accessToken")
    MethodsForApi().delete_user(token)



@pytest.fixture
def open_password_recovery_page(driver):
    password_recovery_page = PasswordRecoveryPage(driver)
    driver.get(Url.PASSWORD_RECOVERY_URL)
    return password_recovery_page




@pytest.fixture
def registered_user_placed_order(driver, login_fixture):
    main_page = login_fixture
    main_page = MainPage(driver)
    main_page.scroll_to_ingredient()
    main_page.put_ingredient_into_basket()
    main_page.put_cursor_and_click_on_place_order_button()
    main_page.wait_for_placed_order_window()
    order_number = main_page.find_created_order_number()
    main_page.put_cursor_and_click_on_close_order_window()
    return order_number




@pytest.fixture
def get_all_time_count_orders_before_new_order(driver):
    main_page = MainPage(driver)
    main_page.click_on_order_feed()
    order_feed_page = OrderFeedPage(driver)
    counter_before = order_feed_page.find_counter_in_orders_done_all_time()
    return counter_before


@pytest.fixture
def get_today_count_of_orders_before_new_order(driver):
    main_page = MainPage(driver)
    main_page.click_on_order_feed()
    order_feed_page = OrderFeedPage(driver)
    counter_before = order_feed_page.find_counter_in_orders_done_today()
    return counter_before




@pytest.fixture(scope='function')
def login_logout_fixture(driver, login_fixture):
    main_page = login_fixture
    main_page = MainPage(driver)
    main_page.main_page_loading_wait()
    main_page.click_on_constructor()

    yield MainPage(driver)
    main_page.click_on_personal_account()
    personal_page = PersonalAccountPage(driver)
    personal_page.click_on_exit_button()
    login_page = LoginPage(driver)
    login_page.find_enter_header()