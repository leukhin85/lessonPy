def correct_int():
    while True:
        try:
            number = int(input())
            break
        except ValueError:
            print("""Некорректно введенное число.\
            Попробуйте снова ввести без пробелов и иных символов!""")
    return number

# Обработка корректного ввода списка целых чисел определенной длины.
# def correct_int_list(length_of_list):
#     while True:
#         try:
#             str_ = str(input())
#             our_list = str_.split()
#             for i, el in our_list:
#                 el = int(our_list[i])
#             if len(our_list) == length_of_list:
#                 break
#         except ValueError:
#             print("""Некорректно введен список целых чисел.\
#             Попробуйте снова ввести в строчку через пробел!""")
#     return our_list
