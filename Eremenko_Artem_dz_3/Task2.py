def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    symbol_list = list(value)  # Разбор и сохранение введённой строки по элементам
    value = value.lower()  # Преобразование строки в нужный формат ключа
    arg = list(range(65, 91))  # Создание листа через кодировку
    if ord(symbol_list[0]) in arg:  # Проверка является ли первый символ Большим
        arg_out = numbers.get(value, None)  # Поиск ответа по изменённому ключу
        str_out = arg_out.title()  # Вывод ответа в нужном формате
    else:
        str_out = numbers.get(value, None)
    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("eight"))
print(num_translate_adv('cipi'))
