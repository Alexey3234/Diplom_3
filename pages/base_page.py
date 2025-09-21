from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from seletools.actions import drag_and_drop
import allure

class BasePage:
    TIMEOUT = 15
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)
        self.actions = ActionChains(driver)
    
    @allure.step("Кликнуть на элемент")
    def click(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()
    
    @allure.step("Кликнуть на конкретный элемент")
    def click_element(self, element, timeout=TIMEOUT):
        element = self.wait_for_element_clickable(element, timeout)
        element.click()
    
    @allure.step("Получить текст элемента")
    def get_text(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        return element.text
    
    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator, timeout=5):
        try:
            return self.wait_for_element(locator, timeout) is not None
        except:
            return False
    
    @allure.step("Ожидать исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=TIMEOUT):
        self.wait.until(EC.invisibility_of_element_located(locator))
    
    @allure.step("Ожидать видимости элемента")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ожидать кликабельности элемента")
    def wait_for_element_clickable(self, element_or_locator, timeout=TIMEOUT):
        if hasattr(element_or_locator, '__getitem__'):  # Это локатор
            return self.wait.until(EC.element_to_be_clickable(element_or_locator))
        else:  # Это WebElement
            return self.wait.until(EC.element_to_be_clickable(element_or_locator))
    
    @allure.step("Найти элементы")
    def find_elements(self, locator, timeout=TIMEOUT):
        self.wait_for_element(locator, timeout)
        return self.driver.find_elements(*locator)
    
    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=TIMEOUT):
        return self.wait_for_element(locator, timeout)
    
    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, element=None):
        if element:
            return self.driver.execute_script(script, element)
        return self.driver.execute_script(script)
    
    @allure.step("Кликнуть через JavaScript")
    def click_with_js(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        self.execute_script("arguments[0].click();", element)
    
    @allure.step("Прокрутить к элементу через JavaScript")
    def scroll_to_element_js(self, element):
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    @allure.step("Нажать ESC")
    def press_escape_key(self):
        self.actions.send_keys(Keys.ESCAPE).perform()
        self.actions.reset_actions()
    
    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source, target):
        self.actions.drag_and_drop(source, target).perform()
    
    @allure.step("Переместить к элементу")
    def move_to_element(self, element):
        self.actions.move_to_element(element).perform()
    
    @allure.step("Выполнить действия")
    def perform_actions(self):
        self.actions.perform()
    
    @allure.step("Сбросить действия")
    def reset_actions(self):
        self.actions = ActionChains(self.driver)
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Проверить URL на содержание текста")
    def is_url_contains(self, text):
        return text in self.get_current_url()
    
    @allure.step("Обновить страницу")
    def refresh(self):
        self.driver.refresh()
    
    @allure.step("Назад")
    def go_back(self):
        self.driver.back()
    
    @allure.step("Вперед")
    def go_forward(self):
        self.driver.forward()
    
    @allure.step("Получить заголовок страницы")
    def get_title(self):
        return self.driver.title
    
    @allure.step("Получить исходный код")
    def get_page_source(self):
        return self.driver.page_source
    
    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    
    @allure.step("Проверить кликабельность элемента")
    def is_element_clickable(self, locator, timeout=5):
        try:
            return self.wait_for_element_clickable(locator, timeout) is not None
        except:
            return False
    
    @allure.step("Сделать скриншот")
    def take_screenshot(self, name):
        try:
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)
    
    @allure.step("Ожидать выполнения условия")
    def wait_for_condition(self, condition, timeout=TIMEOUT, message=""):
        return self.wait.until(condition, message=message)