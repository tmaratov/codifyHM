# Напишите функцию, которая принимает строку и вычисляет количество букв верхнего и нижнего регистра

a = input('>>> ')
b = [*a]

letters = 'qwertyuiopasdfghjklzxcvbnm'
small = []
big = []
small_count = []
big_count = []

for z in letters:
    small.append(z)

for i in small:
    big.append(i.upper())

small_count = (set(a).intersection(set(small)))
big_count = (set(a).intersection(set(big)))


print(f'Здесь маленьких букв {len(small_count)} и больших {len(big_count)}')
