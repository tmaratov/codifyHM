# 1.Список

s = [2, 45, 3, 56, 43, 42, 23, 72, 37, 3]

# Вывести первый и последний элемент в списке
print('Вывести первый и последний элемент в списке = ' +
      str(s[0]),  str(s[-1]))

# Вывести количество элементов в списке
print('Вывести количество элементов в списке = ' + str(len(s)))

# Добавить в конец списка число
s.append(59)
print(s)

# Удалить с конца списка число
s.pop(-1)
print(s)

# Добавить в начало списка число
s.insert(0, 5)
print(s)

# Удалить с начала списка число
s.pop(0)
print(s)

# Добавить в 3 индекс списка число 35
s.insert(3, 35)
print(s)

# 2.Кортеж
# Кортежи как и List, но их нельзя изменить.

# 3. Множества
e = {'Tom', 'Michael', 'Mason', 'Alexander',
     'William', 'Anderson', 'Calvin', 'David'}
x = {'Elliot', 'William', 'David', 'Harry',
     'James', 'Alexander', 'Calvin', 'Kurt'}

# Пересечение
print(set.intersection(e, x))

# Симметрическую разность
print(set.symmetric_difference(e, x))

# Обьединение
# e.update(x)
# print(e)

# Разность
e.difference_update(x)
print(e)

# Словарь
cars = []
car_1 = {
    'Name': 'Jorgo',
    'Manufactured year': 2022,
    'Mileage': '1 km',
    'Color': 'White',
    'Body type': 'Sedan',
    'Country': 'Kyrgyzstan',
    'Number': 'kg01uno111'
}

car_2 = {
    'Name': 'BMW',
    'Manufactured year': 2022,
    'Mileage': '1 km',
    'Color': 'Blue',
    'Body type': 'Sedan',
    'Country': 'Germany',
    'Number': 'kg01BMW039'
}
cars.append(car_1)
cars.append(car_2)
print(cars)
