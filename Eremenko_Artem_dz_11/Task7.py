class ComplexNumber:
    def __init__(self, element: str, complex_element: str):
        """Все элементы необходимо указывать вместе с арифметическим символом"""
        if not 'i' in element:
            self.a = int(element)
            self.b = int(complex_element[:-1])
        else:
            self.a = int(complex_element)
            self.b = int(element[:-1])

    def __add__(self, other):
        a = self.a + other.a
        b = f'{self.b + other.b}i'
        if b.startswith('-'):
            b = f'({b})'
        print(f'{a}+{b}')

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = f'{self.a * other.b + self.b * other.a}i'
        if b.startswith('-'):
            b = f'({b})'
        return f'{a}+{b}'


number1 = ComplexNumber('+1234', '+5i')
number2 = ComplexNumber('-7i', '-1')
number1 + number2
print(number1 * number2)
