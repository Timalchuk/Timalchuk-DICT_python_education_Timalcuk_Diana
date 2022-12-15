bot_name = "Airs"
birth_year = "2022"
print("Hello! My name is,", bot_name, "\nI was created in ", birth_year, )

print("Please, remind me your name")
user_name = input()
print("What a great name you have,", user_name, "!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
user_remainder1 = int(input("  / 3"))
user_remainder2 = int(input(" / 5"))
user_remainder3 = int(input(" / 7"))
user_remainder = int((user_remainder1 * 70 + user_remainder2 * 21 + user_remainder3 * 15) % 105)
print("Your age is ", user_remainder, "that's a good time to start programming!")