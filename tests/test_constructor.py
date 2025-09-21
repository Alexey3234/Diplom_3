import allure
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pages.main_page import MainPage

class TestConstructorFunctionality:
    
    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_page_loaded()        
        main_page.open_ingredient_modal(2)        
        assert main_page.is_modal_visible(), "Модальное окно не открылось"

    @allure.title("Отображение деталей ингредиента в модальном окне")
    def test_ingredient_details_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_page_loaded()        
        main_page.open_ingredient_modal(2)        
        assert main_page.is_ingredient_details_visible(), "Детали ингредиента не отобразились"

    @allure.title("Закрытие модального окна через крестик")
    def test_close_modal_by_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_page_loaded()        
        main_page.open_ingredient_modal(2)
        main_page.close_modal_by_button()        
        assert not main_page.is_modal_visible(), "Модальное окно не закрылось"

    @allure.title("Закрытие модального окна через overlay")
    def test_close_modal_by_overlay(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_page_loaded()        
        main_page.open_ingredient_modal(2)
        main_page.close_modal_by_overlay()
        
        assert not main_page.is_modal_visible(), "Модальное окно не закрылось"

    @allure.title("Закрытие модального окна через ESC")
    def test_close_modal_by_esc(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_page_loaded()        
        main_page.open_ingredient_modal(2)
        main_page.close_modal_by_esc()        
        assert not main_page.is_modal_visible(), "Модальное окно не закрылось"