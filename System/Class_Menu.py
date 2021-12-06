from abc import ABC
from Entity.Class_Matrix import Matrices
from System.Class_Menu_Except import *


class Menu(ABC):
    action = int

    @staticmethod
    def main_menu():
        print("1. Сложение матриц")
        print("2. Вычитание матриц")
        print("3. Умножение матриц")
        print("4. Транспонирование матриц")
        print("5. Умножение матриц на число")
        print("6. Возведение в степень")
        print("0. Выход")

    @staticmethod
    def input_matrix():
        print("Введите количество строк матрицы:")
        cnt_lines = correct_int()
        print("Введите количество столбцов матрицы:")
        cnt_columns = correct_int()
        matrix = Matrices(cnt_lines, cnt_columns)
        print(f"Введите матрицу:")
        matrix.write_matrix()
        return matrix

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
                Menu.action_matrix_degree()
            elif action == 0:
                break
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
    def action_transpose():
        matrix = Menu.input_matrix()
        matrix.transpon_matrix()

    @staticmethod
    def action_addition():
        print("Введите матрицы, которые вы хотите сложить:")
        matrix1 = Menu.input_matrix()
        matrix2 = Menu.input_matrix()
        matrix1 + matrix2

    @staticmethod
    def action_subtraction():
        print("Введите матрицы, которые вы хотите вычесть друг из друга:")
        matrix1 = Menu.input_matrix()
        matrix2 = Menu.input_matrix()
        matrix1 - matrix2

    @staticmethod
    def action_multiplication():
        matrix1 = Menu.input_matrix()
        matrix2 = Menu.input_matrix()
        matrix1 * matrix2

    @staticmethod
    def action_mul_constant():
        matrix1 = Menu.input_matrix()
        print("Введите число, на которое умножается матрицы")
        number = correct_int()
        matrix1 * number

    @staticmethod
    def action_matrix_degree():
        matrix = Menu.input_matrix()
        print("Введите степень, в которую возводим матрицу")
        number = correct_int()
        matrix.exponentation_matrix(number)

