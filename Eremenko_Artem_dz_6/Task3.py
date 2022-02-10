import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    name_list = []
    hobby_list = []
    with open(path_users_file, 'r', encoding='utf-8') as f:
        for str_in1 in f:
            str_in1 = str_in1.replace(',', ' ')
            name_list.append(str_in1.strip())
    with open(path_hobby_file, 'r', encoding='utf-8') as f:
        for str_in2 in f:
            hobby_list.append(str_in2.strip())
    if len(hobby_list) > len(name_list):
        print('Некорректно заполнен файл hobby.csv')
        sys.exit(1)
    dict_out_funk = {}
    a = 0
    for i in range(len(name_list)):
        if i < len(hobby_list):
            for j in range(len(hobby_list)):
                j += a
                a += 1
                dict_out_funk.update({name_list[i]: hobby_list[j]})
                break
        else:
            dict_out_funk.update({name_list[i]: None})
    return dict_out_funk


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
