from yahooparser import Ticker
from prettytable import PrettyTable


def get_tickers(ticker_list):
    """
    Создает экземпляры класса Ticker из полученного списка
    :param ticker_list:  получает список тикеров
    :return: возвращает список с экземплярами класса Ticker
    """
    tickers = []
    for element in ticker_list:
        name = ticker_list[element]
        tickers.append(Ticker(name))

    for name in range(len(tickers)):
        tickers[name].update()
    return tickers


def show_table(tickers):
    """
    Демонстрация полученных данных в ходе работы скрипта
    :return: ничего не возвращает
    """
    # ----- считаем знрачения из класса в переменные
    show_list = []
    for ticker in tickers:
        name = ticker.name
        price = round(ticker.price, 2)
        change = round(ticker.change, 2)
        percent = round(ticker.percent * 100, 2)
        volume = round(ticker.volume, 2)
        # ----- создадим словарь со списком внутри
        show_list.append({name: [price, change, percent, volume]})

    # ----- эта простая табличка - очень крутая вещь
    myTable = PrettyTable()

    # ----- создаем заголовки таблицы
    myTable.field_names = ["Name", "Price", "Change", "Perc. change", "Volume"]

    # ----- добавляем строки в таблицу
    for string in show_list:
        for key in string:
            myTable.add_row([key, string[key][0], string[key][1], string[key][2], string[key][3]])
    # печатаем таблицу с полученными значениями.
    print(myTable)


# ----------------------------------------------------
# в этот словарь можно добавить любые бумаги
# после запуска скрипта создадутся объекты с
# аналогичными именами, для которых будут запрошены
# значения, после чего их можно использовать или распечатать
# ----------------------------------------------------
ticker_list = {'gazp': 'GAZP.ME',
               'sber': 'SBER.ME',
               'tatn': 'TATN.ME',
               'moex': 'MOEX.ME',
               'rosn': 'ROSN.ME',
               'lkoh': 'LKOH.ME',
               'yndx': 'YNDX.ME',
               'nlmk': 'NLMK.ME',
               'alrs': 'ALRS.ME',
               'rual': 'RUAL.ME',
               'magn': 'MAGN.ME'}
# ----------------------------------------------------


# -------- создаем экземпляры класса
tickers = get_tickers(ticker_list)

# -------- распечатаем для примера
show_table(tickers)