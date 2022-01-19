def transform_string(number): #Возвращает строку вида 'N процентов' с учётом склонения по указанному number
    string = str(number)
    if int(string) > 4 and int(string) < 21:
        result = f'{number} процентов'
    elif int(string[-1]) == 0 or int(string[-1]) > 4:
        result = f'{number} процентов'
    elif int(string[-1]) == 1:
        result = f'{number} процент'
    else:
        result = f'{number} процента'
    return result


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))