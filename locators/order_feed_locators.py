from selenium.webdriver.common.by import By

class OrderFeedLocators:
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    ORDER_LIST = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]")
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]//p[contains(@class, 'text_type_digits-default')]")
    
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]")
    ORDERS_IN_PROGRESS_ITEMS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li")
    
    ORDER_LIST_ALT = (By.XPATH, "//h1[text()='Лента заказов']/following::div[contains(@class, 'list')]")
    IN_PROGRESS_ALT = (By.XPATH, "//*[contains(text(), 'В работе')]/following::ul")