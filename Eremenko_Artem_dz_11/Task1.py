import time


class Date:

    def __init__(self, date: str):
        """
        :param date: введённая строка даты в формате день-месяц-год
        """
        Date.date = date

    @classmethod
    def converter(cls):
        datelist = cls.date.split('-')
        result = [int(elem) for elem in datelist]
        Date.result = result
        return result

    @staticmethod
    def validator():
        try:
            valid_date = time.strptime(Date.date, '%d-%m-%Y')
        except ValueError:
            return 'Invalid date'
        else:
            return 'Date valid'


if __name__ == '__main__':
    first_date = Date('29-03-1997')
    print(first_date)
    print(first_date.converter())
    print(first_date.validator())
