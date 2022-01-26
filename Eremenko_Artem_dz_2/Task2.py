def convert_list_in_str(list_in: list) -> str:
    list_out = []  # Подготовка списка для вывода
    for i in list_in:  # перебор элементов изначального списка
        if i.isdigit():  # Проверка является ли элемент числом
            list_out.append(f'"{i.zfill(2)}"')  # Запись элемента в кавычках с форматированием под минимум 2 знака
        elif i[0] == '+' or i[0] == '-':  # То же самое но для температуры
            list_out.append(f'"+{i[1:].zfill(2)}"')
        else:  # Для всего что не является числом
            list_out.append(f'{i}')
    str_out = ' '.join(list_out)  # Преобразование списка в строку черех пробел
    return str_out  # Вывод строки


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
