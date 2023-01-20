
number = 345276
result = []

for a in str(number):
    if int(a) % 2 != 0:
        result.append(a)
print(result)

print(int(result[0] + result[1] + result[2]))

f = 5 % 2
print(f)
