import copy
import random


class Matrices:
    def __init__(self, cntlines, cntcolumns):
        self.cntlines = cntlines
        self.cntcolumns = cntcolumns
        self.matrix = [[0 for _ in range(cntcolumns)] for _ in range(cntlines)]

    def ShowMatrix(self):
        for i in self.matrix:
            print(i)

    def writeMatrix(self):
        print(f"\nВведите матрицу:")
        list = self.matrix.copy()
        for i in range(self.cntlines):
            print(f"Введите {i + 1} строку:")
            expectation = False
            for j in range(self.cntcolumns):
                try:
                    expectation = False
                    list[i][j] = int(input())
                except ValueError:
                    print("Требуется целочисленное значение. Введите матрицу заново!")
                    expectation = True
                    self.writeMatrix()
                    break
            if expectation:
                break
        self.matrix = list

    def __add__(self, other):
        if (self.cntlines == other.cntlines) and \
                (self.cntcolumns == other.cntcolumns):
            list = [[0 for _ in range(self.cntcolumns)] for _ in range(self.cntlines)]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    list[i][j] = self.matrix[i][j] + other.matrix[i][j]
                print(list[i])
        else:
            print("Ошибка! Кол-во столбцов и строк в матрицах не совпадает!")

    def __sub__(self, other):
        if (self.cntlines == other.cntlines) and \
                (self.cntcolumns == other.cntcolumns) and \
                (isinstance(other, Matrices)):
            list = [[0 for _ in range(self.cntcolumns)] for _ in range(self.cntlines)]
            for i in range(self.cntlines):
                for j in range(self.cntcolumns):
                    list[i][j] = self.matrix[i][j] - other.matrix[i][j]
                print(list[i])
            return list
        else:
            print("Вычитание матриц невозможно осуществить, так как кол-во строк и столбцов в них разное!")

    def mulOnConstant(self):
        expectation = True
        num = 0
        while expectation:
            try:
                expectation = False
                num = int(input("Введите целое число: "))
            except ValueError:
                expectation = True
                print("Требуется целочисленное значение. Введите число заново!")
        list = [[0 for _ in range(self.cntcolumns)] for _ in range(self.cntlines)]
        for i in range(self.cntlines):
            for j in range(self.cntcolumns):
                list[i][j] = self.matrix[i][j] * num
            print(list[i])

    def __mul__(self, other):
        exception = True
        list = [[0 for _ in range(other.cntcolumns)] for _ in range(self.cntlines)]
        if isinstance(other, Matrices) and (self.cntcolumns == other.cntlines):
            exception = False
            for i in range(self.cntlines):
                for j in range(other.cntcolumns):
                    for k in range(self.cntcolumns):
                        list[i][j] += self.matrix[i][k] * other.matrix[k][j]
                print(list[i])
            return list
        else:
            # Если кол-во строк одной матрицы не равно кол-ву столбцов другой, то здесь матрицы меняются местами и
            # метод выполняется снова
            print('Матрицы нельзя умножить,т.к. кол-во эл. в столбце 1-ой матрицы, не соотв. кол-ву эл. во 2-ой')

    def TransponMatrix(self):
        list = [[0 for _ in range(self.cntlines)] for _ in range(self.cntcolumns)]
        for i in range(self.cntcolumns):
            for j in range(self.cntlines):
                list[i][j] = self.matrix[j][i]
            print(list[i])

    def ExponentationMatrix(self):
        expectation = True
        num = 0
        while expectation:
            try:
                expectation = False
                num = int(input("Введите целое число, в качестве степени: "))
            except ValueError:
                expectation = True
                print("Требуется целочисленное значение. Введите число заново!")
        if self.cntlines == self.cntcolumns:
            object = copy.copy(self)
            for i in range(num - 1):
                print(f"{i + 1}-й шаг:")
                object.matrix = self.__mul__(object)
            print("Результат возведения в степень")
            object.ShowMatrix()
        else:
            print("Чтобы возвести матрицу в степень, она должна быть квадратной!")

    def WriteMatrixToFile(self):
        file = open(f"{random.randint(0, 10000)} matrix.txt", 'a')
        file.write(str(self.cntlines) + ' ' + str(self.cntcolumns) + '\n')
        for i in range(self.cntlines):
            for j in range(self.cntcolumns):
                file.write(str(self.matrix[i][j]) + ' ')
            file.write('\n')
        file.close()

    def writing_from_file(self):
        pass

# наш скрипт


if __name__ == '__main__':

    matrix1 = Matrices(3, 3)
    matrix1.writeMatrix()
    matrix2 = Matrices(3, 3)
    matrix2.writeMatrix()
    print("Матрица №1:")
    matrix1.ShowMatrix()
    print("Матрица №2:")
    matrix2.ShowMatrix()
    print("\nМетод умножения функции на число:")
    matrix1.mulOnConstant()
    print("\nМетод сложения матриц:")
    matrix2 + matrix1
    print("\nМетод разности матриц:")
    matrix2.__sub__(matrix1)
    print("\nМетод умножения матриц друг на друга:")
    matrix2 * matrix1
    print("\nсмена матриц друг на друга в этом же методе")
    matrix1 * matrix2
    print("\nМетод возведения матрицы в степень:")
    matrix1.ExponentationMatrix()
    print("Проверка на изменение начальных матриц:")
    print("Матрица №1:")
    matrix1.ShowMatrix()
    print("Матрица №2:")
    matrix2.ShowMatrix()
    print("Начальные матрицы остались неизмененными после выполнения действий с ними.")
    matrix1.WriteMatrixToFile()