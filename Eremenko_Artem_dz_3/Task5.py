import random


def get_jokes(count: int, repeat=True) -> list:
    """Возвращает список шуток в количестве count, repeat - флаг разрешающий повторение слов"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_out = []
    forbidden = []  # Список запрещённых слов для repeat = False
    if not repeat:  # Защита от дурака
        count = min(len(nouns), len(adverbs), len(adjectives))
    for i in range(count):  # Создание ответа путём перебора элементов
        argument_1 = random.choice(nouns)  # Выбор 3 случайных аргументов из 3 списков
        argument_2 = random.choice(adverbs)
        argument_3 = random.choice(adjectives)
        if repeat:  # Если повторять слова можно
            joke = f'{argument_1} {argument_2} {argument_3}'  # Создание ответа
            list_out.append(joke)  # Добавление ответа в список
        else:  # Если повторять слова нельзя
            forbidden.extend([argument_1, argument_2, argument_3])  # Занесение трёх элементов в запрещённый список
            nouns = list(set(nouns) - set(
                forbidden))  # Перезапись списоков с исключением запрещённых слов путём вычитания множеств
            adverbs = list(set(adverbs) - set(forbidden))
            adjectives = list(set(adjectives) - set(forbidden))
            joke = f'{argument_1} {argument_2} {argument_3}'
            list_out.append(joke)
    return list_out


print(get_jokes(6))
print(get_jokes(6, False))
