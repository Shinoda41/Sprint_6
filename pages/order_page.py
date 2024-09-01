import allure

from pages.base_page import BasePage
from locators.order_page_locator import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Заполняем поле Имя')
    def set_name(self, name):
        name_input = self.wait_and_find_element(OrderPageLocators.NAME_FIELD)
        name_input.send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_second_name(self, second_name):
        second_name_input = self.wait_and_find_element(OrderPageLocators.SECOND_NAME_FIELD)
        second_name_input.send_keys(second_name)

    @allure.step('Заполняем поле Адрес')
    def set_address(self, address):
        address_input = self.wait_and_find_element(OrderPageLocators.ADDRESS_FIELD)
        address_input.send_keys(address)

    @allure.step('Заполняем поле Станция метро')
    def set_metro_station(self, station):
        metro_station_input = self.wait_and_find_element(OrderPageLocators.METRO_STATION_FIELD)
        metro_station_input.click()
        button = self.wait_and_find_element(OrderPageLocators.station_locator(station))
        button.click()

    @allure.step('Заполняем поле Номер телефона')
    def set_phone_number(self, phone_number):
        phone_number_input = self.wait_and_find_element(OrderPageLocators.PHONE_NUMBER_FIELD)
        phone_number_input.send_keys(phone_number)

    @allure.step('Кликаем кнопку далее')
    def click_continue_button(self):
        button = self.wait_and_find_element(OrderPageLocators.CONTINUE_BUTTON)
        button.click()

    @allure.step('Заполняем поле Дата доставки')
    def set_delivery_date(self, day_number):
        delivery_date_input = self.wait_and_find_element(OrderPageLocators.DELIVERY_DATE_FIELD)
        delivery_date_input.click()
        button = self.wait_and_find_element(OrderPageLocators.date_locator(day_number))
        button.click()

    @allure.step('Заполняем поле Срок Аренды')
    def set_rental_period(self, period):
        rental_period_input = self.wait_and_find_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        rental_period_input.click()
        button = self.wait_and_find_element(OrderPageLocators.period_locator(period))
        button.click()

    @allure.step('Кликаем кнопку заказать')
    def click_order_button(self):
        button = self.wait_and_find_element(OrderPageLocators.ORDER_BUTT)
        button.click()

    @allure.step('Подтверждаем заказ')
    def click_confirm_button(self):
        button = self.wait_and_find_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        button.click()

    @allure.step('Находим кнопку Статус Заказа')
    def find_status_button(self):
        button = self.wait_and_find_element(OrderPageLocators.SHOW_STATUS_BUTTON)
        return button

    @allure.step('Заказаываем самокат')
    def order_scooter(self, name, second_name, address, metro_station, phone_number, day_number, period):
        self.set_name(name)
        self.set_second_name(second_name)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone_number(phone_number)
        self.click_continue_button()
        self.set_delivery_date(day_number)
        self.set_rental_period(period)
        self.click_order_button()
        self.click_confirm_button()

    @allure.step('Кликаем Самокат в главном лого')
    def click_scooter_logo(self):
        scooter_logo = self.wait_and_find_element(OrderPageLocators.SCOOTER_LOGO)
        scooter_logo.click()

    @allure.step('Кликаем Яндекс в главном лого')
    def click_yandex_logo(self):
        yandex_logo = self.wait_and_find_element(OrderPageLocators.YANDEX_LOGO)
        yandex_logo.click()

