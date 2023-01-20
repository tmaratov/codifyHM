number = input('Введите натуральное число: ')
number_list = []
for i in number:
    number_list.append(i)
    # print(len(number_list))
    # print(max(number_list))
print(sorted(number_list))
print(max(number_list))
count = len(number_list)

for i in range(count):
    for j in range(count - i - 1):
        number_list[j] > number_list[j + 1]
        temp = number_list[j]
        number_list[j] = number_list[j + 1]
        number_list[j + 1] = temp
