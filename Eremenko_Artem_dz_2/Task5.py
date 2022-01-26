from random import uniform

commodity_prices = [57.8, 46.51, 97, 5.05, 15, 96.1, 0.50, 61.25, 33, 17.7, 412.24, 19.3, 52, 87.16, 54.9, 85, 101,
                    108.15, 55.9, 45.05]


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    list_out = []
    for i in list_in:
        a = int(i)
        b = int((i * 100) % 100)
        list_out.append(f'{a} руб {b:02} коп')
    str_out = ', '.join(list_out)
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)
if id(my_list) == id(result_2):
    print('result_2 равен начальному объекту')
else:
    print('result_2 не равен начальному объекту')


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    interim_list = sort_price_adv(list_in)
    list_out = interim_list[:5]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
