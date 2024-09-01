from selenium.webdriver.common.by import By


class OrderPageLocators:

    UPPER_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')  #  Вверхняя кнопка заказа
    LOWER_ORDER_BUTTON = (By.CLASS_NAME, 'Button_UltraBig__UU3Lp')  # Нижняя кнопка заказа
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле Имя
    SECOND_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле Фамилия
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # Поле адреса
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Поле Станция Метро
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле Номер Телефона
    CONTINUE_BUTTON = (By.XPATH, "//button[text() = 'Далее']")  # Кнопка Далее
    DELIVERY_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")  # Поле даты доставки
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")  # Поле срока аренды
    ORDER_BUTT = (By.XPATH, "//button[(@class = 'Button_Button__ra12g Button_Middle__1CSJM') and (text() = 'Заказать')]")  # Кнопка заказать
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Да']")  # Кнопка подверждение заказа
    SHOW_STATUS_BUTTON = (By.XPATH, "//button[text() = 'Посмотреть статус']")  # Кнопка посмотреть статус заказа
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")  # Главное лого: самокат
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")  # Главное лого: яндекс
    DZEN_NEWS = (By.XPATH, "//div[text() = 'Новости']")  # Элемент новости на яндекс дезене

    @staticmethod
    def period_locator(period: str):   # Выбор периода аренды
        return [By.XPATH, f"//div[contains(text(),'{period}')]"]

    @staticmethod
    def date_locator(day_number: str):  # Выбор даты доставки
        return [By.XPATH, f"//div[contains(text(),'{day_number}')]"]

    @staticmethod
    def station_locator(station: str):  # Выбор станции метро
        return [By.XPATH, f"//div[contains(text(),'{station}')]"]

