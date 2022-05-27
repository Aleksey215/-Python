# ***** Функция map *****
print("Функция map")
# Функция map пришла из функционального программирования.
# Она позволяет применять некую функцию к каждому элементу итерируемого объекта (строки, списки, кортежи, словари).
# Псевдо код функции map:
# def map_(func, some_list):
#     # some_list объект, над которым будет производиться преобразование
#     # func функция, которая должна выполняться над каждым объектом
#     outp = []
#     for i in range(len(some_list)):
#         outp.append(func(some_list[i]))
#     return outp

# Но особенность функции map в том, что она возвращает результат вычислений не сразу,
# а в виде итератора, который в дальнейшем производит «ленивые» вычисления.
# Чтобы получить список значений, нужно в явном виде привести к нужному типу либо воспользоваться циклом for:
# print(list(map(pow_, a_list)))  # [1, 4, 9]
#
# for i in map(pow_, a_list):
#    pass

print("Задание 5.5.1")
# C помощью метода строки str.lower перевести все элементы списка в нижний регистр.
L = ['THIS', 'IS', 'LOWER', 'STRING']
print(list(map(str.lower, L)))
print()

# ***** Функция filter *****
print("Функция filter")
# Функция filter согласно своему названию фильтрует элементы итерируемого объекта.
# Она принимает на вход:
#       функцию, которая должна возвращать bool значение (True или False);
#       итерируемый объект, над которым будет производиться фильтрация
#       (в этом случае можно передать только один объект).
# Функция filter возвращает итератор с теми элементами из входящей последовательности,
# для которых функция вернула True.

# из заданного списка необходимо вывести только положительные элементы.
def positive(x):
    return x > 0

result = filter(positive, [-2, -1, 0, 1, 2, 3, -3])
print(list(result))
print()

print("Задание 5.5.2")
# Отфильтровать из заданного списка только четные элементы.
def get_even_elements(n):
    return n % 2 == 0

print(list(filter(get_even_elements, [-2, -1, 0, 1, 2, 3, -3])))
print()

# *** В каких случаях стоит использовать map и filter? ***
# Чаще всего генераторы списков более читаемы, чем map и filter, особенно в простых конструкциях.

# map + filter
some_list = [i - 10 for i in range(20)]
def pow2(x): return x**2
def positive(x): return x > 0


print(some_list)
print(list(map(pow2, filter(positive, some_list))))

# Тоже самое через list comprehension.
new_list = [i ** 2 for i in some_list if i > 0]
print(new_list)
print()

# Возникает вопрос, когда использовать map, а когда list comprehension?
# Как оговаривалось ранее, map работает по принципу ленивых вычислений,
# а list comprehension возвращает результат вычислений сразу.

# ***** Lambda функции *****
print("***** Lambda функции *****")
# Функции map и filter принимают в виде первого аргумента другую функцию,
# которая должна применяться к каждому элементу.
# Иногда встроенных функций не хватает, и приходится объявлять функцию,
# которая зачастую будет применена всего один раз. Но при этом она будет загромождать исходный код.

# Специально для таких одноразовых функций были сделаны анонимные функции.
# Объявляются они по ключевому слову lambda.

def my_function(x1, x2):
    return x2 + x1


lambda x1,x2: x2 + x1
# Анонимные функции могут содержать в себе только одну инструкцию (выражение), которую они выполняют.
# # Возвести первые 10 натуральных чисел в квадрат
print(list(map(lambda x: x**2, range(1, 11))))

# Для чего могут быть полезны lambda-функции?
# Предположим, мы хотим отсортировать словарь по значениям.
# Вообще говоря, словарь (его еще называют ассоциативным массивом) является неупорядоченной структурой данных.
# Иными словами, порядок хранения пар ключ-значение в памяти может быть произвольным.
# Однако создатели языка Python, начиная с версии 3.6, изменили реализацию словарей таким образом,
# что порядок ключей «запоминается». И потому упорядочивание словаря в Python становится осмысленным.
# По умолчанию словарь сортируется по ключам.
d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}

# Чтобы отсортировать его по ключам нужно сделать так
print(dict(sorted(d.items())))

# А вот, чтобы отсортировать словарь по значениям, необходимо указать,
# что сортировать нужно по второму элементу кортежа ключ-значение.
# Тут на помощь приходят lambda-функции.
# У встроенной функции sortred() можно задать аргумент key, который укажет,
# по какому ключу нужно производить сортировку.
print(sorted(d.items(), key=lambda x: x[1]))  # сортировка по значению словаря

# Итог по lambda-функциям:
#   1. используются один раз;
#   2. не загромождают код программы;
#   3. после выполнения сразу удаляются;
#   4. могут выполнять только одно действие.
print()

print("Задание 5.5.3")
# Предположим у нас есть список с данными о росте и весе людей.
# Задача — отсортировать их по индексу массы тела.
# Он вычисляется по формуле:
# свой рост в сантиметрах возвести в квадрат,
# потом массу тела в килограммах разделить на полученную цифру.
# (вес, рост)
data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]

mass_list = (sorted([round(i[0] / (int(i[1]*100))**2, 5) for i in data]))
print(mass_list)

mass_list_1 = sorted(data, key=lambda x: x[0] / (x[1]*100)**2)
print(mass_list_1)
print()

print("Задание 5.5.4")
# Из списка в предыдущем задании найти кортеж с минимальным индексом массы тела
print(min(mass_list))
print(min(data, key=lambda x: x[0] / (x[1]*100)**2))