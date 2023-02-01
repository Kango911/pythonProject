import requests
from dpath.util import values as path_val


class Ticker:
    # -------- URL запрос будет через открытие сессии
    session = requests.session()

    # -------- заголовки для URL запроса
    headers = 'Mozilla/5.0 ' \
              '(Windows NT 10.0; WOW64) ' \
              'AppleWebKit/537.36' \
              ' (KHTML, like Gecko) ' \
              'Chrome/91.0.4472.135 ' \
              'Safari/537.36'

    # -------- Запрашиваемые поля
    value = {'price': 'regularMarketPrice',
             'percent': 'regularMarketChangePercent',
             'change': 'regularMarketChange',
             'volume': 'regularMarketVolume'}

    # -------- конструктор
    def __init__(self, name):
        # -------- определим первоначальные значения
        self.name = name
        self.price = 0.00
        self.change = 0.00
        self.percent = 0.0
        self.volume = 0.0

    def update(self):
        """
        Устанавливает обновленные значения
        полученные в результате работы _get_update
        """
        # присвоим возвращенный кортеж из функции _ger_update
        self.price, self.percent, self.change, self.volume = self.__get_update()

    def __get_update(self):
        """
            Отправляет URL запрос,  получает JSON
            возвращает список со значениями float
        """
        # -------- ссылка для URL запроса
        link = f"https://query2.finance.yahoo.com/v10/" \
               f"finance/quoteSummary/{self.name}?modules=price"

        # -------- отправляем запрос и получаем результат в response
        response = self.session.get(link, headers={'User-Agent': self.headers})

        # -------- получаем json массив
        array = response.json()

        # ---- создадим список, в который будут помещаться возвращаемые значения
        return_value = []

        # -------- перебором ключей словаря получим все нужные строки,
        #          и сконвертируем их в числа типа float
        for key in self.value:
            return_value.append(float(path_val(array, f"/**/{self.value[key]}/raw")[0]))

        # -------- возвращаем список из всех элементов по ключам из value
        return return_value
