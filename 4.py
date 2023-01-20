# первое задание
while True:
    name = input('Поажалуйста введите своё имя: ').lower()

    if name == 'нурсултан':
        print(f"""
    Здравтвуйте {name.title()}! Вы попали на страницу ментора!
    На этой странице вы можете просмотреть домашние задание студентов!
        """)

    elif name == 'вероника':
        print(f"""
    Здравтвуйте {name.title()}! Вы попали на страницу ментора!
    На этой странице вы можете просмотреть домашние задание студентов!
        """)

    else:
        print(f"""
    Привет, {name.title()}!
    Вы попали на страницу студента!
    На этой странице Вы можете отправить домашнее задание
        """)

    choise = input('Если хотите продолжить нажмите y - да или n - нет: ')
    if not choise in ('y', 'n'):
        break

    if choise == 'y':
        continue

    if choise == 'n':
        break


# второе задание


countries = ['America', 'Great britain', 'France',
             'Argentina', 'Poslka', 'Itlay', 'Zambia']
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)

countries.reverse()
print(countries)
countries.reverse()
print(countries)

countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
