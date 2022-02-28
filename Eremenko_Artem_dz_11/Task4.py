class Warehouse:
    """Инициализация склада"""

    def __init__(self, size=1000):
        self.equipment = {}  # Словарь-перечень предметов на складе
        self.size = size  # Размер склада
        try:
            if not type(self.size) is int:
                raise ValueError
        except:
            print('Недопустимое значение')


    def __add__(self, other):
        """
        Метод добавления предмета на склад
        Сначала указывать склад, потом что добавить
        """
        if self.size - other.number < 0:
            return 'Невозможно выполнить. Склад переполнен'
        else:
            self.size = self.size - other.number
            return 'Предмет добавлен на склад'

    def transfer(self, name: str, name_warehouse: object, number=1):  # Передача предмета из склада в отделение
        try:
            if not type(name) is str and type(number) is int and type(name_warehouse) is object:
                raise ValueError
        except:
            print('Недопустимое значение')
        if not self.equipment.get(name):
            self.equipment.update({name: 1})
        else:
            self.equipment[name] += number
        self.size -= number
        name_warehouse.size += number


class OfficeEquipment:
    def __init__(self, company, model, number=1):
        self.company = company
        self.model = model
        self.number = number
        try:
            if not type(self.company) and type(self.model) is str and type(self.number) is int:
                raise ValueError
        except:
            print('Недопустимое значение')


class Printer(OfficeEquipment):
    task = 'печатать'


class Scanner(OfficeEquipment):
    price_in_USD = 100


class Xerox(OfficeEquipment):
    print_speed = '10 sheets in 1 minute'


sklad = Warehouse(5)
printer = Printer('Dell', 'A-300')
print(sklad + printer)
office = Warehouse()
office.transfer('printer', sklad)
print(office.equipment)
