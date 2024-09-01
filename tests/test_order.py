import allure

from data import Urls, OrderData
from locators.order_page_locator import OrderPageLocators
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка верхней кнопки заказа')
    @allure.description(
        'Находим сверху кнопку Заказа и нажимаем на нее')
    def test_upper_order_button(self, driver):
        up_order_button = OrderPage(driver)
        up_order_button.open_page(Urls.MAIN_PAGE)
        up_order_button.wait_and_find_element(OrderPageLocators.UPPER_ORDER_BUTTON).click()
        assert driver.current_url == Urls.ORDER_PAGE

    @allure.title('Проверка нижней кнопки заказа')
    @allure.description(
        'Находим снизу кнопку Заказа и нажимаем на нее')
    def test_lower_order_button(self, driver):
        low_order_button = OrderPage(driver)
        low_order_button.open_page(Urls.MAIN_PAGE)
        low_order_button.scroll_to_element(OrderPageLocators.LOWER_ORDER_BUTTON)
        low_order_button.wait_and_find_element(OrderPageLocators.LOWER_ORDER_BUTTON).click()
        assert driver.current_url == Urls.ORDER_PAGE

    @allure.title('Полная процедура заказа самоката, 1 вариант')
    @allure.description(
        'Заказываем самокат с 1 вариантов данных')
    def test_order_scooter_1_data(self, driver,):
        order = OrderPage(driver)
        order.open_page(Urls.ORDER_PAGE)
        order.order_scooter(
            OrderData.NAME[0],
            OrderData.SECOND_NAME[0],
            OrderData.ADDRESS[0],
            OrderData.METRO_STATION[0],
            OrderData.PHONE_NUMBER[0],
            OrderData.DELIVERY_DATE[0],
            OrderData.RENT_PERIOD[0]
        )
        assert order.find_status_button().is_displayed

    @allure.title('Полная процедура заказа самоката, 2 вариант')
    @allure.description(
        'Заказываем самокат со вторым вариантом данных')
    def test_order_scooter_2_data(self, driver,):
        order = OrderPage(driver)
        order.open_page(Urls.ORDER_PAGE)
        order.order_scooter(
            OrderData.NAME[1],
            OrderData.SECOND_NAME[1],
            OrderData.ADDRESS[1],
            OrderData.METRO_STATION[1],
            OrderData.PHONE_NUMBER[1],
            OrderData.DELIVERY_DATE[1],
            OrderData.RENT_PERIOD[1]
        )
        assert order.find_status_button().is_displayed

    @allure.title('Переходим на главную страницу через главное лого')
    def test_scooter_logo_redirect(self, driver):
        scooter_logo = OrderPage(driver)
        scooter_logo.open_page(Urls.ORDER_PAGE)
        scooter_logo.click_scooter_logo()
        assert driver.current_url == Urls.MAIN_PAGE

    @allure.title('Переходим на яндекс дзен через главное лого')
    def test_yandex_logo_redirect(self, driver):
        yandex_logo = OrderPage(driver)
        yandex_logo.open_page(Urls.ORDER_PAGE)
        yandex_logo.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        yandex_logo.wait_and_find_element(OrderPageLocators.DZEN_NEWS)
        assert driver.current_url == Urls.DZEN_URL
