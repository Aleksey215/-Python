# ***** Задачи по пройденным материалам *****

a = 0
b = 0
while id(a) == id(b):
    a -= 1
    b -= 1
print(a)

# Максимальное положительное число, хранящееся в кэш = 257
# Максимальное отрицательное число, хранящееся в кэш = -6

# Списки нельзя копировать через простое присвоение:
L = [1, 2, 3]
M = L
# Потому, что копируется не сам список, а его id, то есть ссылка на область памяти,
# а это приведет к тому, что изменяя список М мы будем менять список L
M.append(5)
print(M)
print(L)
# Следовательно, копировать списки надо через метод ".copy()"
L1 = [4, 5, 6]
M1 = L.copy()
M1.append(10)
print(L1)
print(M1)
print()

# *** Неизменяемость кортежей ***
print("*** Неизменяемость кортежей ***")
# Сам кортеж изменять нельзя, но можно в нем хранить элемент изменяемого типа данных (список, например)
shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
shopping_center[-1].append("Uniqlo")
print(shopping_center)
# изменение списка внутри кортежа не привело к ошибке,
# потому что уникальный идентификатор этого списка остался неизменным.
print()

# *** Уникальные элементы списка ***
print("*** Уникальные элементы списка ***")
# Для решения практических задач, по поиску уникальных элементов,
# в Python есть еще один изменяемый тип данных — множества (set).

# Множество — это неупорядоченный набор уникальных элементов.
# Иными словами, во множествах не могут повторяться элементы,
# а хранятся они в памяти компьютера в произвольном порядке.

# Создать множество можно несколькими способами:
a = {'a', 'b', 'c', 'd'}
# или, что нам будет более полезно, множество можно создать из списка с помощью приведения типов:
l = [1, 1, 2, 3, 2]
print(l)
b = set(l)
print(b)
# так же можно опять вернуть множество в список
b_list = list(b)
print(b_list)
# для краткости все эти операции можно записать в одну строку
c = list(set(l))
print(c)
print()

print('Задание 5.2.9')
# Напишите программу, которая на вход принимает текст и выводит количество уникальных символов.
text = "some text"
print(len(set(text)))
print()

# Множества в Python аналогичны математическим множествам, поэтому для них существует несколько собственных операций.
#     set.union(other) - Объединение - Возвращает множество, состоящее из элементов set и other.
#     set.intersection(other) - Пересечение - Возвращает множество, состоящее из элементов,
#                                             которые встречаются и в set, и в other.
#     set.difference(other) - Разность - Возвращает множество элементов set, которые не встречаются в other.
#     set.symmetric_difference(other) - Симметричная разность - Возвращает множество элементов,
#                                                               встречающиеся в одном из множеств,
#                                                               но не в обоих одновременно.

# Пусть у нас есть множество абонентов (для простоты — фамилии)
# и множество должников, а мы хотим получить множество абонентов, не имеющих долгов.
abons = {"Иванов", "Петров", "Васильев", "Антонов"}
debtors = {"Петров", "Антонов"}
non_debtors = abons.difference(debtors)
print(non_debtors)
print()

