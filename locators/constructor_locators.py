from selenium.webdriver.common.by import By

class ConstructorLocators:
    # Модальные окна
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_modal__close__')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")
    
    # Детали ингредиента 
    INGREDIENT_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_NAME = (By.XPATH, "//h2[text()='Детали ингредиента']/following-sibling::p")  # Название после заголовка
    INGREDIENT_CALORIES = (By.XPATH, "//p[contains(text(), 'Калории,ккал')]")
