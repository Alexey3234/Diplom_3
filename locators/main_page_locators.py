from selenium.webdriver.common.by import By

class MainPageLocators:
    # Основные кнопки навигации
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, 'account') or contains(text(), 'Личный Кабинет')]")
    
    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'Ingredient_ingredient__')]")
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket__')]")
    BUNS_SECTION = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')  # Ингредиент "Флюоресцентная булка R2-D3"

    # Локаторы для оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__') and .//p[contains(@class, 'digits-large')]]")
    
    # Локаторы для авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, 'account/profile')]")
