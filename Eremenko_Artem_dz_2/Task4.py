def convert_name_extract(list_in: list) -> list:  # Извлекает имена из элементов и формирует список приветствий
    list_out = []  # Подготовка списка на вывод
    for i in list_in:  # Перебор элементом входящего списка
        one_list_item = i.split()  # разбивание пришедшей строки на список
        list_out.append(
            f'Привет, {one_list_item[-1].title()}!')  # Вывод в подготовленый список последнего элемента в нужном формате
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
