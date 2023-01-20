# 1 задание

var_int = 10
var_float = 8.4
var_str = "No"
var_big = var_int * 3.5
var_float = 8.4 - 1

a = var_int / float(var_float)
b = var_big / float(var_float)

var_str = var_str * 2 + "Yes" * 3

print(var_big, var_float, a, b, var_str)

# 2 задание
# по математически выполняется сначала степень, потом слева на право умножение затем деление, минус потом плюс
c = 11 * 2 ** 2 - 13 / 4 + 7
print(c)

# 3 задание

s = 'py'
t = 'th'
u = 'on'

print(f"{s}{t}{u}")

# 4 задание

b = 'Python is one of the most popular programming languages today and is easy for beginners'
print(len(b))
