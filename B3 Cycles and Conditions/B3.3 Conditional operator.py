# ***** Простой условный оператор *****

# Условный оператор позволяет выполнять определенные вами команды при некотором условии.
# Условие задается логическим выражением, которое может принимать два значения:
# «истина» или «ложь», и в зависимости от этого выполнять какие-то действия или, наоборот, пропускать их.
# Запись условного оператора на Python
# if Условие:
#     Блок инструкций 1
# else:
#     Блок инструкций 2
# Часть else условного оператора не является обязательной и может быть опущена,
# если вам не нужно ничего делать в случае ложности проверяемого условия.

# Вложенные условные операторы

# is_rainy = True  # дождь будет
# heavy_rain = False  # не сильный дождь
#
# if is_rainy:
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")
# Пример программы проверки делителя:
num = 5
# в качестве условия неявное приведение к логическому типу
if num:
    print(10 / num)
else:
    print("На ноль делить нельзя")