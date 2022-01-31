def thesaurus_adv(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for full_name in args:  # выбор одного имени
        name_surname = full_name.split()  # Разбитие имени на список имя фамилия
        surname_list = list(name_surname[1])  # Разбитие фамилии на символы
        surname_key = surname_list[0]  # Подготовка ключа фамилии
        name_list = list(name_surname[0])  # Разбитие имени на символы
        name_key = name_list[0]  # Подготовка ключа имени
        if dict_out.get(surname_key):  # Проверка истинности ключа фамилии
            dict_in_surname = dict_out[surname_key]  # Выделение внутреннего словаря по ключу фамилии
            if name_key in dict_in_surname:  # Проверка истинности ключа имени во внутреннем словаре фамилии
                dict_in_surname[name_key].append(full_name)  # Добавление нового имени в нужно место
                dict_in_surname[name_key].sort()  # Сортировка имён в списке ключа имени
            else:
                dict_in_surname.update({name_key: [full_name]})  # Создание нового ключа имени и списка значения
        else:  # создание ключа фамилии если такого нет
            dict_out.update({surname_key: {name_key: [full_name]}})
    dict_out = sorted(dict_out.items())  # Сортировка основного словаря по ключам
    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Мария Савельева", "Петр Алексеев", "Петр Акинфеев", "Илья Иванов"))
