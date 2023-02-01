from yahooparser import Ticker
from prettytable import PrettyTable
import pandas as pd
from openpyxl import Workbook
import openpyxl


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
    myTable.field_names = ["Тикер", "Цена", "Изменение за день", "Процентное изменение"]

    # ----- добавляем строки в таблицу
    for string in show_list:
        for key in string:
            myTable.add_row([key, string[key][0], string[key][1], string[key][2]])
    # печатаем таблицу с полученными значениями.
    print(myTable)


# ----------------------------------------------------
# в этот словарь можно добавить любые бумаги
# после запуска скрипта создадутся объекты с
# аналогичными именами, для которых будут запрошены
# значения, после чего их можно использовать или распечатать
# ----------------------------------------------------
ticker_list = {
               'rstip': 'RSTIP.ME',
               'moex': 'MOEX.ME',
               'plzl': 'PLZL.ME',
               'poly': 'POLY.ME',
               'banep': 'BANEP.ME',
               'mrku': 'MRKU.ME',
               'mtss': 'MTSS.ME',
               'ogkb': 'OGKB.ME',
               'gmkn': 'GMKN.ME',
               'nvtk': 'NVTK.ME',
               'posi': 'POSI.ME',
               'tatnp': 'TATNP.ME',
               'rosn': 'ROSN.ME',
               'flot': 'FLOT.ME',
               'yndx': 'YNDX.ME',
               'hhru': 'HHRU.ME',
               'nlmk': 'NLMK.ME',
               'rtkmp': 'RTKMP.ME',
               'fees': 'FEES.ME',
               'sgzh': 'SGZH.ME',
               'tatn': 'TATN.ME',
               'gazp': 'GAZP.ME',
               'sibn': 'SIBN.ME',
               'chmf': 'CHMF.ME',
               'sberp': 'SBERP.ME',
               'sngsp': 'SNGSP.ME',
               'irao': 'IRAO.ME',
               'sber': 'SBER.ME',
               'five': 'FIVE.ME',
               'lkhon': 'LKOH.ME',
               'dsky': 'DSKY.ME',
               'tgka': 'TGKA.ME',
               'aflt': 'AFLT.ME',
               'afks': 'AFKS.ME',
               'phor': 'PHOR.ME',
               'alrs': 'ALRS.ME',
               'magn': 'MAGN.ME',
               'vsmo': 'VSMO.ME',
               'trmk': 'TRMK.ME'
               }
# ----------------------------------------------------


# -------- создаем экземпляры класса
tickers = get_tickers(ticker_list)

# -------- распечатаем для примера
show_table(tickers)

print(ticker_list)




wb = openpyxl.load_workbook("file.xlsx")

sheet = wb.active

data = (ticker_list)

for row in data:
    sheet.append(row)
wb.save("file.xlsx")
