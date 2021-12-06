import copy
import random
from System.Class_Menu_Except import *
from Entity.Class_Matrix_Except import *


class Matrices:
    def __init__(self, cnt_lines, cnt_columns):
        self.cnt_lines = cnt_lines
        self.cnt_columns = cnt_columns
        self.matrix = [[0*j*i for j in range(cnt_columns)] for i in range(cnt_lines)]

    def show_matrix(self):
        for i in self.matrix:
            print(i)

    def write_matrix(self):
        matrix = self.matrix.copy()
        for i in range(self.cnt_lines):
            print(f"Введите {i + 1} строку:")
            for j in range(self.cnt_columns):
                matrix[i][j] = correct_int()
        self.matrix = matrix

    def __add__(self, other):
        try:
            if self.__eq__(other):
                matrix = [[0*j*i for j in range(self.cnt_columns)] for i in range(self.cnt_lines)]
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[i])):
                        matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                    print(matrix[i])
            else:
                raise MatrixSizeError
        except MatrixSizeError:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def __sub__(self, other):
        try:
            if self.__eq__(other):
                matrix = [[0*j*i for j in range(self.cnt_columns)] for i in range(self.cnt_lines)]
                for i in range(self.cnt_lines):
                    for j in range(self.cnt_columns):
                        matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
                    print(matrix[i])
                return matrix
            else:
                raise MatrixSizeError
        except MatrixSizeError:
            print("Вычитание матриц невозможно осуществить, так как кол-во строк и столбцов в них разное!")

    def __mul__(self, other):
        try:
            if isinstance(other, Matrices):
                matrix = [[0*i*j for j in range(other.cnt_columns)] for i in range(self.cnt_lines)]
                if isinstance(other, Matrices) and (self.cnt_columns == other.cnt_lines):
                    for i in range(self.cnt_lines):
                        for j in range(other.cnt_columns):
                            for k in range(self.cnt_columns):
                                matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                        print(matrix[i])
                    return matrix
                else:
                    raise MatrixSizeError
            elif isinstance(other, int):
                matrix = [[0*j*i for j in range(self.cnt_columns)] for i in range(self.cnt_lines)]
                for i in range(self.cnt_lines):
                    for j in range(self.cnt_columns):
                        matrix[i][j] = self.matrix[i][j] * other
                    print(matrix[i])
            else:
                raise MatrixTypeError
        except MatrixTypeError:
            print('Некорретно введено значение передаваемого параметра(int, Matrices)')
        except MatrixSizeError:
            print("Матрицы нельзя умножить,т.к. кол-во эл. в столбце 1-ой, не соотв. кол-ву эл. строк во 2-ой")

    def transpon_matrix(self):
        matrix = [[0*j*i for j in range(self.cnt_lines)] for i in range(self.cnt_columns)]
        for i in range(self.cnt_columns):
            for j in range(self.cnt_lines):
                matrix[i][j] = self.matrix[j][i]
            print(matrix[i])

    def exponentation_matrix(self, num):
        try:
            if self.__eq__(self):
                object_new = copy.copy(self)
                for i in range(num - 1):
                    print(f"{i + 1}-й шаг:")
                    object_new.matrix = self.__mul__(object_new)
                print("Результат возведения в степень")
                object_new.show_matrix()
            else:
                raise MatrixSizeError
        except MatrixSizeError:
            print("Чтобы возвести матрицу в степень, она должна быть квадратной!")

    def __eq__(self, other):
        return isinstance(self, Matrices) and\
            isinstance(other, Matrices) and\
            self.cnt_columns == other.cnt_columns and\
            self.cnt_lines == other.cnt_lines

    def write_matrix_file(self):
        file = open(f"{random.randint(0, 10000)} matrix.txt", 'a')
        file.write(str(self.cnt_lines) + ' ' + str(self.cnt_columns) + '\n')
        for i in range(self.cnt_lines):
            for j in range(self.cnt_columns):
                file.write(str(self.matrix[i][j]) + ' ')
            file.write('\n')
        file.close()

