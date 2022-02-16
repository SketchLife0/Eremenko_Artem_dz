import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'\w+[@]\w+\.\w{2,3}')
    if not RE_MAIL.fullmatch(email):
        raise ValueError(f'wrong email: {email}')
    result_list = email.split('@')
    result_dict = {'username': result_list[0], 'domain': result_list[1]}
    return result_dict


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))
