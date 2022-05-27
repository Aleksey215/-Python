player_1 = input("Игрок 1 - введите ваше имя: ")
player_2 = input("Игрок 2 - введите ваше имя: ")


def greetings():
    print(f"""
{player_1} и {player_2}, добро пожаловать в игру "Крестики-нолики"!
{player_1} - вы играете крестиками и ходите первым.
{player_2} - вы играете ноликами и ходите вторым.
Для того, чтобы сделать ход вам нужно последовательно ввести две координаты:
"Х" - номер строки и "Y" - номер столбца.
Игра продолжается до тех пор, пока кто-то соберет выигрышную комбинацию
или закончатся ходы и на поле не останется свободного места.
    """)


sign = " - "
field = []
for i in range(4):
    field.append([sign] * 4)


def display_field():
    for i in range(4):
        for j in range(4):
            if i == 0:
                print(f"{j} ", end="  ")
            elif j == 0:
                print(f"{i} ", end="|")
            else:
                print(f"{field[i][j]}", end="|")
        print()
    print("-----------------------------------")


def make_a_move():
    while True:
        if move % 2 != 0:
            print(f"Ходят крестики! {player_1}, ваш ход!")
            x = input("Введите - Х: ")
            if not x:
                print("Вы не ввели координату")
                continue
            x = int(x)
            if x > 3 or x < 1:
                print("Неверно задана координата, введите число от 1 до 3")
                continue
            y = input("Введите - Y: ")
            if not y:
                print("Вы не ввели координату")
                continue
            y = int(y)
            if y > 3 or y < 1:
                print("Неверно задана координата, введите число от 1 до 3")
                continue
            if field[x][y] == " - ":
                field[x][y] = " X "
                print("-----------------------------------")
                break
            else:
                print("Клетка занята введите другие координаты!")
        else:
            print(f"Ходят нолики! {player_2}, ваш ход!")
            x = input("Введите - Х: ")
            if not x:
                print("Вы не ввели координату")
                continue
            x = int(x)
            if x > 3 or x < 1:
                print("Неверно задана координата, введите число от 1 до 3")
                continue
            y = input("Введите - Y: ")
            if not y:
                print("Вы не ввели координату")
                continue
            y = int(y)
            if y > 3 or y < 1:
                print("Неверно задана координата, введите число от 1 до 3")
                continue
            if field[x][y] == " - ":
                field[x][y] = " O "
                print("-----------------------------------")
                break
            else:
                print("Клетка занята введите другие координаты!")


def winner():
    winning_comb = [[(1, 1), (1, 2), (1, 3)], [(2, 1), (2, 2), (2, 3)], [(3, 1), (3, 2), (3, 3)],
                    [(1, 1), (2, 1), (3, 1)], [(1, 2), (2, 2), (3, 2)], [(1, 3), (2, 3), (3, 3)],
                    [(1, 1), (2, 2), (3, 3)], [(1, 3), (2, 2), (3, 1)]]

    for comb in winning_comb:
        comb_list = []
        for element in comb:
            comb_list.append(field[element[0]][element[1]])
        if comb_list[0] == " X " and comb_list[1] == " X " and comb_list[2] == " X ":
            print(f"Игра окончена! Победили крестики! {player_1}, поздравляем вас!")
            print("-----------------------------------")
            return True
        elif comb_list[0] == " O " and comb_list[1] == " O " and comb_list[2] == " O ":
            print(f"Игра окончена! Победили нолики! {player_2}, поздравляем вас!")
            print("-----------------------------------")
            return True
        else:
            continue


greetings()
display_field()
move = 1
while True:
    if winner():
        break
    elif move == 10:
        print("Ничья!")
        break
    else:
        make_a_move()
        display_field()
        move += 1

