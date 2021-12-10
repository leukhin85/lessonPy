def correct_int():
    while True:
        try:
            number = int(input())
            break
        except ValueError:
            print("""Некорректно введенное число.\
            Попробуйте снова ввести без пробелов и иных символов!""")
    return number


def correct_int_list(len_list):
    while True:
        try:
            list_values = str(input()).split()
            if len(list_values) == len_list:
                list_values = [int(el) for el in list_values]
            else:
                raise ValueError
            break
        except ValueError:
            print("Требуется ввести строку из целых чисел через пробел!")
            print(f"Количество элементов в строке должно быть равно: {len_list}")
    return list_values
