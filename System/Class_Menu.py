from abc import ABC

from Entity.Class_Matrix import *
from System.Class_Menu_Except import *


def list_output(list_):
    if isinstance(list_, list):
        for i in list_:
            print(i)


class Menu(ABC):
    action = int

    @staticmethod
    def main_menu():
        print("1. Сложение матриц")
        print("2. Вычитание матриц")
        print("3. Умножение матриц")
        print("4. Транспонирование матриц")
        print("5. Умножение матриц на число")
        print("6. Возведение матрицы в степень")
        print("0. Выход")

    # size_matrix = [<кол-во строк>,<кол-во столбов>]
    @staticmethod
    def input_matrix():
        object_matrix = object
        while True:
            try:
                print("Введите размер матрицы: <кол-во_строк> <кол-во_столбцов>:")
                size_matrix = correct_int_list(2)
                count_lines = size_matrix[0]
                count_columns = size_matrix[1]
                if (count_lines == 0 and count_columns != 0) or \
                        (count_columns == 0 and count_columns != 1) or \
                        (count_lines == count_columns == 0):
                    raise ValueError
                if count_lines*count_columns >= 30:
                    print("Размер матрицы слишком велик. Правильно ли вы ввели данные?(y/n)")
                    if str(input()) != 'y':
                        print("Попробуйте снова!")
                        continue
                object_matrix = Matrices(count_lines, count_columns)
                print("Введите матрицу:")
                object_matrix.write_matrix()
                break
            except ValueError:
                print("Введите размер матрицы снова, т.к. один из размеров равен нулю.")
        return object_matrix

    @staticmethod
    def action_menu():
        while True:
            Menu.main_menu()
            print("Введите номер действия: ")
            action = correct_int()
            if action == 1:
                Menu.action_addition()
            elif action == 2:
                Menu.action_subtraction()
            elif action == 3:
                Menu.action_multiplication()
            elif action == 4:
                Menu.action_transpose()
            elif action == 5:
                Menu.action_mul_constant()
            elif action == 6:
                Menu.action_exponentiation()
            elif action == 0:
                break
            else:
                print("Нет такого действия!")
            print("Хотите вернуться в главное меню?(y/n)")
            flag = str(input())
            if flag == 'y':
                continue
            elif flag == 'n':
                break
            else:
                print("Вы не ввели символы 'y' или 'n', поэтому вы были переведеы в главное меню.")
                continue

    @staticmethod
    def action_addition():
        print("Введите матрицы, которые будут сложены:")
        matrix1 = Menu.input_matrix()
        matrix2 = Menu.input_matrix()
        try:
            list_output(matrix1 + matrix2)
        except MatrixSizeError:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    @staticmethod
    def action_subtraction():
        print("Введите матрицы, которые будут вычитаться:")
        matrix1 = Menu.input_matrix()
        matrix2 = Menu.input_matrix()
        try:
            list_output(matrix1 - matrix2)
        except MatrixSizeError:
            print("Вычитание матриц невозможно осуществить, так как кол-во строк и столбцов в них разное!")

    @staticmethod
    def action_multiplication():
        print("Введите матрицы, которые умножатся друг на друга:")
        matrix1 = Menu.input_matrix()
        matrix2 = Menu.input_matrix()
        try:
            list_output(matrix1 * matrix2)
        except MatrixMulError:
            print("Матрицы нельзя умножить, так как кол-во столбцов 2 матрицы не соответствует кол-ву строк первой:")

    @staticmethod
    def action_transpose():
        print("Введите матрицу для транспонирования:")
        matrix = Menu.input_matrix()
        list_output(matrix.transpon_matrix())

    @staticmethod
    def action_mul_constant():
        print("Введите матрицу, которая умножится на число:")
        matrix = Menu.input_matrix()
        print("Введиет число, на которое уможается матрица:")
        number = correct_int()
        list_output(matrix.mul_on_constant(number))

    @staticmethod
    def action_exponentiation():
        print("Введите матрицу, которая будет возведена в степень")
        matrix = Menu.input_matrix()
        print("Введите степень возводимой матрицы:")
        number = correct_int()
        try:
            list_output(matrix.exponentation_matrix(number))
        except MatrixSquareError:
            print("Чтобы возвести матрицу в степень, она должна быть квадратной!")
        except MatrixMulError:
            print("Чтобы возвести матрицу в степень, кол-во столбцов должно быть равно")
