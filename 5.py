# # Первое задание
# # def sum_range(start, end):
# #     sum_of_numbers = []

# #     for number in range(start, end):
# #         sum_of_numbers.append(number)
# #     return (sum(sum_of_numbers))


# # while True:
# #     start = int(input('> Первое число: '))
# #     end = int(input('> Второе число: '))

# #     if start < end:
# #         end = end + 1
# #         print(sum_range(start, end))

# #     elif start > end:
# #         temp = start + 1
# #         start = end
# #         end = temp
# #         print(sum_range(start, end))

# #     else:
# #         print('Введите не похожие числа!')
# #         continue

# #     a = input('Хотите продолжить? (y/n) > ')
# #     if a == 'y':
# #         continue
# #     break
# # print('---------------------')
# # print('---------------------')
# # Второе задание

# # def date(d, m, y):
# #     if d <= 0 or m <= 0 or y <= 0:
# #         return False
# #     else:
# #         mounth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# #         if y % 4 == 0:
# #             mounth[1] = 29
# #         if d <= mounth[m-1]:
# #             if m <= 12:
# #                 return True
# #         return False


# # d = int(input('> Day: '))
# # m = int(input('> Month: '))
# # y = int(input('> Year: '))
# # print(date(d, m, y))
# # print('---------------------')
# # print('---------------------')

# # Третье задание

# # def is_prime(x):

# #     if x in range(0, 1001):
# #         return True
# #     else:
# #         return False


# # x = input('> Введи число: ')
# # print(is_prime(x))
# # print('---------------------')
# # print('---------------------')

# # Четвертое задание
# # import math


# # def squer(x):
# #     a = (4, 2, (math.sqrt(2)))
# #     print(f'Периметр: {x*a[0]}')
# #     print(f'Площадь: {x**a[1]}')
# #     print(f'Диагональ: {x*a[2]}')
# #     return f'Вы ввели число: {x}'


# # x = int(input('> '))
# # print(squer(x))
# # print('---------------------')
# # print('---------------------')

# # Пятое задание
# # def is_year_leap(year):
# #     if year % 4 == 0:
# #         print('True')
# #     else:
# #         print('False')


# # year = int(input('Сейчас мы узнаем высокостный ли год. Введите любой год: '))
# # is_year_leap(year)
# # print('---------------------')
# # print('---------------------')

# # Шестое задание

# # def sum(number1, number2) -> float:
# #     ans = number1 + number2
# #     return ans


# # def sub(number1, number2) -> float:
# #     ans = number1 - number2
# #     return ans


# # def mult(number1, number2) -> float:
# #     ans = number1 * number2
# #     return ans


# # def div(number1, number2) -> float:
# #     ans = number1 / number2
# #     return ans


# # print('Это калькулятор!')
# # print('---------------------')


# # operation_list = ('+', '-', '*', '/')

# # while True:
# #     number1 = input('> Ведите первое число: ')
# #     number2 = input('> Ведите второе число: ')
# #     if not number1.isdigit() or not number2.isdigit():
# #         print('Введите числа!')
# #         continue
# #     operation = input('> Введите какую будете вести операцию(+,-,*,/): ')
# #     print('---------------------')

# #     if not operation in operation_list:
# #         print('Неизвестная операция!')
# #         continue

# #     if operation in operation_list:
# #         if operation == '+':
# #             print(sum(float(number1), float(number2)))

# #         elif operation == '-':
# #             print(sub(float(number1), float(number2)))
# #         elif operation == '*':
# #             print(mult(float(number1), float(number2)))
# #         elif operation == '/':
# #             print(div(float(number1), float(number2)))

# #     want_to_continue = input('Хотите повторить операцию(y/n): ')

# #     if want_to_continue == 'y':
# #         continue
# #     else:
# #         break
# # print('---------------------')
# # print('---------------------')

# # Седьмое задание

# def bank(a, years):
#     income = a
#     for year in range(0, years):

#         income += income * 0.1
#     print(f'Через {years} года/лет у вас будет {income} денег!')


# while True:
#     a = input('Какую сумму вы хотите вложить в банк: ')
#     years = input('На сколько лет: ')
#     print('---------------------')
#     if not a.isdigit() and not years.isdigit():
#         print('Вводите числа!!')
#         continue
#     if float(a) < 0:
#         print('Вы не можете вложить ничего!')
#         continue
#     if int(years) < 0:
#         print('Вы не можете вложить на 0 или меньше лет!!!')
#         continue

#     bank(float(a), int(years))
#     print('---------------------')
#     repeat = input(
#         'Хотите посчитать еще? Введите "y" что бы продолждить и "n" что бы отменить: ')
#     if repeat == 'y':
#         continue

#     break
