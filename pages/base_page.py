from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from seletools.actions import drag_and_drop
import allure


class BasePage:
    TIMEOUT = 15
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)
        self.actions = ActionChains(driver)
    
    @allure.step("Кликнуть на элемент по локатору")
    def click(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()
    
    @allure.step("Получить текст элемента")
    def get_text(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        return element.text
    
    @allure.step("Ввести текст в поле")
    def input_text(self, locator, text, timeout=TIMEOUT):
        element = self.wait_for_element_clickable(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator, timeout=5):
        try:
            return self.wait_for_element(locator, timeout) is not None
        except TimeoutException:
            return False
    
    @allure.step("Ожидать исчезновения элемента")
    def wait_for_element_to_disappear(self, locator, timeout=TIMEOUT):
        self.wait.until(EC.invisibility_of_element_located(locator))
    
    @allure.step("Ожидать видимости элемента")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ожидать кликабельности элемента")
    def wait_for_element_clickable(self, locator, timeout=TIMEOUT):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Найти элементы")
    def find_elements(self, locator, timeout=TIMEOUT):
        self.wait_for_element(locator, timeout)
        return self.driver.find_elements(*locator)
    
    @allure.step("Получить количество элементов")
    def get_elements_count(self, locator, timeout=TIMEOUT):
        elements = self.find_elements(locator, timeout)
        return len(elements)
    
    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, element=None):
        if element:
            return self.driver.execute_script(script, element)
        return self.driver.execute_script(script)
    
    @allure.step("Прокрутить к элементу через JavaScript")
    def scroll_to_element(self, element):
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получить заголовок страницы")
    def get_title(self):
        return self.driver.title
    
    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self, timeout=10):
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    
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
    
    @allure.step("Нажать ESC")
    def press_escape_key(self):
        self.actions.send_keys(Keys.ESCAPE).perform()
        self.actions.reset_actions()

    @allure.step("Проверить URL на содержание текста")
    def is_url_contains(self, text):
        return text in self.get_current_url()
    
    @allure.step("Проверить кликабельность элемента")
    def is_element_clickable(self, locator, timeout=5):
        try:
            return self.wait_for_element_clickable(locator, timeout) is not None
        except:
            return False
    
    @allure.step("Найти элемент")
    def find_element(self, locator, timeout=TIMEOUT):
        return self.wait_for_element(locator, timeout)
    
    @allure.step("Прокрутить к элементу через JavaScript")
    def scroll_to_element_js(self, element):
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    @allure.step("Получить заголовок страницы")
    def get_current_page_title(self):
        return self.driver.title
    
    @allure.step("Получить исходный код страницы")
    def get_page_source(self):
        return self.driver.page_source
    
    @allure.step("Открыть новую вкладку")
    def open_new_tab(self):
        self.driver.execute_script("window.open('');")

    @allure.step("Переключиться на первую вкладку")
    def switch_to_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step("Переключиться на последнюю вкладку")
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
    
    # ДОБАВЛЕННЫЕ МЕТОДЫ:
    
    @allure.step("Кликнуть на элемент (объект)")
    def click_element(self, element):
        """Кликнуть на переданный элемент"""
        self.execute_script("arguments[0].click();", element)
    
    @allure.step("Получить текст элемента (объект)")
    def get_element_text(self, element):
        """Получить текст переданного элемента"""
        return element.text.strip()
    
    @allure.step("Ввести текст в элемент")
    def send_keys(self, locator, text):
        """Ввести текст в элемент по локатору"""
        element = self.wait_for_element_clickable(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Ожидать появления текста в элементе")
    def wait_for_text_in_element(self, locator, text, timeout=TIMEOUT):
        """Ожидать появления определенного текста в элементе"""
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))
    
    @allure.step("Проверить наличие текста на странице")
    def is_text_present(self, text):
        """Проверить наличие текста на странице"""
        return text in self.get_page_source()
    
    @allure.step("Переключиться в iframe")
    def switch_to_frame(self, locator, timeout=TIMEOUT):
        """Переключиться в iframe по локатору"""
        frame = self.wait_for_element(locator, timeout)
        self.driver.switch_to.frame(frame)
    
    @allure.step("Вернуться из iframe")
    def switch_to_default_content(self):
        """Вернуться к основному контенту"""
        self.driver.switch_to.default_content()
    
    @allure.step("Переместиться к элементу")
    def move_to_element(self, element):
        """Переместить курсор к элементу"""
        self.actions.move_to_element(element).perform()
    
    @allure.step("Двойной клик по элементу")
    def double_click(self, locator, timeout=TIMEOUT):
        """Двойной клик по элементу"""
        element = self.wait_for_element_clickable(locator, timeout)
        self.actions.double_click(element).perform()
    
    @allure.step("Клик правой кнопкой мыши")
    def right_click(self, locator, timeout=TIMEOUT):
        """Клик правой кнопкой мыши по элементу"""
        element = self.wait_for_element_clickable(locator, timeout)
        self.actions.context_click(element).perform()
    
    @allure.step("Обновить страницу")
    def refresh_page(self):
        """Обновить текущую страницу"""
        self.driver.refresh()
    
    @allure.step("Вернуться назад")
    def go_back(self):
        """Вернуться на предыдущую страницу"""
        self.driver.back()
    
    @allure.step("Перейти вперед")
    def go_forward(self):
        """Перейти на следующую страницу в истории"""
        self.driver.forward()
    
    @allure.step("Принять alert")
    def accept_alert(self, timeout=TIMEOUT):
        """Принять alert"""
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
    
    @allure.step("Отклонить alert")
    def dismiss_alert(self, timeout=TIMEOUT):
        """Отклонить alert"""
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()
    
    @allure.step("Получить текст alert")
    def get_alert_text(self, timeout=TIMEOUT):
        """Получить текст alert"""
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert.text
    
    @allure.step("Установить значение cookie")
    def set_cookie(self, name, value):
        """Установить cookie"""
        self.driver.add_cookie({'name': name, 'value': value})
    
    @allure.step("Получить значение cookie")
    def get_cookie(self, name):
        """Получить cookie по имени"""
        return self.driver.get_cookie(name)
    
    @allure.step("Удалить cookie")
    def delete_cookie(self, name):
        """Удалить cookie по имени"""
        self.driver.delete_cookie(name)
    
    @allure.step("Очистить все cookies")
    def delete_all_cookies(self):
        """Удалить все cookies"""
        self.driver.delete_all_cookies()
    
    @allure.step("Выполнить асинхронный JavaScript")
    def execute_async_script(self, script, *args):
        """Выполнить асинхронный JavaScript"""
        return self.driver.execute_async_script(script, *args)
    
    @allure.step("Получить значение атрибута элемента")
    def get_attribute(self, locator, attribute, timeout=TIMEOUT):
        """Получить значение атрибута элемента"""
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)
    
    @allure.step("Проверить, что элемент выбран (чекбокс/радио)")
    def is_element_selected(self, locator, timeout=TIMEOUT):
        """Проверить, выбран ли элемент"""
        element = self.wait_for_element(locator, timeout)
        return element.is_selected()
    
    @allure.step("Проверить, что элемент включен")
    def is_element_enabled(self, locator, timeout=TIMEOUT):
        """Проверить, включен ли элемент"""
        element = self.wait_for_element(locator, timeout)
        return element.is_enabled()