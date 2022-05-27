# n секунд прощло с начала суток. Что выведут часы в формате hh:mm:ss
n = int(input("Введите кол-во секунд: "))
temp_mm = n // 60
hh = temp_mm // 60
mm = temp_mm % 60
ss = n % 60
print('%02d:%02d:%02d' % (hh, mm, ss))
# вывод через f-строку
print(f"{hh:02d}:{mm:02d}:{ss:02d}")
print()

# в словаре хранится база паролей.
# нужно запрашивать у пользователя логин и пароль и проверять их
dict = {
    'user': 1234,
    'admin': 'qwe',
}
username = input("Enter username: ")
if username in dict.keys():
    password = input("Enter password: ")
    if dict[username] == password or dict[username] == int(password):
        print(f"Welcome {username}!")
    else:
        print("Password not correct")
else:
    print("Username not found!")
print()

# дан список результатов состоящий из пар: имя-балл.
# есть интервал баллов, при которых человек стал призером.
# вывести имя призера.
results = [('Alex', 45), ('Elena', 87), ('Skif', 35)]
start = 60
end = 100
for result in results:
    if result[1] in range(60, 100):
        print(result[0])
print()

# найти кол-во уникальных символов в строке
string = input("Enter string: ")
print(len(set(string)))

# Найти индекс минимального элемента в списке
l = [1, 4, 45, -4, 34, -45, 10]
cand = l[0]
cand_index = 0
for i in range(len(l)):
    if l[i] < cand:
        cand = l[i]
        cand_index = i
print(cand)
print(cand_index)

# Реализация через enumerate
for i, elem in enumerate(l):
    if elem < cand:
        cand = elem
        cand_index = i
print(cand)
print(cand_index)

# еще способ
print(min(enumerate(l), key=lambda pair: pair[1])[0])
# pair[1] - это обращение к значению элемента в паре индекс-элемент
print(list(enumerate(l)))
print()

# Дано натуральное число n.
# вывести слово "Yes" если число является точной степенью двойки
# или вывести "No" в противном случае
def func(n):
    if n == 1:
        return "Yes"

    if n % 2 == 0:
        print(n)
        return func(n//2)
    else:
        return "No"

print(func(10))