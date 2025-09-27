import allure
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class TestOrderFeed:
    
    @allure.title('Проверка увеличения счетчика "Выполнено за все время"')
    def test_total_orders_counter_increases(self, driver, login, pages):
        main_page = pages['main_page']
        order_feed_page = pages['order_feed_page']

        main_page.navigate_to_order_feed()
        initial_total = order_feed_page.get_total_orders_count()

        main_page.navigate_to_constructor()
        main_page.add_ingredient_to_constructor(0)
        main_page.create_order()
        main_page.wait_for_order_modal()
        order_number = main_page.get_order_number()
        main_page.close_modal()

        main_page.navigate_to_order_feed()
        current_total = order_feed_page.get_total_orders_count()

        assert order_number is not None, "Заказ не был создан"
        assert current_total > initial_total, f"Счетчик не увеличился: {current_total} <= {initial_total}"
    
    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня"')
    def test_today_orders_counter_increases(self, driver, login, pages):
        main_page = pages['main_page']
        order_feed_page = pages['order_feed_page']
        
        main_page.navigate_to_order_feed()
        initial_today = order_feed_page.get_today_orders_count()

        main_page.navigate_to_constructor()
        main_page.add_ingredient_to_constructor(0)
        main_page.create_order()
        main_page.wait_for_order_modal()
        order_number = main_page.get_order_number()
        main_page.close_modal()

        main_page.navigate_to_order_feed()
        current_today = order_feed_page.get_today_orders_count()
        
        assert order_number is not None, "Заказ не был создан"
        assert current_today > initial_today, f"Счетчик не увеличился: {current_today} <= {initial_today}"
    
    @allure.title('Проверка создания заказа с получением номера')
    def test_order_creation_with_number(self, driver, login, pages):
        main_page = pages['main_page']

        main_page.add_ingredient_to_constructor(0)
        main_page.create_order()
        main_page.wait_for_order_modal()
        order_number = main_page.get_order_number()
        main_page.close_modal()

        assert order_number is not None, "Заказ не был создан"
        assert len(order_number) > 0, "Номер заказа пустой"

    @allure.title('Проверка отображения заказа в ленте')
    def test_order_appears_in_feed(self, driver, login, pages):
        main_page = pages['main_page']
        order_feed_page = pages['order_feed_page']

        main_page.add_ingredient_to_constructor(0)
        main_page.create_order()
        main_page.wait_for_order_modal()
        order_number = main_page.get_order_number()
        main_page.close_modal()

        main_page.navigate_to_order_feed()
        
        assert order_number is not None, "Заказ не был создан"
        assert order_feed_page.is_order_in_feed(order_number), f"Заказ {order_number} не найден в ленте"

    @allure.title('Проверка наличия раздела "В работе"')
    def test_orders_in_progress_section_exists(self, driver, login, pages):
        main_page = pages['main_page']
        order_feed_page = pages['order_feed_page']

        main_page.navigate_to_order_feed()
        
        assert order_feed_page.is_order_in_progress_section(), "Раздел 'В работе' не отображается"

    @allure.title('Проверка что раздел "В работе" отображается корректно')
    def test_orders_in_progress_section_displayed(self, driver, login, pages):
        main_page = pages['main_page']
        order_feed_page = pages['order_feed_page']

        main_page.navigate_to_order_feed()
        
        section_exists = order_feed_page.is_order_in_progress_section()
        
        orders_in_progress = order_feed_page.get_orders_in_progress_numbers()
        
        assert section_exists, "Раздел 'В работе' не отображается"