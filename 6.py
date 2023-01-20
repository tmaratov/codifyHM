import datetime

b = datetime.datetime.today() + datetime.timedelta(1)
b = b.strftime("%d-%m-%Y ")


def try_to_choose():
    try:
        choose = int(input('Choose your flight. (1, 2, 3, 4): '))
        print('------------------------------')

    except:
        print('Please, write number between 1 and 4!')
        return try_to_choose()

    if choose == 1:
        info(choose)

    elif choose == 2:
        info(choose)

    elif choose == 3:
        info(choose)

    elif choose == 4:
        info(choose)

    else:
        print('You wrote wrong number. Please, write number between 1 and 4!.')
        return try_to_choose()


def info(choose):
    print(
        f'You have chosen flight #{choose}. Fligth:', flights[choose]['Where'])
    price = int(flights[choose]['Price'])
    print(f'You need to pay {price} som\n')

    try:
        pay = int(input('Pay here >>> '))
    except:
        print('\nYou can not pay with letters or something else!!')
        print('------------------------------')
        print('******************************\n')
        return info(choose)

    if pay < price:
        left = price - pay
        print(f'\nNot enought! Sorry we don"t sell to you this ticket...')
        print('Try again')
        print('------------------------------')
        print('******************************\n')
        return info(choose)
    elif pay > price:
        left = pay - price
        print(f'\nTake change {left} som.\n')
        nice(choose)

    else:
        print('Good!')
        nice(choose)

    print('------------------------------')


def nice(choose):
    print('------------------------------')
    print('Your Tiket')
    print('------------------------------')
    print('Fligth: ', flights[choose]['Flight'])

    print('Name, Surname: ' + name, flights[choose]
          ['Where'], flights[choose]['Time'], sep='\n')

    print('\nHave a nice flight!')
    print('------------------------------')


flights = {
    1:
        {
            'Flight': 'TK 347',
            'Where': 'Bishkek - Istambul',
            'Time': b + '03:40',
            'Price': '34907'
        },
    2:
        {
            'Flight': 'G9 354',
            'Where': 'Bishkek - Sharjah',
            'Time': b + '04:20',
            'Price': '19068'
        },
    3:
        {
            'Flight': 'FZ 1462',
            'Where': 'Bishkek - Dubai',
            'Time': b + '05:40',
            'Price': '38680'
        },
    4:
        {
            'Flight': 'SU 1883',
            'Where': 'Bishkek - Moskow',
            'Time': b + '06:05',
            'Price': '26593'
        }
}
print('------------------------------')

for key, values in flights.items():
    for i in values:
        print(i + ': ' + values[i])
    print('------------------------------')

print('------------------------------')
print('------------------------------')


while True:
    pay = 0
    price = 0
    try:
        name = input('Write your Name, Surname: ')
        if name.isdigit():
            print('Please write your name.')
            continue
    except KeyboardInterrupt:
        print('Please try again!')
        continue

    try_to_choose()
    break
