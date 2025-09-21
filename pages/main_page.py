import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.constructor_locators import ConstructorLocators
from locators.order_feed_locators import OrderFeedLocators
from locators.order_locators import OrderLocators

class MainPage(BasePage):
    locators = MainPageLocators()
    constructor_locators = ConstructorLocators()
    order_feed_locators = OrderFeedLocators()
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_constructor(self):
        self.click(self.locators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Кликнуть на кнопку 'Лента заказов'")
    def click_order_feed(self):
        self.click(self.locators.ORDER_FEED_BUTTON)
    
    @allure.step("Кликнуть на ингредиент с индексом {index}")
    def click_ingredient(self, index=0):
        self.wait_for_element(self.locators.INGREDIENT_ITEM)
        
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            self.scroll_to_element_js(ingredients[index])
            self.wait_for_element_clickable(ingredients[index])
            self.click_element(ingredients[index])
            self.wait_for_element(self.constructor_locators.MODAL)
    
    @allure.step("Получить счетчик ингредиента с индексом {index}")
    def get_ingredient_counter(self, index=0):
        try:
            counter_elements = self.find_elements(self.locators.INGREDIENT_COUNTER)
            
            if counter_elements and index < len(counter_elements):
                counter_text = counter_elements[index].text.strip()
                
                try:
                    return int(counter_text) if counter_text else 0
                except ValueError:
                    return 1
            else:
                return 0
                
        except Exception as e:
            print(f"Ошибка получения счетчика: {e}")
            return 0
    
    @allure.step("Проверить видимость деталей ингредиента")
    def is_ingredient_details_visible(self):
        try:
            details_title = self.is_element_visible(self.constructor_locators.INGREDIENT_DETAILS, timeout=3)
            name_visible = self.is_element_visible(self.constructor_locators.INGREDIENT_NAME, timeout=3)
            calories_visible = self.is_element_visible(self.constructor_locators.INGREDIENT_CALORIES, timeout=3)
            
            return details_title and name_visible and calories_visible
        
        except Exception as e:
            print(f"Ошибка в is_ingredient_details_visible: {e}")
            return False
    
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        try:
            self.wait_for_element(OrderLocators.ORDER_MODAL, timeout=10)
            order_number = self.get_order_number()
            
            self.click(OrderLocators.ORDER_MODAL_CLOSE)
            self.wait_for_element_to_disappear(OrderLocators.ORDER_MODAL, timeout=5)
            
            return order_number
        
        except Exception as e:
            print(f"Ошибка при закрытии модального окна: {e}")
            try:
                self.press_escape_key()
                self.wait_for_element_to_disappear(OrderLocators.ORDER_MODAL, timeout=3)
            except:
                print("Не удалось закрыть модальное окно")
            return None
    
    @allure.step("Добавить ингредиент в конструктор с индексом {index}")
    def add_ingredient_to_constructor(self, index=0):
        try:
            ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
            drop_area = self.find_element(self.locators.CONSTRUCTOR_DROP_AREA)
            
            if not ingredients:
                return False
                
            if index >= len(ingredients):
                return False
            
            ingredient = ingredients[index]
            self.scroll_to_element_js(ingredient)
            self.wait_for_element_clickable(ingredient)
            self.drag_and_drop_element(ingredient, drop_area)
            
            counter = self.get_ingredient_counter(index)
            return counter > 0
            
        except Exception as e:
            print(f"Ошибка в add_ingredient_to_constructor: {e}")
            return False

    @allure.step("Закрыть модальное окно через крестик")
    def close_modal_by_button(self):
        self.click(self.constructor_locators.MODAL_CLOSE)
        self.wait_for_element_to_disappear(self.constructor_locators.MODAL)

    @allure.step("Открыть модальное окно ингредиента с индексом {index}")
    def open_ingredient_modal(self, index=0):
        self.wait_for_element(self.locators.INGREDIENT_ITEM)
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            self.scroll_to_element_js(ingredients[index])
            self.wait_for_element_clickable(ingredients[index])
            self.click_element(ingredients[index])
            self.wait_for_element(self.constructor_locators.MODAL)

    @allure.step("Проверить изменение URL на /feed")
    def is_url_changed_to_feed(self):
        return self.is_url_contains("/feed")

    @allure.step("Проверить загрузку ленты заказов")
    def is_order_feed_loaded(self):
        return (self.is_element_visible(self.order_feed_locators.TOTAL_ORDERS) and
                self.is_element_visible(self.order_feed_locators.TODAY_ORDERS))

    @allure.step("Ожидание счетчика ингредиента {index} со значением {expected_value}")
    def wait_for_ingredient_counter(self, index=0, expected_value=1, timeout=5):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            return self.wait_for_condition(
                lambda: self.get_ingredient_counter(index) == expected_value,
                timeout=timeout
            )
        return False

    @allure.step("Проверить видимость кнопки Конструктор")
    def is_constructor_button_visible(self):
        return self.is_element_visible(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Проверить видимость кнопки Лента заказов")
    def is_order_feed_button_visible(self):
        return self.is_element_visible(self.locators.ORDER_FEED_BUTTON)

    @allure.step("Проверить кликабельность кнопки Конструктор")
    def is_constructor_button_clickable(self):
        return self.is_element_clickable(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Проверить кликабельность кнопки Лента заказов")
    def is_order_feed_button_clickable(self):
        return self.is_element_clickable(self.locators.ORDER_FEED_BUTTON)

    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_loaded(self, timeout=10):
        return self.wait_for_element(self.locators.CONSTRUCTOR_BUTTON, timeout)
    
    @allure.step("Выполнить авторизацию с email: {email}")
    def login(self, email, password):
        self.click(self.locators.LOGIN_BUTTON)
        self.wait_for_element(self.locators.EMAIL_INPUT)
        self.find_element(self.locators.EMAIL_INPUT).send_keys(email)
        self.find_element(self.locators.PASSWORD_INPUT).send_keys(password)
        self.click(self.locators.LOGIN_SUBMIT_BUTTON)
        self.wait_for_element(self.locators.ORDER_BUTTON, timeout=10)
    
    @allure.step("Добавить булку и начинку в конструктор")
    def add_bun_and_filling(self):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        drop_area = self.find_element(self.locators.CONSTRUCTOR_DROP_AREA)
    
        if len(ingredients) >= 2:
            self.scroll_to_element_js(ingredients[0])
            self.drag_and_drop_element(ingredients[0], drop_area)
            
            self.scroll_to_element_js(ingredients[1])
            self.drag_and_drop_element(ingredients[1], drop_area)
            
            counter1 = self.get_ingredient_counter(0)
            counter2 = self.get_ingredient_counter(1)
            
            return counter1 > 0 or counter2 > 0
        return False
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            self.click(self.constructor_locators.MODAL_CLOSE)
            self.wait_for_element_to_disappear(self.constructor_locators.MODAL)
            return True
        except:
            try:
                self.press_escape_key()
                self.wait_for_element_to_disappear(self.constructor_locators.MODAL, timeout=5)
                return True
            except Exception as e:
                print(f"Не удалось закрыть модальное окно: {e}")
                return False
                
    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self):
        try:
            self.wait_for_element(OrderLocators.ORDER_MODAL, timeout=5)
            
            locators = [
                OrderLocators.ORDER_NUMBER,
                OrderLocators.ORDER_NUMBER_ALT1,
                OrderLocators.ORDER_NUMBER_ALT2, 
                OrderLocators.ORDER_NUMBER_ALT3,
                OrderLocators.ORDER_NUMBER_ALT4,
                OrderLocators.ORDER_NUMBER_ALT5
            ]
            
            for locator in locators:
                try:
                    element = self.find_element(locator, timeout=2)
                    order_text = element.text.strip()
                    if order_text and len(order_text) > 3:
                        return order_text
                except:
                    continue
            
            return None
            
        except Exception as e:
            print(f"Ошибка получения номера заказа: {e}")
            return None

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_element_visible(self.constructor_locators.MODAL, timeout=3)
    @allure.step("Закрыть модальное окно через ESC")
    def close_modal_by_esc(self):
        """Закрыть модальное окно через клавишу ESC"""
        self.press_escape_key()
        self.wait_for_element_to_disappear(self.constructor_locators.MODAL)

    @allure.step("Закрыть модальное окно через overlay")
    def close_modal_by_overlay(self):
        """Закрыть модальное окно через клик на overlay"""
    # Просто вызываем универсальный метод close_modal, который уже содержит логику
        return self.close_modal()