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
    def wait_for_page_loaded(self, timeout=10):
        return self.wait_for_element(OrderLocators.TOTAL_ORDERS_COUNT, timeout)
    
    @allure.step("Получить количество заказов за все время")
    def get_total_orders_count(self):
        count_text = self.get_text(OrderLocators.TOTAL_ORDERS_COUNT)
        return int(count_text)
    
    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        count_text = self.get_text(OrderLocators.TODAY_ORDERS_COUNT)
        return int(count_text)
    
    @allure.step("Проверить наличие раздела 'В работе'")
    def is_order_in_progress_section(self):
        return self.is_element_visible(OrderLocators.ORDERS_IN_PROGRESS_SECTION, timeout=3)
    
    @allure.step("Получить номера заказов в работе")
    def get_orders_in_progress_numbers(self):
        orders = self.find_elements(OrderLocators.ORDERS_IN_PROGRESS_ITEMS, timeout=2)
        order_numbers = []
        
        for order in orders:
            order_text = order.text.strip()
            order_number = self.extract_order_number(order_text)
            if order_number:
                order_numbers.append(order_number)
        
        return order_numbers
    
    @allure.step("Получить все заказы из ленты")
    def get_all_order_numbers(self):
        orders = self.find_elements(OrderLocators.ALL_ORDER_ITEMS, timeout=3)
        order_numbers = []
        
        for order in orders:
            order_text = order.text.strip()
            order_number = self.extract_order_number(order_text)
            if order_number:
                order_numbers.append(order_number)
        
        return order_numbers
    
    @allure.step("Проверить наличие заказа в ленте")
    def is_order_in_feed(self, order_number):
        order_numbers = self.get_all_order_numbers()
        return order_number in order_numbers
    
    @allure.step("Извлечь номер заказа из текста")
    def extract_order_number(self, text):
        patterns = [
            r'№\s*(\d+)',
            r'#\s*(\d+)',  
            r'заказ\s*(\d+)',
            r'order\s*(\d+)',
            r'(\d{4,})',
        ]
    
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                number = match.group(1).lstrip('0')
                return number if number else '0'
        
        return None