# *** Задача 1 ***
# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово "Fizz",
# а вместо чисел, кратных пяти - слово "Buzz".
# Если число кратно и 3, и 5, то программа должна выводить слово "FizzBuzz"
print("Задача 1")


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number


for i in range(1, 101):
    print(fizzbuzz(i))
print()


# *** Задача 2 ***
# Создайте список [18, 14, 10, 6, 2] с помощью функции range().
# Пробегаемся циклом for по последовательности, которую формирует range.
# Пусть начало диапазона будет 18, а коней диапазона 1, шаг -4
print("Задача 2")

l = []
for i in range(18, 1, -4):
    l.append(i)
print(l)
print()


print(" Задача 3 ")
# Дан список list=[11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
# Необходимо вывести элементы, которые одновременно
# 1) меньше 30
# 2) делятся на 3 без остатка
# Все остальные элементы списка необходимо просуммировать и вывести конечный результат.

l1 = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
print(l1)
s = 0
for i in l1:
    if i < 30 and i % 3 == 0:
        print(i)
    else:
        s += i
print(f'sum = {s}')
print()

print(" Задача 4 ")
# Создать функцию calc(a, b, operation).
# Описание входных параметров:
# 1. Первое число
# 2. Второе число
# 3. Операция(+, -, *, /)
# В остальных случаях, функция возвращает: "Операция не поддерживается"


def calc(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return 'Нельзя делить на ноль!'
    else:
        return 'Операция не поддерживается'


print(calc(2, 2, "-"))
print()

print(" Задача 5 ")
# Напишите программу, которая будет выводить нечетные числа из списка и остановится,
# если встретит число 139
lst = [i for i in range(100, 201)]
for i in lst:
    if i % 2 != 0:
        if i != 139:
            print(i)
        else:
            break

print(" Задача 6 ")
# вывести таблицу умножения для заданного числа


def multiply(num):
    table = ''
    for i in range(1, 11):
        table += f'{i} * {num} = {i * num}\n'
    return table


print(multiply(5))
print()

print(" Задача 7 ")
# Изограмма - это слово, в котором нет повторяющихся букв,
# последовательных или непоследовательных.
# Реализуйте функцию, которая определяет, является ли строка,
# содержащая только буквы, изограммой.
# Предположим, что пустая строка является изограммой.
# Игнорировать регистр букв.


def is_isogram(string):
    new_string = set(string.lower())
    if len(new_string) == len(string.lower()):
        return "Yes"
    else:
        return "No"


print(is_isogram(input("Enter string: ")))
print()

print(" Задача 8 ")
# В массиве целых чисел найти минимум


def find_smallest_int(arr):
    min_ = arr[0]
    for i in arr:
        if i < min_:
            min_ = i
    return min_


a = [34, 15, 88, 2]
print(find_smallest_int(a))
a1 = [34, -345, -1, 100]
print(find_smallest_int(a1))
print()

print(" Задача 9 ")
# написать функцию, которая повторит заданную строку n раз


def repeat_string(n, string):
    return string * n


print(repeat_string(3, 'Hello!'))
print()


print(" Задача 10 ")
# Написать метод, который принимает логическое значение
# и возвращает строку "Да" для истины или строку "Нет" для ложного


def bool_to_word(boolean):
    if boolean:
        return "Да"
    else:
        return "Нет"


print(bool_to_word(True))
print(bool_to_word(0))
print()


print(" Задача 11 ")
# Переставить цифры полученного целого, не отрицательного числа


def descending_order(num):
    num = str(num)
    num = num[::-1]
    return int(num)


print(descending_order(123))
print()

print(" Задача 12 ")
# Учитывая список целых чисел, определите, является ли сумма его элементов нечетной или четной.
# Вывести ответ в виде строки, соответствующей "нечетному" или "четному"
# Если входной массив пуст, считайте его [0]


def odd_or_even(arr):
    s = 0
    for i in arr:
        s += i
    if s % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(odd_or_even([1, 1, 1]))