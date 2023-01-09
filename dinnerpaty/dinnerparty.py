"""" Python: practice №6 dinner party"""
import random

    #Узнаём количество чуловек и их имена
def band_list():
    friend_list = dict()
    print("Сколько включая вас будет человек?")
    number_of_members = int(input())
    if number_of_members <= 0:
        print("\n Никого не будет!")
        exit()
    else:
        print("\n Ввести имена участников включая вас:")
        for i in range(0, number_of_members):
            friend: str = input()
            friend_list[friend] = 0
        return friend_list

    # Из выше перечисленных имен выбираем счастливчика или нет
def who_is_lucky(friend_list: dict):
    name = random.choice(list(friend_list.keys()))
    print("{name} Кто счастливчик?\n")
    return name

    # Делим сумму на количество человек( если комуто повезло то количество человек -1)
def segmentation(friend_list: dict):
    print("\n Ну и на сколько вы наели?!")
    sum = int(input())
    print("\n Вы хотите узнать кому повезло?  Напишите Yes/No:")
    answer = input()
    if answer == 'Yes':
        lucky_one = who_is_lucky(friend_list)
        if sum % (len(friend_list) - 1) == 0:
            pay = int(sum / (len(friend_list) - 1))
        else:
            pay = round(sum / (len(friend_list) - 1), 2)
        for friend in friend_list:
            if friend == lucky_one:
                friend_list[friend] = 0
                continue
            friend_list[friend] = pay
    else:
        print("\nУпс сочувствую, попробуйте еще раз!")
        if sum % len(friend_list) == 0:
            pay = int(sum / len(friend_list))
        else:
            pay = round(sum / len(friend_list), 2)
        for friend in friend_list:
            friend_list[friend] = pay
    print(friend_list)

    # Получаем наши ответы
friend_list = band_list()
segmentation(friend_list)
