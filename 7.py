# 1.1

# while True:
#     try:
#         g = input('>> enter gramms: ')
#         if not g.isdigit():
#             print('Введите число')
#             continue
#     except ValueError:
#         print('Число введите')
#         continue

#     if g == 0:
#         kg = g

#     else:
#         kg = int(g) / 1000

#     print(f'{kg} kg')
#     break

# 1.2 Даны две переменные x = 10 и y = 55. Поменяйте их значения местами. Выведите значения переменных на экран до и после замены.

# x = 10
# y = 55

# print(x, y)

# t = x
# x = y
# y = t
# print(x, y)

# 1.3 С клавиатуры вводится расстояние L в метрах. Необходимо найти и вывести на экран количество полных километров в нем.

# while True:
#     try:
#         L = input('>> enter meters: ')
#         if not L.isdigit():
#             print('Введите число')
#             continue
#     except ValueError:
#         print('Число введите')
#         continue

#     if L == 0:
#         km = L

#     else:
#         km = int(L) // 100

#     print(f'{km} km')
#     break

# 1.4

# m = input('>> ')
# list_1 = [*m]
# list_1.reverse()
# print(''.join(list_1))

# 1.5
# import datetime

# d = datetime.datetime.today()
# b = datetime.datetime.today().strftime("%d-%m-%Y")

# print(d, '\n', b)

# 2.1
# while True:
#     try:
#         x = int(input('>> Please 1st value: '))
#         y = int(input('>> Please 2nd value: '))
#         z = int(input('>> Please 3rd value: '))

#     except ValueError:
#         print('please enter digit')
#         continue

#     if x > 80 or y > 80 or z > 80:
#         print(True)
#     else:
#         False
#     break

# 2.2
# while True:
#     try:
#         x = int(input('>> Please 1st value: '))
#         y = int(input('>> Please 2nd value: '))

#     except ValueError:
#         print('please enter digit')
#         continue

#     if x > 0 and y > 0:
#         print(True)
#     elif x < 0 and y < 0:
#         print(True)
#     else:
#         print(False)
#     break

# 2.3
# x = 130
# y = 25
# z = 70
# if x < y and x < z:
#     print(x)
# elif y < x and y < z:
#     print(y)
# elif z < x and z < y:
#     print(z)

# 3.1
# text = 'Python - это Питон!'
# a = []
# for letter in text:
#     a.append(letter)
# print(len(a))

# 3.2
# num = [1, '2', 3, 4, '5']
# summ = 0
# for e in num:
#     e = int(e)
#     summ += e

# print(summ)

# # 3.3
# b = 'bad_cat_23'
# list_b = [*b]
# list_a = [*'abcde123']

# for letters in list_a:
#     if letters in list_b:
#         print(f'{letters} exist in {b} ')
#     elif not letters in list_b:
#         print(f'{letters} not exist in {b} ')

# 3.4

# for i in range(2, 15):
#     if i % 2 == 0:
#         for j in range(2, 15):
#             print('/ \_', end='')
#     else:
#         for j in range(2, 15):
#             print('\_/ ', end='')
#     print('')

# # 3.5

# print(
#     ' ____+____________________________________________________________________________')
# print(' | x |  ', end='')
# for f in range(1, 10):
#     print(f, end=' \t ')

# print('|')
# print(' ____+____________________________________________________________________________')
# for i in range(1, 10):
#     print(' |', i, end=' | \t')
#     for j in range(1, 10):
#         print(j*i, end=' \t ')
#     print('|')
# print(' ____+____________________________________________________________________________')

# 4.1
import secrets

letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
sym = '!@#$%^&'


def gen():
    try:
        length = int(input('>> input lenght of pass: '))
        count = int(input('>> how many passwords generate? '))
    except ValueError:
        print('Type number')
        return gen()

    all_pass = letters + capital_letters + num + sym

    for i in range(count):
        password = ''.join(secrets.choice(all_pass) for i in range(length))
        print(password)


gen()
