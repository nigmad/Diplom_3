import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl import Url
from data import DataForUser, MethodsForApi, register_new_user
from pages.create_order_page import CreateOrderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage


# Параметризация для двух браузеров (Chrome и Firefox)
@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        # Настройки для Chrome
        options = Options()
        options.add_argument("--window-size=1200,600")
        service = Service("/Users/diananigma/Downloads/WebDriver/bin/chromedriver")
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(Url.MAIN_SITE_URL)
    elif request.param == "firefox":
        # Настройки для Firefox
        options = FirefoxOptions()
        options.add_argument("--window-size=1200,600")
        driver = webdriver.Firefox(options=options)
        driver.get(Url.MAIN_SITE_URL)

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
def login_fixture(generate_registered_user):
    user_data = generate_registered_user
    response = MethodsForApi().register_user(user_data)
    assert response.status_code == 200
    assert response.json().get("success") is True

    login_response = MethodsForApi().login_user(user_data)
    assert login_response.status_code == 200
    assert login_response.json().get("success") is True
    return user_data



@pytest.fixture
def login_and_go_to_personal_account(driver, generate_registered_user):
    user_data = generate_registered_user

    response = MethodsForApi().register_user(user_data)
    assert response.status_code == 200
    assert response.json().get("success") is True

    login_response = MethodsForApi().login_user(user_data)
    assert login_response.status_code == 200
    assert login_response.json().get("success") is True

    main_page = MainPage(driver)
    main_page.click_on_personal_account()
    login_page = LoginPage(driver)
    login_page.fill_login_data_form(user_data)
    login_page.click_on_login_button()
    login_page.wait_overlay_to_disappear_login()

    main_page.wait_overlay_to_disappear_main()
    main_page.wait_for_personal_account_button()
    main_page.click_on_personal_account()
    personal_page = PersonalAccountPage(driver)
    personal_page.wait_overlay_to_disappear_personal()

    return personal_page





@pytest.fixture
def open_password_recovery_page(driver):
    password_recovery_page = PasswordRecoveryPage(driver)
    driver.get(Url.PASSWORD_RECOVERY_URL)
    return password_recovery_page



@pytest.fixture
def login_and_place_order_fixture(driver, login_and_go_to_personal_account):
    personal_page = login_and_go_to_personal_account
    personal_page.click_on_constructor_from_personal_account()
    personal_page.wait_overlay_to_disappear_personal()

    create_order_page = CreateOrderPage(driver)
    create_order_page.wait_overlay_to_disappear_order()
    create_order_page.scroll_to_ingredient()
    create_order_page.wait_for_ingredient()

    create_order_page.get_counter_on_ingredient()
    create_order_page.bun_drag_and_drop()
    create_order_page.wait_overlay_to_disappear_order()

    create_order_page.scroll_to_place_order_button()
    create_order_page.click_on_place_order_button()
    create_order_page.wait_overlay_to_disappear_order()
    create_order_page.wait_for_placed_order_window()
    create_order_page.wait_overlay_to_disappear_order()

    order_confirmation = create_order_page.find_order_number()
    return order_confirmation


