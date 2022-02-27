class MyError(ValueError):
    # Опять говорится о классе-исключении который должен что-то делать. Может имеллось ввиду просто класс???
    def __str__(self):
        return 'Вводить только числа'


result = []
while True:
    element = input('Введи элемент для списка ')
    if element == 'stop':
        break
    try:
        if not element.isdigit():
            raise MyError
    except MyError as err:
        print(err)
    else:
        result.append(element)
print(result)
