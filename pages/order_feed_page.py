import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
import re

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()
    
    @allure.step("Перейти на страницу ленты заказов")
    def navigate(self):
        from pages.main_page import MainPage
        MainPage(self.driver).click_order_feed()
        return self
    
    @allure.step("Ожидать загрузки ленты заказов")
    def wait_for_order_feed_loaded(self, timeout=10):
        return any(
            self.is_element_visible(locator, timeout)
            for locator in [
                self.locators.ORDER_LIST,
                self.locators.TOTAL_ORDERS, 
                self.locators.TODAY_ORDERS
            ]
        )
    
    @allure.step("Проверить видимость счетчика 'Выполнено за все время'")
    def is_total_orders_visible(self):
        return self.is_element_visible(self.locators.TOTAL_ORDERS)
    
    @allure.step("Проверить видимость счетчика 'Выполнено за сегодня'")
    def is_today_orders_visible(self):
        return self.is_element_visible(self.locators.TODAY_ORDERS)
    
    def _extract_number_from_text(self, text):
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else int(text) if text.isdigit() else 0
    
    @allure.step("Получить значение счетчика 'Выполнено за все время'")
    def get_total_orders_count(self):
        text = self.get_text(self.locators.TOTAL_ORDERS)
        return self._extract_number_from_text(text)
    
    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        text = self.get_text(self.locators.TODAY_ORDERS)
        return self._extract_number_from_text(text)
    
    @allure.step("Проверить видимость списка заказов")
    def is_order_list_visible(self):
        return self.is_element_visible(self.locators.ORDER_LIST)
    
    @allure.step("Проверить видимость раздела 'В работе'")
    def is_in_progress_section_visible(self):
        return self.is_element_visible(self.locators.ORDERS_IN_PROGRESS_SECTION)
    
    @allure.step("Проверить наличие заказов в ленте")
    def has_any_orders(self):
        return len(self.find_elements(self.locators.ORDER_ITEMS)) > 0
    
    @allure.step("Проверить наличие заказов в работе")
    def has_orders_in_progress(self):
        return len(self.find_elements(self.locators.ORDERS_IN_PROGRESS_ITEMS)) > 0
    
    @allure.step("Получить исходный код страницы")
    def get_page_source(self):
        return self.driver.page_source

    @allure.step("Получить заголовок страницы")
    def get_title(self):
        return self.driver.title
    
