from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        len_set = set()
        for elem in matrix:
            len_set.add(len(elem))
            if len(len_set) > 1:
                raise ValueError('fail initialization matrix')

    def __str__(self):
        str_out = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if j == 0:
                    str_out += '| '
                str_out += f'{str(self.matrix[i][j])} '
                if j == len(self.matrix[i]) - 1:
                    str_out += '|\n'
                if i == len(self.matrix) - 1:
                    if j == len(self.matrix[i]) - 1:
                        str_out = str_out.strip()
        return str_out

    def __add__(self, other):
        if not len(self.matrix) == len(other.matrix):
            raise ValueError('Matrix addition error')
        result = [[0 for _ in self.matrix[0]] for _ in self.matrix]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        result_matrix = Matrix(result)
        return result_matrix


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
