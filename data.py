class Urls:
    MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'


class OrderData:
    NAME = ['Фили', 'Кили']
    SECOND_NAME = ['Филин', 'Килин']
    ADDRESS = ['Проспект победы', 'Проспект мира']
    METRO_STATION = ['Черкизовская', 'Сокольники']
    PHONE_NUMBER = ['+79530379716', '+79530379715']
    DELIVERY_DATE = ['16', '17']
    RENT_PERIOD = ['двое суток', 'трое суток']


class QuestionData:
    param = 'number, expected_answer'
    value = [
        [0, '0'],
        [1, '1'],
        [2, '2'],
        [3, '3'],
        [4, '4'],
        [5, '5'],
        [6, '6'],
        [7, '7'],
    ]
