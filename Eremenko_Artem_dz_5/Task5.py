def get_uniq_numbers(src: list):  # Вариант что был написан без подглядывания в код урока
    result = []
    ban_list = set()
    for elem in src:
        if elem not in ban_list:
            result.append(elem)
            ban_list.add(elem)
        else:
            if elem in result:
                result.remove(elem)
    yield result  # не уверен что использую правильно но вот так. Выводит лист


# # Улучшенный вариант после сравнения с кодом урока
#     result = set()  # set лучше по количеству памяти. \
#     # А вывод листа-генератора почему-то в два раза быстрее чем вывод листа
#     ban_list = set()
#     for el in src:
#         if el not in ban_list:
#             result.add(el)
#             ban_list.add(el)
#         else:
#             result.discard(el)
#     yield [el for el in src if el in result]  # Выводит лист с генератором внутри чтобы все шло согласно условию


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
