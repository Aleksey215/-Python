# Вывести сумму цифр введенного числа
# num = list(map(int, input("Enter number: ")))
# print(sum(num))
# print()

# Даны два катета a, b. Вывести гипотенузу треугольника.
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# hep = (a ** 2 + b ** 2) ** 0.5
# print(round(hep, 2))
# print()

# Альтернативный способ ввода переменных с новой строки
# a, b = [int(input("Enter: ")) for i in range(2)]
# print(a, b)

# Вводится e-mail, mail@example.com, а нужно вывести домен.
# mail = input("Enter your e-mail: ").split("@")
# domain = mail[-1]
# print(domain)
# print()

# Задан список А.
# Вывести сумму элементов с индексами, кратными 3
a = [2, 2, 3, 4, 56, 7, 9, 0]
s = 0
for i in range(len(a)):
    if i % 3 == 0:
        s += a[i]
print(s)
print()
# а можно сделать через срез
print(sum(a[::3]))
print()

# Задан список а.
# Циклически сдвинуть элементы списка вправо.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_A = []
for i in range(len(A)):
    if i == len(A) - 1:
        new_A.insert(0, A[i])
    else:
        new_A.append(A[i])
print(new_A)

a1 = [1, 2, 3, 4, 5, 6]
a1.insert(0, a1[-1])
a1.pop()
print(a1)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_A = A[-1:] + A[:-1]
print(new_A)
print()

# Задан список В.
# Найти второй и третий минимумы списка.
B = [1, 2, 3, 4, 5, 6, -1, 5, -6, -2]
list_min = []
for i in range(3):
    list_min.append(min(B))
    B.remove(min(B))
print(list_min[1], list_min[2])
print()

# Вводим основание системы счисления.
# Вводим число в этой системе.
# Вывести число в десятичной системе
n = 3
numm = '101'
numm = numm[::-1]
ans = 0
for i in range(len(numm)):
    ans += int(numm[i])*n**i


print(ans)
# а еще ф-ия "int()" имеет встроенную функцию перевода
ans = int(numm, n)
print(ans)

# вывести один список с элементами
list_a = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10], [11], [12, 13, 14]]
list_b = []

for list_ in list_a:
    for elem in list_:
        list_b.append(elem)

print(list_b)
# можно использовать метод ".extend()".
# он принимает несколько элементов из итерируемого объекта
list_c = []
for elem in list_a:
    list_c.extend(elem)
print(list_c)
# можно сделать склеивание списков
list_d = []
for elem in list_a:
    list_d += elem
print(list_d)
# еще можно так:
print(sum(list_a, []))
print()

# есть текст и нужно посчитать сколько раз каждый символ встречается
text = "aaabbbcc dddd"
stat = {}

for i in text:
    if i not in stat.keys():
        stat[i] = 1
    else:
        stat[i] += 1

for symbol, count in stat.items():
    print(f"{symbol} - {count}")
print()
# через set()
unique_symbols = set(text)
for symbol in unique_symbols:
    symbol_count = text.count(symbol)
    print(f"{symbol} - {symbol_count}")
print()

# вводится строка, нужно удалить каждое второе слово
string = "слово слово2 слово3 слово4"
list_ans = string.split()

str_ans = ''
for index, word in enumerate(list_ans):
    if index % 2 == 0:
        word += " "
        str_ans += word
print(str_ans)

even_words = list_ans[::2]
str_ans_1 = " ".join(even_words)
print(str_ans_1)
print()

# Вводится целое число.
# Вывести запись числа в двоичной системе
print("Через рекурсию")
n = 10


def get_binary(num):
    if num == 1:
        return str(num)
    return get_binary(num//2) + str(num % 2)


print(get_binary(n))
print()

print("Императивное решение")
ans = ''
while True:
    if n == 1:
        ans += '1'
        ans = ans[::-1]
        break
    ans += str(n % 2)
    n = n // 2

print(ans)