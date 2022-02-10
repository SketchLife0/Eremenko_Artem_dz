def get_parse_attrs(line: str) -> str:
    """Берёт строку и возвращает ip"""
    stop1 = line.find('- -') - 1  # Из строки находит где заканчивается ip
    remote_addr = line[:stop1]  # Выводит сам ip
    return remote_addr


def spammer_detection(ip_list: list) -> str:
    '''Берёт лист и возвращает строку кто спамер'''
    spammer_ip = ''  # Подготовка перенной для определения ip
    number_of_requests = 0  # Подготовка переменной для определения количества запросов
    ip_set = set()  # Подготовка множества чтобы ip не проверялись каждый раз повторно
    for elem in ip_list:  # Проверка айпи по списку
        if elem not in ip_set:  # Проверка на то проверялся ли ip ранее
            ip_set.add(elem)  # Добавление элемента в исключения
            number = ip_list.count(elem)  # Запись количества запросов по этому ip
            if number > number_of_requests:  # Сравнение является ли это найбольшим количеством запросов
                number_of_requests = number  # Приравнивание нового рекорда запросов
                spammer_ip = elem  # Запись нынешнего рекордсмена
    detected_spammer = f'{spammer_ip} - является спамером и сделал {number_of_requests} запросов'
    return detected_spammer


list_out = list()  # Создаёт список для ip
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:  # Открывает файл на чтение
    while True:  # Бесконечный цикл чтения файла по строке на случай большого файла
        line = fr.readline()
        if not line:  # Если строка пуста цикл заканчивается
            break
        list_out.append(get_parse_attrs(line))  # Обновляет список добавляя в него все выведенный ip
print(spammer_detection(list_out))
