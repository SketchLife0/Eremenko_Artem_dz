import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты code по отношению к рублю"""
    result = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")  # Создание Get запроса на сайт
    data_received_list = result.text.split('Valute')  # Сохранение полученных данных в список с удобным разбиванием
    for i in range(len(data_received_list)):  # Перебор элементров списка пока не найдёт нужный
        if code in data_received_list[i]:  # Проверка наличия в элементе списка нужной строки
            list_item = data_received_list[i]  # Фиксация нужного элемента списка
            start = list_item.find('<Value>')  # Поиск начала курса валюты
            stop = list_item.find('</Value>')  # Поиск конца курса валюты
            result_value = list_item[start + 7:stop]  # Фиксация элемента путём среза
            result_value = float(result_value.replace(',', '.'))  # Получение float элемента с заменой запятой на точку
            break  # Прерывание цикла для прекращения перебора
        else:  # В случае если элемент пока не найден или не найдётся вовсе он даст вывод согласно поставленной задаче
            result_value = None
    return result_value


print(currency_rates("USD"))
print(currency_rates("EUR"))
print(currency_rates("noname"))
# Для работы с подсчётом денежных средств для подсчёта точного результата лучше использовать Decimal вместо Float
# Но для простого вывода числа в этом нет необходимости
