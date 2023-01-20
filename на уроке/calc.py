
print('Здравствуйте, это калькулятор!\n ВЫберите действие (+, - , / , *):')
a = input('')
b = input('Выберите первую цифру: ')
c = input('Выберите вторую цифру: ')

while True:

    if not b.isdigit:
        b = input('Введите первую цифру пожалуйста')
        continue

    elif not c.isdigit:
        c = input('Введите вторуб цифру пожалуйста')
        continue

    if a == '+':
        d = float(b) + float(c)
        print(f'Ваш ответ: {b} + {c} = {d}')

    elif a == '/':
        d = float(b) / float(c)
        print(f'Ваш ответ: {b} / {c} = {d}')

    elif a == '-':
        d = float(b) - float(c)
        print(f'Ваш ответ: {b} - {c} = {d}')

    elif a == '*':
        d = float(b) * float(c)
        print(f'Ваш ответ: {b} * {c} = {d}')
