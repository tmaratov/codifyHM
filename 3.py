# первое задание

list_3 = []
list_2 = []
list_cube = []

for a in range(0, 31):
    if a % 3 == 0:
        list_3.append(a)
print(list_3)

for b in range(0, 1001):
    if b % 2 == 0:
        list_2.append(b)
print(sum(list_2))


for c in range(1, 11):
    list_cube.append(c)
cube = []
for d in list_cube:
    cube.append(d*d*d)

print(cube)

# второе задание
# 1
dinner = ['Natasha Romanov', 'Riri Williams', 'Gwen Stacy']

for name in dinner:
    print('Привет ' + name + '! Хочу тебя пригласить на ужин в это воскресенье.')

print(dinner[1] + ' к ожалению придти не сможет')
# 2
dinner[1] = 'Mary Jane'
for name in dinner:
    print('Привет ' + name + '! Хочу тебя пригласить на ужин в это воскресенье.')
# 3
print('Список гостей расширяется!')
dinner.insert(0, 'Wanda Maximoff')
dinner.insert(2, 'Monica Rambeau')
dinner.append('America Chavez')
for name in dinner:
    print('Привет ' + name + '! Хочу тебя пригласить на ужин в это воскресенье.')
# 4
print('К сожалению стол привезти не успели! Приглашаются только 2 гостя.')
count = len(dinner)
print(str(count) + ' - это много, надо уменьшить список')

while len(dinner) >= 3:
    print(dinner.pop(-1) + ' я очень сожалею об отмене приглашения.')

for name in dinner:
    print('Привет ' + name + '! Ужин в воскресенье остается в силе.')

del dinner[:]

print(dinner)
