import allure
import re
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pages.base_page import BasePage
from locators.order_locators import OrderLocators

class OrderFeedPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Ожидание загрузки страницы ленты заказов")
    def wait_for_page_loaded(self):
        return self.wait_for_element(OrderLocators.ORDER_FEED_SECTION)
    
    @allure.step("Получить количество заказов за все время")
    def get_total_orders_count(self):
        count_text = self.get_text(OrderLocators.TOTAL_ORDERS_COUNT)
        return int(count_text)
    
    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        count_text = self.get_text(OrderLocators.TODAY_ORDERS_COUNT)
        return int(count_text)
    
    @allure.step("Получить номера заказов в работе")
    def get_orders_in_progress_numbers(self):
        orders = self.find_elements(OrderLocators.ORDERS_IN_PROGRESS_ITEMS)
        order_numbers = []
        
        for order in orders:
            order_text = order.text.strip()
            order_number = self.extract_order_number(order_text)
            if order_number:
                order_numbers.append(order_number)
        
        return order_numbers
    
    @allure.step("Кликнуть на заказ в ленте")
    def click_order(self, index=0):
        orders = self.find_elements(OrderLocators.ORDERS_IN_PROGRESS_ITEMS)
        if orders and index < len(orders):
            self.click_element(orders[index])
    
    @allure.step("Проверить отображение деталей заказа")
    def is_order_details_visible(self):
        return self.is_element_visible(OrderLocators.ORDER_MODAL)
    
    @allure.step("Извлечь номер заказа из текста")
    def extract_order_number(self, text):
        """Извлечь номер заказа из текста"""
        patterns = [
            r'№\s*(\d+)',      # № 12345
            r'#\s*(\d+)',       # # 12345  
            r'заказ\s*(\d+)',   # заказ 12345
            r'order\s*(\d+)',   # order 12345
            r'(\d{5,})',        # последовательность из 5+ цифр
        ]
    
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                number = match.group(1).lstrip('0')
                return number if number else '0'
        
        return None