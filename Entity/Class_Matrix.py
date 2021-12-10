import copy
import random

from System.Class_Menu_Except import *
from Entity.Class_Matrix_Except import *


class Matrices:
    def __init__(self, cnt_lines, cnt_columns):
        self.cnt_lines = cnt_lines
        self.cnt_columns = cnt_columns
        self.matrix = Matrices.null_matrix(cnt_lines, cnt_columns)

    def show_matrix(self):
        for i in self.matrix:
            print(i)

    def write_matrix(self):
        for i in range(self.cnt_lines):
            self.matrix[i] = correct_int_list(self.cnt_columns)

    def __add__(self, other):
        if self.__eq__(other):
            matrix = Matrices.null_matrix(self.cnt_lines, self.cnt_columns)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        else:
            raise MatrixSizeError

    def __sub__(self, other):
        if self.__eq__(other):
            matrix = Matrices.null_matrix(self.cnt_lines, self.cnt_columns)
            for i in range(self.cnt_lines):
                for j in range(self.cnt_columns):
                    matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return matrix
        else:
            raise MatrixSizeError

    def __mul__(self, other):
        list_matrix = Matrices.null_matrix(self.cnt_lines, other.cnt_columns)
        if not isinstance(other, Matrices) or self.cnt_columns != other.cnt_lines:
            raise MatrixMulError
        else:
            for i in range(self.cnt_lines):
                for j in range(other.cnt_columns):
                    for k in range(self.cnt_columns):
                        list_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return list_matrix

    def mul_on_constant(self, number):
        list_matrix = self.null_matrix(self.cnt_lines, self.cnt_columns)
        for i in range(self.cnt_lines):
            for j in range(self.cnt_columns):
                list_matrix[i][j] = self.matrix[i][j] * number
        return list_matrix

    def transpon_matrix(self):
        matrix = Matrices.null_matrix(self.cnt_columns, self.cnt_lines)
        for i in range(self.cnt_columns):
            for j in range(self.cnt_lines):
                matrix[i][j] = self.matrix[j][i]
        return matrix

    def exponentation_matrix(self, number):
        if self.__eq__(self):
            other = copy.copy(self)
            for i in range(number - 1):
                other.matrix = self * other
            return other.matrix
        else:
            raise MatrixMulError

    def __eq__(self, other):
        return isinstance(other, Matrices) and\
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

    @staticmethod
    def null_matrix(cnt_lines, cnt_columns):
        matrix = [[0*j*i for j in range(cnt_columns)] for i in range(cnt_lines)]
        return matrix
