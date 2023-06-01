def matrix_enter(rows, columns):
    # Создаем пустую матрицу
    matrix = []
    # Считываем строки матрицы
    for i in range(0, rows):
        row = input().split()[:columns]  # Вводим строку и ограничиваем ее до нужного числа элементов
        matrix.append([])  # Добавляем пустую строку в матрицу
        # Преобразуем элементы строки в числа и добавляем их в текущую строку матрицы
        for j in range(0, columns):
            matrix[i].append(float(row[j]))
    return matrix


def matrix_print(matrix):
    if matrix is None:
        return None
    # Печатаем элементы матрицы
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=' ')
        print("")


def matrix_round(matrix):
    # Округляем элементы матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = int(matrix[i][j]) if matrix[i][j] == round(matrix[i][j]) else matrix[i][j]
    return matrix


def matrix_add(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print('Размеры матрицы не равны')
        return None
    # Складываем соответствующие элементы матриц
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1[0])):
            matrix1[i][j] += matrix2[i][j]
    return matrix_round(matrix1)


def matrix_multiply_constant(matrix, const):
    # Умножаем матрицу на константу
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            matrix[i][j] *= const
    return matrix_round(matrix)


def matrix_multiply_matrix(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print('Количество столбцов первой матрицы и количество строк второй матрицы не равны')
        return None
    # Умножаем матрицы
    matrix = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix2[i])):
            result = 0
            for k in range(0, len(matrix2)):
                result += matrix1[i][k] * matrix2[k][j]
            matrix[i][j] = int(result) if round(result) == 0 else result
    return matrix_round(matrix)


def matrix_transpose(matrix, transpose_type):
    if transpose_type not in [1, 2, 3, 4]:
        print('Тип не существует')
        return None
    # Транспонируем матрицу в зависимости от выбранного типа
    matrix_transpose = []
    if transpose_type == 1:
        matrix_transpose = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range(len(matrix_transpose)):
            for j in range(len(matrix_transpose[i])):
                matrix_transpose[i][j] = matrix[j][i]
    elif transpose_type == 2:
        matrix_transpose = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range(len(matrix_transpose)):
            for j in range(len(matrix_transpose[i])):
                matrix_transpose[i][j] = matrix[len(matrix) - 1 - j][len(matrix[i]) - 1 - i]
    elif transpose_type == 3:
        matrix_transpose = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix_transpose)):
            for j in range(len(matrix_transpose[i])):
                matrix_transpose[i][j] = matrix[i][len(matrix[0]) - 1 - j]
    elif transpose_type == 4:
        matrix_transpose = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix_transpose)):
            for j in range(len(matrix_transpose[i])):
                matrix_transpose[i][j] = matrix[len(matrix) - 1 - i][j]
    return matrix_round(matrix_transpose)


def matrix_determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print('Определитель неквадратной матрицы не существует')
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    # Рекурсивно вычисляем определитель матрицы
    for i in range(0, len(matrix)):
        minor = [[0 for j in range(len(matrix) - 1)] for i in range(len(matrix[0]) - 1)]
        for j in range(1, len(matrix)):
            shift = 0
            for k in range(0, len(matrix)):
                if k == i:
                    shift = 1
                    continue
                minor[j - 1][k - shift] = matrix[j][k]
        det += ((-1) ** i) * matrix_determinant(minor) * matrix[0][i]
    return int(det) if det == round(det) else det


def matrix_reverse(matrix):
    if len(matrix) != len(matrix[0]):
        print('Обратная матрица для неквадратной матрицы не существует')
        return None
    det = matrix_determinant(matrix)
    if det == 0:
        print('Обратная матрица для матрицы с нулевым определителем не существует')
        return None
    transpose_matrix = matrix_transpose(matrix, 1)
    reverse_matrix = [[0 for j in range(len(transpose_matrix))] for i in range(len(transpose_matrix[0]))]
    for i in range(len(transpose_matrix)):
        for j in range(len(transpose_matrix[0])):
            minor = [[0 for j in range(len(transpose_matrix) - 1)] for i in range(len(transpose_matrix[0]) - 1)]
            row_shift = 0
            for k in range(len(transpose_matrix)):
                if k == i:
                    row_shift = 1
                    continue
                column_shift = 0
                for p in range(len(transpose_matrix[0])):
                    if p == j:
                        column_shift = 1
                        continue
                    minor[(k - row_shift)][(p - column_shift)] = transpose_matrix[k][p]
            reverse_matrix[i][j] = ((-1) ** (i + j)) * matrix_determinant(minor)
    return matrix_round(matrix_multiply_constant(reverse_matrix, 1/det))


def main_menu():
    while True:
        print("""1. Добавить матрицы
2. Умножить матрицу на константу
3. Умножение матриц
4. Транспонировать матрицу
5. Вычислить определитель
6. Обратная матрица
0. Выход
Твой выбор:""", end="")
        choice = int(input())
        if choice == 0:
            return None
        elif choice == 2:
            print("Введите размер матрицы:", end="")
            size = input().split(" ")
            print("Введите матрицу:")
            matrix = matrix_enter(int(size[0]), int(size[1]))
            print("Введите константу:", end="")
            constant = float(input())
            matrix = matrix_multiply_constant(matrix, constant)
            matrix_print(matrix)
        elif choice == 4:
            print('''1.Главная диагональ
2. Боковая диагональ
3. Вертикальная линия
4. Горизонтальная линия
Твой выбор:''', end="")
            choice = int(input())
            print("Введите размер матрицы:", end="")
            size = input().split(" ")
            print("Введите матрицу:")
            matrix = matrix_enter(int(size[0]), int(size[1]))
            matrix = matrix_transpose(matrix, choice)
            matrix_print(matrix)
        elif choice == 5 or choice == 6:
            print("Введите размер матрицы:", end="")
            size = input().split(" ")
            print("Введите матрицу:")
            matrix = matrix_enter(int(size[0]), int(size[1]))
            if choice == 5:
                det = matrix_determinant(matrix)
                if det is None:
                    continue
                print('Результат :\n', det)
            elif choice == 6:
                matrix = matrix_reverse(matrix)
                matrix_print(matrix)
        elif choice == 1 or choice == 3:
            matrix = []
            print("Введите размер первой матрицы:", end="")
            size = input().split(" ")
            print("Введите первую матрицу:")
            first_matrix = matrix_enter(int(size[0]), int(size[1]))
            print("Введите размер второй матрицы:", end="")
            size = input().split(" ")
            print("Введите вторую матрицу:")
            second_matrix = matrix_enter(int(size[0]), int(size[1]))
            if choice == 1:
                matrix = matrix_add(first_matrix, second_matrix)
            elif choice == 3:
                matrix = matrix_multiply_matrix(first_matrix, second_matrix)
            matrix_print(matrix)


main_menu()
