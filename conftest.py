import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_page import OrderFeedPage
from data.urls import BASE_URL
from data.user_data import UserData


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура для инициализации драйвера с поддержкой разных браузеров"""
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    
    driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)
    
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def login(driver):
    """Фикстура для выполнения авторизации"""
    main_page = MainPage(driver)
    main_page.wait_for_page_loaded()
    
    # Выполняем авторизацию с данными из data модуля
    main_page.login(UserData.EMAIL, UserData.PASSWORD)
    
    return driver


@pytest.fixture(scope='function')
def main_page(driver):
    """Фикстура для инициализации главной страницы"""
    return MainPage(driver)


@pytest.fixture(scope='function')
def order_feed_page(driver):
    """Фикстура для инициализации страницы ленты заказов"""
    return OrderFeedPage(driver)


@pytest.fixture(scope='function')
def order_page(driver):
    """Фикстура для инициализации страницы заказа"""
    return OrderFeedPage(driver)


@pytest.fixture(scope='function')
def pages(driver, login):
    """Фикстура для инициализации всех page objects после авторизации"""
    return {
        'main_page': MainPage(driver),
        'order_feed_page': OrderFeedPage(driver),
        'order_page': OrderFeedPage(driver)
    }


@pytest.fixture(scope='function')
def pages_without_login(driver):
    """Фикстура для инициализации всех page objects без авторизации"""
    return {
        'main_page': MainPage(driver),
        'order_feed_page': OrderFeedPage(driver),
        'order_page': OrderFeedPage(driver)
    }