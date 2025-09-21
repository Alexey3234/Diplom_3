from selenium.webdriver.common.by import By

class OrderLocators:
    # Счетчики заказов в ленте
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'digits-large')]")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'digits-large')]")
    
    # Раздел "В работе"
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//div[contains(text(), 'В работе')]/following-sibling::ul")
    ORDERS_IN_PROGRESS_ITEMS = (By.XPATH, "//div[contains(text(), 'В работе')]/following-sibling::ul//li")
    
    # Конструктор бургера
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    
    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'Ingredient_ingredient__')]")
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__')]")
    
    # Кнопка оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    
    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_title') and contains(text(), 'идентификатор заказа')]/following-sibling::p")
    ORDER_MODAL_CLOSE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_modal__close__')]")
    ORDER_NUMBER_TEXT = (By.XPATH, "//h2[contains(@class, 'Modal_title')]")
    # Расширенные локаторы для номера заказа
    ORDER_NUMBER_ALT1 = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h2[contains(text(), 'идентификатор')]/following-sibling::p")
    ORDER_NUMBER_ALT2 = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//p[contains(text(), 'Ваш заказ начали готовить')]/preceding-sibling::p")
    ORDER_NUMBER_ALT3 = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//*[contains(@class, 'digits')]")
    ORDER_NUMBER_ALT4 = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//*[contains(text(), '0') and string-length(text()) > 4]")
    ORDER_NUMBER_ALT5 = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//p[contains(@class, 'text_type_digits-large')]")
    
    # Элементы модального окна
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h2")
    MODAL_TEXT = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//p")
    MODAL_IMAGE = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//img")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")
    
    # Лента заказов
    ORDER_FEED_SECTION = (By.XPATH, "//h1[text()='Лента заказов']")
    ALL_ORDERS_LIST = (By.XPATH, "//div[contains(@class, 'OrderHistory_orderList__')]")
    
    # Сообщения об ошибках
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'error') or contains(@class, 'message')]")
    # Раздел "В работе"
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//*[contains(text(), 'В работе')]")
    ORDERS_IN_PROGRESS_ITEMS = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')