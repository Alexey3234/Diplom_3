import allure
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class TestMainFunctionality:
    
    @allure.title("Переход по клику на Конструктор")
    def test_constructor_navigation(self, main_page):
        main_page.click_constructor()        
        assert main_page.is_element_visible(main_page.locators.BUNS_SECTION), "Секция булок не отображается"

    @allure.title("Переход по клику на Лента заказов")
    def test_order_feed_navigation(self, main_page):
        main_page.wait_for_page_loaded()    
        main_page.click_order_feed()
        assert main_page.is_url_changed_to_feed(), "Переход на ленту заказов не выполнен"

    @allure.title("Видимость кнопки Конструктор")
    def test_constructor_button_visible(self, main_page):
        assert main_page.is_constructor_button_visible(), "Кнопка Конструктор не видима"

    @allure.title("Видимость кнопки Лента заказов")
    def test_order_feed_button_visible(self, main_page):
        assert main_page.is_order_feed_button_visible(), "Кнопка Лента заказов не видима"

    @allure.title("Кликабельность кнопки Конструктор")
    def test_constructor_button_clickable(self, main_page):
        assert main_page.is_constructor_button_clickable(), "Кнопка Конструктор не кликабельна"

    @allure.title("Кликабельность кнопки Лента заказов")
    def test_order_feed_button_clickable(self, main_page):
        assert main_page.is_order_feed_button_clickable(), "Кнопка Лента заказов не кликабельна"