import random

def generate_task(level):
    if level == 1:
        # Згенерувати два випадкових числа в діапазоні від 2 до 9
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        # Згенерувати випадкову арифметичну операцію
        operator = random.choice(['+', '-', '*'])
        # Створити рядок-завдання
        task = f"{num1} {operator} {num2}"
        return task
    elif level == 2:
        # Згенерувати випадкове число в діапазоні від 11 до 29
        num = random.randint(11, 29)
        # Створити рядок-завдання для зведення у квадрат
        task = f"{num}^2"
        return task

def check_answer(task, answer):
    try:
        # Перевірити, чи відповідь користувача має правильний формат
        user_answer = int(answer)
    except ValueError:
        print("Incorrect format.")
        return False

    # Отримати правильну відповідь на завдання
    if '^2' in task:
        # Якщо завдання є зведенням у квадрат, обчислити правильну відповідь
        num = int(task.split('^2')[0])
        correct_answer = num ** 2
    else:
        # Якщо завдання є арифметичною операцією, обчислити правильну відповідь
        correct_answer = eval(task)

    # Перевірити, чи відповідь користувача правильна
    if user_answer == correct_answer:
        print("Right!")
        return True
    else:
        print("Wrong!")
        return False

def save_result(name, mark, level_description):
    # Записати результат в файл results.txt
    with open('results.txt', 'a') as file:
        file.write(f"{name}: {mark}/5 in level {level_description}\n")

def run_quiz():
    level = int(input("Choose the difficulty level (1 - simple operations, 2 - squaring): "))

    if level == 1:
        level_description = "simple operations with numbers 2-9"
    elif level == 2:
        level_description = "squaring numbers 11-29"
    else:
        print("Invalid level. Exiting the program.")
        return

    correct_answers = 0
    for _ in range(5):
        # Згенерувати завдання
        task = generate_task(level)
        print(task)
        # Зчитати відповідь користувача
        while True:
            user_answer = input("Your answer: ")
            if check_answer(task, user_answer):
                correct_answers += 1
                break

    # Вивести оцінку
    print(f"Your mark is {correct_answers}/5.")
    # Зберегти результат
    name = input("Enter your name: ")
    save_result(name, correct_answers, level_description)

# Запустити тест
run_quiz()
