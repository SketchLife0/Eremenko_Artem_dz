tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '11Б', '9А']


def check_gen(tutors: list, klasses: list):
    # a = list(zip(tutors, klasses))  # Для использования второго способа необходим этот список
    for i in range(len(tutors)):  # перебор по длине tutors согласно поставленной задаче
        if i < len(klasses):  # первый способ через простой вывод кортежей по подобранным элементам
            yield tutors[i], klasses[i]
        else:
            yield tutors[i], None
        # if i >= len(klasses):  # Второй способ через zip список
        #     a.append((tutors[i], None))
        # yield a[i]


generator = check_gen(tutors, klasses)
print(type(generator))  # <class 'generator'>
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
