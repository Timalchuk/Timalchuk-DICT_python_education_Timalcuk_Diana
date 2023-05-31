# Создание игрового поля
board = [" " for _ in range(9)]

# Рисуем игровое поле
def draw_board():
    print("---------")
    for i in range(0, 9, 3):
        row = "|".join(board[i:i+3])
        print("|" + row + "|")
        print("---------")

# Функция для проверки, есть ли выигрышная комбинация
def check_win(player):
    # Проверка по горизонтали
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Проверка по вертикали
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Проверка по диагоналям
    if board[0] == board[4] == board[8] == player or \
       board[2] == board[4] == board[6] == player:
        return True

    return False

# Функция для хода игрока
def player_move():
    while True:
        move = input("Выберите ячейку для хода (от 1 до 9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
        print("Некорректный ход. Попробуйте еще раз.")

# Функция для хода компьютера
def computer_move():
    # Простая логика компьютера: выбираем первую свободную ячейку
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            break

# Основной игровой цикл
def play_game():
    draw_board()
    while True:
        player_move()
        draw_board()
        if check_win("X"):
            print("Вы победили!")
            break
        if " " not in board:
            print("Ничья!")
            break
        computer_move()
        draw_board()
        if check_win("O"):
            print("Вы проиграли!")
            break

# Запуск игры
play_game()
