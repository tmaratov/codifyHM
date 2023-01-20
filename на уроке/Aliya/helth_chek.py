# Написать функцию is_alive(health), которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, то функция возвращает False, в противном случае True.
def is_alive():
    try:
        helth = int(input('helth>>> '))
    except:
        print('Пиши цифру')
        return is_alive()

    if helth <= 0:
        print(False)
    else:
        print(True)


is_alive()
