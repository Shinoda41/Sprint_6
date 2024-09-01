class Urls:
    MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'


class OrderData:
    param = 'name, second_name, address, metro_station, phone_number, delivery_date, rent_period'
    value = [
        ['Фили', 'Филин', 'Проспект победы', 'Черкизовская', '+79530379716', '16', 'двое суток'],
        ['Кили', 'Килин', 'Проспект мира', 'Сокольники', '+79530379715', '17', 'трое суток']
    ]


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
