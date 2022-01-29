def thesaurus(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for name in args:
        key = name[0]
        if dict_out.get(key):
            if name not in dict_out[key]:
                dict_out[key].append(name)
        else:
            dict_out.update({key: [name]})
    dict_out = sorted(dict_out.items())
    return dict_out


print(thesaurus( "Мария", "Петр", "Илья", "Иван"))
