import copy
import random
from System.Class_Menu_Except import *


class Matrices:
    def __init__(self, cnt_lines, cnt_columns):
        self.cnt_lines = cnt_lines
        self.cnt_columns = cnt_columns
        self.matrix = [[0 for _ in range(cnt_columns)] for _ in range(cnt_lines)]

    def show_matrix(self):
        for i in self.matrix:
            print(i)

    def write_matrix(self):
        print(f"\nВведите матрицу:")
        matrix = self.matrix.copy()
        for i in range(self.cnt_lines):
            print(f"Введите {i + 1} строку:")
            expectation = False
            for j in range(self.cnt_columns):
                try:
                    expectation = False
                    matrix[i][j] = correct_int()
                except ValueError:
                    print("Требуется целочисленное значение. Введите матрицу заново!")
                    expectation = True
                    self.write_matrix()
                    break
            if expectation:
                break
        self.matrix = matrix

    def __add__(self, other):
        if (self.cnt_lines == other.cnt_lines) and \
                (self.cnt_columns == other.cnt_columns):
            matrix = [[0 for _ in range(self.cnt_columns)] for _ in range(self.cnt_lines)]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                print(matrix[i])
        else:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def __sub__(self, other):
        if (self.cnt_lines == other.cnt_lines) and \
                (self.cnt_columns == other.cnt_columns) and \
                (isinstance(other, Matrices)):
            matrix = [[0 for _ in range(self.cnt_columns)] for _ in range(self.cnt_lines)]
            for i in range(self.cnt_lines):
                for j in range(self.cnt_columns):
                    matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
                print(matrix[i])
            return matrix
        else:
            print("Вычитание матриц невозможно осуществить, так как кол-во строк и столбцов в них разное!")

    def __mul__(self, other):
        if isinstance(other, Matrices):
            matrix = [[0 for _ in range(other.cnt_columns)] for _ in range(self.cnt_lines)]
            if isinstance(other, Matrices) and (self.cnt_columns == other.cnt_lines):
                for i in range(self.cnt_lines):
                    for j in range(other.cnt_columns):
                        for k in range(self.cnt_columns):
                            matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                    print(matrix[i])
                return matrix
            else:
                print('Матрицы нельзя умножить,т.к. кол-во эл. в столбце 1-ой матрицы, не соотв. кол-ву эл. во 2-ой')
        elif isinstance(other, int):
            matrix = [[0 for _ in range(self.cnt_columns)] for _ in range(self.cnt_lines)]
            for i in range(self.cnt_lines):
                for j in range(self.cnt_columns):
                    matrix[i][j] = self.matrix[i][j] * other
                print(matrix[i])

    def transpon_matrix(self):
        matrix = [[0 for _ in range(self.cnt_lines)] for _ in range(self.cnt_columns)]
        for i in range(self.cnt_columns):
            for j in range(self.cnt_lines):
                matrix[i][j] = self.matrix[j][i]
            print(matrix[i])

    def exponentation_matrix(self):
        expectation = True
        num = 0
        while expectation:
            try:
                expectation = False
                num = int(input("Введите целое число, в качестве степени: "))
            except ValueError:
                expectation = True
                print("Требуется целочисленное значение. Введите число заново!")
        if self.cnt_lines == self.cnt_columns:
            object_new = copy.copy(self)
            for i in range(num - 1):
                print(f"{i + 1}-й шаг:")
                object_new.matrix = self.__mul__(object_new)
            print("Результат возведения в степень")
            object_new.show_matrix()
        else:
            print("Чтобы возвести матрицу в степень, она должна быть квадратной!")

    def write_matrix_file(self):
        file = open(f"{random.randint(0, 10000)} matrix.txt", 'a')
        file.write(str(self.cnt_lines) + ' ' + str(self.cnt_columns) + '\n')
        for i in range(self.cnt_lines):
            for j in range(self.cnt_columns):
                file.write(str(self.matrix[i][j]) + ' ')
            file.write('\n')
        file.close()
