import pytest
from selenium import webdriver
from pages.main_page import MainPage

main_site = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    
    driver.set_window_size(1920, 1080)
    driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def login(driver):
    """Войти в аккаунт через главную страницу"""
    main_page = MainPage(driver)
    main_page.wait_for_page_loaded()

    # Выполняем авторизацию
    main_page.login("test1121@example.com", "Ye343fe")  # Используйте реальные данные

    # Убедимся, что авторизация прошла успешно - используем правильный локатор
    # Используем locators из MainPage, а не order_locators
    assert main_page.is_element_visible(main_page.locators.ORDER_BUTTON), "Авторизация не удалась"
    
    yield

@pytest.fixture(scope='function')
def pages(driver, login):
    """Инициализирует page objects после авторизации"""
    from pages.main_page import MainPage
    from pages.order_feed_page import OrderFeedPage
    from pages.order_page import OrderFeedPage
    
    return {
        'main_page': MainPage(driver),
        'order_feed_page': OrderFeedPage(driver),
        'order_page': OrderFeedPage(driver)
    }

@pytest.fixture(scope='function')
def order_feed_page(driver, login):
    """Инициализирует OrderFeedPage после авторизации"""
    from pages.order_feed_page import OrderFeedPage
    return OrderFeedPage(driver)

import pytest
from pages.main_page import MainPage

@pytest.fixture
def main_page(driver):
    return MainPage(driver)