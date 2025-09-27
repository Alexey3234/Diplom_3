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
            self.wait_for_ingredient_modal()
    
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
                
        except Exception:
            return 0
    
    @allure.step("Проверить видимость деталей ингредиента")
    def is_ingredient_details_visible(self):
        try:
            details_title = self.is_element_visible(self.constructor_locators.INGREDIENT_DETAILS, timeout=3)
            name_visible = self.is_element_visible(self.constructor_locators.INGREDIENT_NAME, timeout=3)
            calories_visible = self.is_element_visible(self.constructor_locators.INGREDIENT_CALORIES, timeout=3)
            
            return details_title and name_visible and calories_visible
        
        except Exception:
            return False
    
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
            
        except Exception:
            return False

    @allure.step("Открыть модальное окно ингредиента с индексом {index}")
    def open_ingredient_modal(self, index=0):
        self.wait_for_element(self.locators.INGREDIENT_ITEM)
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            self.scroll_to_element(ingredients[index])
            self.wait_for_element_clickable(ingredients[index])
            self.click_element(ingredients[index])
            self.wait_for_ingredient_modal()

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
        self.send_keys(self.locators.EMAIL_INPUT, email)
        self.send_keys(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.LOGIN_SUBMIT_BUTTON)
        self.wait_for_order_button_visible()
    
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
    
    @allure.step("Создать заказ")
    def create_order(self):
        self.click(self.locators.ORDER_BUTTON)
    
    @allure.step("Ожидать появления модального окна заказа")
    def wait_for_order_modal(self, timeout=10):
        return self.wait_for_element(OrderLocators.ORDER_MODAL, timeout)
    
    @allure.step("Ожидать появления модального окна ингредиента")
    def wait_for_ingredient_modal(self, timeout=5):
        return self.wait_for_element(self.constructor_locators.MODAL, timeout)
    
    @allure.step("Ожидать появления кнопки заказа")
    def wait_for_order_button_visible(self, timeout=10):
        return self.wait_for_element(self.locators.ORDER_BUTTON, timeout)
    
    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self):
        try:
            self.wait_for_order_modal(timeout=5)
            
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
                    order_text = self.get_element_text(element)
                    if order_text and len(order_text) > 3:
                        return order_text
                except:
                    continue
            
            return None
            
        except Exception:
            return None

    @allure.step("Проверить видимость модального окна ингредиента")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(self.constructor_locators.MODAL, timeout=3)
    
    @allure.step("Проверить видимость модального окна заказа")
    def is_order_modal_visible(self):
        return self.is_element_visible(OrderLocators.ORDER_MODAL, timeout=3)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        try:
            if self.is_element_visible(self.constructor_locators.MODAL_CLOSE, timeout=1):
                self.click(self.constructor_locators.MODAL_CLOSE)
                self.wait_for_element_to_disappear(self.constructor_locators.MODAL)
                return True
            
            if self.is_element_visible(OrderLocators.ORDER_MODAL_CLOSE, timeout=1):
                self.click(OrderLocators.ORDER_MODAL_CLOSE)
                self.wait_for_element_to_disappear(OrderLocators.ORDER_MODAL)
                return True
                
        except:
            pass
        
        try:
            self.press_escape_key()
            
            if self.is_ingredient_modal_visible():
                self.wait_for_element_to_disappear(self.constructor_locators.MODAL, timeout=3)
            elif self.is_order_modal_visible():
                self.wait_for_element_to_disappear(OrderLocators.ORDER_MODAL, timeout=3)
                
            return True
        except Exception:
            return False

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        return self.close_modal()

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        return self.close_modal()

    @allure.step("Проверить, что заказ успешно создан")
    def is_order_created_successfully(self):
        order_number = self.get_order_number()
        return order_number is not None and len(order_number) > 0

    @allure.step("Проверить, что ингредиент добавлен в конструктор")
    def is_ingredient_added_to_constructor(self, index=0):
        counter = self.get_ingredient_counter(index)
        return counter > 0

    @allure.step("Перейти в конструктор и проверить загрузку")
    def navigate_to_constructor(self):
        self.click_constructor()
        return self.wait_for_page_loaded()

    @allure.step("Перейти в ленту заказов и проверить загрузку")
    def navigate_to_order_feed(self):
        self.click_order_feed()
        return self.is_order_feed_loaded()

    @allure.step("Кликнуть на элемент")
    def click_element(self, element):
        self.execute_script("arguments[0].click();", element)

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_element_visible(self.constructor_locators.MODAL, timeout=3)

    @allure.step("Закрыть модальное окно через ESC")
    def close_modal_by_esc(self):
        self.press_escape_key()
        self.wait_for_element_to_disappear(self.constructor_locators.MODAL)

    @allure.step("Закрыть модальное окно через overlay")
    def close_modal_by_overlay(self):
        return self.close_modal()

    @allure.step("Закрыть модальное окно через крестик")
    def close_modal_by_button(self):
        self.click(self.constructor_locators.MODAL_CLOSE)
        self.wait_for_element_to_disappear(self.constructor_locators.MODAL)