# ***** Замыкания и декораторы *****
print("*** Функции высшего порядка ***")
# Функция высшего порядка — в программировании это функция,
# принимающая в качестве аргументов другие функции или
# возвращающая другую функцию в качестве результата.

# Мы можем передавать функции как параметры:
# def my_func(inside_func):
#     ...
#     inside_func()  # Вызов функции принятой в качестве аргумента
#     ...
# Можем возвращать как результат:
# def a():
#     def b():
#         pass
#     return b

# Сделаем функцию, которая будет выполнять принимаемую функцию дважды:


def twice_func(inside_func):
    """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
    inside_func()
    inside_func()


def hello():
    print("Hello")


test = twice_func(hello)
print()

print("*** Замыкание функций ***")
# Замыкание в программировании — это функция, в теле которой присутствуют ссылки на переменные,
# объявленные вне тела этой функции в окружающем коде и не являющиеся её аргументами.
# Вспомните нелокальную (nonlocal) область видимости, на этом принципе работает замыкание функций.

# Сделаем функцию, которая будет возвращать функцию, всегда прибавляющую одно и тоже число x:


def make_adder(x):
    def adder(n):
        return x + n  # захват переменной "x" из nonlocal области
    return adder  # возвращение функции в качестве результата


add_5 = make_adder(5)
print(add_5(10))
print(add_5(100))
print()

print("*** Декораторы ***")
# Декораторы предназначены для подключения любого дополнительного поведения к основной функции,
# называемой декорируемой функцией, которое может выполняться до, после или даже вместо основной функции.
# При этом исходный код декорируемой функции никак не затрагивается.

# Пример:
def my_decorator(a_functon_to_decorate):
    # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        print("Выполнение до основного вызова")
        result = a_functon_to_decorate()
        print("Выполнение после основного вызова")
        return result
    return wrapper


def my_func():
    print("Декорируемая функция")
    return 0


print(my_func())

decorated_function = my_decorator(my_func)
print(decorated_function())

# пример замера времени выполнения функции
import time


def decorator_time(function):
    def wrapper():
        print(f"Запустилась функция - {function}")
        t0 = time.time()
        result = function()
        dt = time.time() - t0
        print(f"Функция {function} выполнилась за время: {dt:.10f}")
        return dt, result  # задекорированная функция будет возвращать время работы
    return wrapper


def pow_2():
    return 10 ** 2


def in_build_pow():
    return pow(10, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

print(pow_2())

print(in_build_pow())
# Чтобы замерить время, будем использовать модуль time, в котором есть функция time(), возвращающая текущее время.
# Зная время до начала выполнения и сразу после, можно вычислить время работы функции.
print()

print("Задание 4.5.1")
# Взять из предыдущего примера декорированные функции, которые возвращают время работы основной функции
# и найти среднее время выполнения для 100 выполнений каждой функции.


def decorator_time(function):
    def wrapper():
        t0 = time.time()
        result = function()
        dt = time.time() - t0
        return dt  # задекорированная функция будет возвращать время работы
    return wrapper


def pow_2():
    return 1000000 ** 2


def in_build_pow():
    return pow(1000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)


print(f'Время выполнения pow_2:, {pow_2():.10f}')
print(f'Время выполнения in_build_pow, {in_build_pow():.10f}')

summ = 0
summ_1 = 0
for f in range(100):
    summ += pow_2()
    summ_1 += in_build_pow()

print(f'Среднее время выполнения pow_2 за 100 вызовов, {summ / 100:.10f}')
print(f'Среднее время выполнения in_build_pow за 100 вызовов,{summ_1 / 100:.10f}')
print()

print("*** Синтаксический сахар ***")
# Синтаксический сахар в языке программирования — это синтаксические возможности,
# применение которых не влияет на поведение программы, но делает использование языка более удобным для человека.
# Пример:


@my_decorator
def my_function():
    pass
# Данная запись аналогична: my_function = my_decorator(my_function)
# !!! при использовании синтаксического сахара, на месте декорируемой функции появляется задекорированная функция!


def my_decorator_1(fn):
    def wrapper():
        fn()
    return wrapper  # возвращается задекорированная функция, которая заменяет исходную

# выведем незадекорированную функцию
def my_fn():
    pass
print(my_fn)

# выведем задекорированную функцию
@my_decorator_1
def my_fn():
    pass
print(my_fn)
# после декорирования, под названием исходной функции будет не сама функция,
# а функция, которая была внутри декоратора, в данном случае функция wrapper.
print()

print("*** Передача аргументов в декорируемую функцию ***")
# wrapper должен уметь принимать те же аргументы, что и исходная функция и передавать их в неё.
# Чтобы не задумываться над количеством аргументов и сделать наш декоратор универсальным,
# мы будем использовать *args и **kwargs.

# декоратор, в котором встроенная функция умеет принимать аргументы:


def do_it_twice(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        function(*args, **kwargs)
    return wrapper


@do_it_twice
def say_word(word):
    print(word)


say_word("Hi")

# итог по декораторам:
#     Декораторы добавляют дополнительное поведение функции без изменения её исходного кода
#     Декораторы — вызовы дополнительных функций, поэтому они немного замедляют ваш код
#     Для передачи аргументов декорируемой функции используйте *args и **kwargs.
# ---------------------------------------------------------------------------------------------------------------
# универсальный шаблон для декоратора:
def my_decorator(function):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = function(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result
    return wrapper
# ---------------------------------------------------------------------------------------------------------------


print("Задание 4.5.2")
# Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции.
# Для хранения переменной содержащей, количество вызовов, используйте nonlocal область декоратора.
def call_count(function):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        function(*args, **kwargs)
        count += 1
        print(f"Функция {function} была вызвана {count} раз")
    return wrapper


@call_count
def say_word_1(word):
    print(word)


say_word_1("Hello")
say_word_1("Hello")
say_word_1("Hello")

print("Задание 4.5.3")
# Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре.
# Словарь должен находиться в nonlocal области в следующем формате:
# по ключу располагается аргумент функции, по значению результат работы функции, например, {n: f(n)}.

# И при повторном вызове функции будет брать значение из словаря, а не вычислять заново.
# То есть словарь можно считать промежуточной памятью на время работы программы,
# где будут храниться ранее вычисленные значения.
# Исходная функция, которую нужно задекорировать имеет следующий вид
# и выполняет простое умножение на число 123456789.

# def f(n):
#    return n * 123456789


def cash_decorator(function):
    cash_dict = {}

    def wrapper(n):
        nonlocal cash_dict
        if n in cash_dict:
            print(f"Взято из кэша {cash_dict[n]}")
            return cash_dict[n]
        else:
            result = function(n)
            cash_dict[n] = result
            print(cash_dict)
            print(f"в кэш добавлено новое значение: {result}")
            return result
    return wrapper

# Реализация декоратора от SkillFactory
# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper


@cash_decorator
def f(n):
    return n * 123456789


f(1)
f(2)

f(2)