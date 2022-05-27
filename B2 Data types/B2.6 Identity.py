# ***** Идентичность *****
"""
Встроенная функция id() позволяет получить число, которое называется идентичностью.
Каждый объект при создании получает некоторое значение идентичности,
и оно не может измениться у одного конкретного объекта во время выполнения программы.
Также можно сказать, что это число ассоциируется с адресом области памяти компьютера,
в которой хранится данный объект.
"""

L = ['a', 'b', 'c']
print(id(L))
L.append('d')
print(id(L))
# Так как список - это изменяемый тип данных, его id не изменился
print()
a = 5
print(id(a))
b = 3 + 2
print(id(b))
# Некоторые целые числа и строки кэшируются в памяти, позволяя не создавать каждый раз новый объект.
# Иными словами, Python при компиляции сам создает объекты некоторых видов и сохраняет их в памяти.
# И если в коде встречается «создание» такого объекта, то он подгружается из этой временной памяти.

# свойство уникальности каждого объекта используется,
# в том числе для сравнения объектов с помощью ключевого слова is.
print()
list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)
print(list_2)
print(list_3)

# проверяем равенство этих списков
print("Проверка равенства")
print(list_1 == list_2)
print(list_1 == list_3)

# их значения list_1, list_2, list_3 равны, тогда условие становится истинным
print("Проверка is")
print(list_1 is list_2)
print(list_1 is list_3)
# list_1 и list_3 указывают на два разных объекта, даже если их содержимое может быть одинаковым.
# «is» вернет True, если две переменные указывают на один и тот же объект,
# и «==», если объекты, на которые ссылаются переменные, равны.

# При работе со списками есть особенность, которую необходимо рассмотреть.
print()
L = ['Hello', 'world']
M = L
print(M is L)
# Очевидно, что эти списки будут равны по своим значениям (сравнивая через ==).
# И при таком присваивании в M скопируется не сам список L, а его идентификатор!
# Поэтому, изменяя список M, мы увидим неожиданные изменения в списке L.
M.append('!')
print(L)
# Чтобы избежать такого поворота событий, список нужно копировать.
M = L.copy()
print(M is L)
M.append('45')
print(L)
print(M)

# ***** Неизменяемость кортежей *****
print("***** Неизменяемость кортежей *****")
# Ранее мы рассматривали три схожих между собой типа данных — кортежи, списки и словари.
# Списки хранят объекты, ассоциируя с ними числа — индексы.
# Аналогично словари каждому значению ставят в пару его ключ.
# К элементам кортежа также можно обратиться по индексам, однако он является неизменяемым.
# После создания он «замораживается» и добавить или удалить элементы становится невозможно.
# Неизменяемость кортежей заключается в неизменности набора уникальных идентификаторов объектов,
# которые хранятся в кортеже.

# Например, мы хотим хранить в кортеже информацию о торгово-развлекательном центре:
# его название, адрес и список магазинов.
# В общем-то такой набор информации остается почти всегда неизменным за исключением того,
# что список магазинов может изменяться — какие-то закрываются, какие-то открываются или же меняют название.
# По этой причине такой список нельзя хранить в самом кортеже.
# Однако можно создать список (list) внутри самого кортежа.

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
shopping_center[-1].append("Uniqlo")
print(shopping_center)
# Как видим, изменение списка внутри кортежа не привело к ошибке,
# потому что уникальный идентификатор этого списка остался неизменным.