""" Python: practice № 5 'Hangman' """
import random


print("HANGMAN")
print("The game will be available soon.")

word = ("python", "hello", "cat", "java", "javascript")
random_word = random.choice(word)

for i in random_word:
    print("_", end=" ")

def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ===")
    elif (wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif (wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif (wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif (wrong == 6):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")
def print_word(letter):
    counter=0
    right_letter=0
    for chr in random_word:
        if(chr in letter):
            print(random_word[counter], end=" ")
            right_letter+=1
        else:
            print(" ", end=" ")
        counter+=1
    return right_letter
def print_lines():
    print("\r")
    for chr in random_word:
        print("\u203E", end=" ")

lengh_of_word_to_guess = len(random_word)
amound_of_times_wrong = 0
current_guess_index = 0
current_letter_guessed = []
current_letters_right = 0


while(amound_of_times_wrong != 6 and current_letters_right != lengh_of_word_to_guess):
    print()
    print(" Letter guessed so far :")
    for letter in current_letter_guessed:
        print(letter, end=" ")
    letter_guessed = input("\n Guess a letter:")
    if(random_word[current_guess_index] == letter_guessed):
        print_hangman(amound_of_times_wrong)
        current_guess_index+=1
        current_letter_guessed.append(letter_guessed)
        current_letters_right = print_word(current_letter_guessed)
        print_lines()
    else:
        amound_of_times_wrong+=1
        current_letter_guessed.append(letter_guessed)
        print_hangman(amound_of_times_wrong)
        current_letters_right = print_word(current_letter_guessed)
        print_lines()
    print("Game is over! Good job) ")

