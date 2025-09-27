import allure
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

class TestOrderFeedNavigation:
    """Тесты навигации в ленту заказов"""
    
    @allure.title("Переход в ленту заказов с главной страницы")
    def test_navigate_to_order_feed_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert main_page.is_url_contains("feed") or main_page.is_url_contains("order")


class TestOrderFeedCountersDisplay:
    
    @allure.title("Отображение счетчика 'Выполнено за всё время'")
    def test_total_orders_counter_displayed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.navigate()
        order_feed_page.wait_for_order_feed_loaded()
        assert order_feed_page.is_total_orders_visible()

    @allure.title("Отображение счетчика 'Выполнено за сегодня'")
    def test_today_orders_counter_displayed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.navigate()
        order_feed_page.wait_for_order_feed_loaded()
        assert order_feed_page.is_today_orders_visible()


class TestOrderFeedCountersValues:
    
    @allure.title("Валидное значение счетчика 'Выполнено за всё время'")
    def test_total_orders_counter_has_valid_value(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.navigate()
        order_feed_page.wait_for_order_feed_loaded()
        total_orders = order_feed_page.get_total_orders_count()
        assert total_orders >= 0

    @allure.title("Валидное значение счетчика 'Выполнено за сегодня'")
    def test_today_orders_counter_has_valid_value(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.navigate()
        order_feed_page.wait_for_order_feed_loaded()
        today_orders = order_feed_page.get_today_orders_count()
        assert today_orders >= 0


class TestOrderFeedElementsDisplay:
    
    @allure.title("Отображение списка заказов")
    def test_order_list_displayed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.navigate()
        order_feed_page.wait_for_order_feed_loaded()
        assert order_feed_page.is_order_list_visible()

    @allure.title("Отображение раздела 'В работе'")
    def test_orders_in_progress_section_displayed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.navigate()
        order_feed_page.wait_for_order_feed_loaded()
        assert order_feed_page.is_in_progress_section_visible()


class TestOrderFeedContent:
    
    @allure.title("Наличие текста связанного с заказами")
    def test_order_feed_contains_order_related_text(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.navigate()
        page_text = order_feed_page.get_page_source().lower()
        assert "заказ" in page_text or "order" in page_text

    @allure.title("Наличие осмысленного заголовка страницы")
    def test_order_feed_has_meaningful_title(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.navigate()
        page_title = order_feed_page.get_title()
        assert page_title and len(page_title.strip()) > 0

