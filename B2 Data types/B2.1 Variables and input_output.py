# ***** Переменные *****
# Переменная - это именованная ссылка на область памяти компьютера, которая хранит данные
# Запись данных в переменную
some_var = "value"
# слева - имя переменной, справа - значение, которое она хранит, а "=" - это оператор присвоения.

# Существует два главных правила именования переменных:
#     Название переменной должно состоять только из букв, цифр и знаков подчеркивания _.
#     Название переменной не должно начинаться с цифры.

# Python поддерживает "Множественное присвоение":
a, b = "some_string_a", "some_string_b"
print(a)
print(b)

# ***** Ввод с консоли, input() и вывод в консоль, print() *****
# Функция "input()" - принимает данные, которые пользователь вводит в консоли с клавиатуры.
# Данная функция, по умолчанию возвращает значение в формате строки.
# Для подсказки, можно в качестве аргумента передать строку с текстом.
# Так же важно то, что результат, который возвращает данная функция
# обязательно должен записываться в какую-то переменную.
text = input('Enter text: ')
# Функция "print()" - выводит все значения, переданные ей в качестве аргумента, в консоль.
# Здесь нет необходимости возвращать какие-то данные обратно в программу,
# поэтому print() не имеет возвращаемого значения.
# Это означает, что нет необходимости присваивать её какой-то переменной.
print(text)
# Более того, можно выводить в консоль сразу и текст, и числа.
# Для этого вводимые данные разделяются запятыми.
# По умолчанию функция print() автоматически ставит пробел между аргументами:
print("Hello world!",412)