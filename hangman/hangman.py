""" Python: practice № 5 'Hangman' """
import random


print("HANGMAN")
print("The game will be available soon.")

word = ("python", "hello", "cat", "java", "javascript")
take = random.choice(word)

print('there are', len(take), ' letters in a word')

guessed = ['_'] * len(take)
wrong = []


def transformation():
    for x in guessed:
        print(x, end=' ')
    print()


transformation()

while True:

    user_write = input("Input a letter:")
    if user_write in take:
        index = 0
        for i in take:
            if i == user_write:
                guessed[index] = user_write
            index += 1
        transformation()
    else:
             if user_write not in wrong:
               wrong.append(user_write)
             else:
                print('You already guessed that')
             print(wrong)
    if len(wrong) > 6:

        print('You lost!')
        print('', take)
        break
    if '_' not in guessed:
        print('You win!')
        break
