from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    stop1 = line.find('- -') - 1
    remote_addr = line[:stop1]
    start2 = line.find('"') + 1
    stop2 = line.find('/downloads')
    request_type = line[start2:stop2 - 1]
    stop3 = line.find('HTTP') - 1
    requested_resource = line[stop2:stop3]
    result = (remote_addr, request_type, requested_resource)
    return result


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for str_in in fr.readlines():
        tuple_out = get_parse_attrs(str_in)
        list_out.append(tuple_out)
pprint(list_out)
