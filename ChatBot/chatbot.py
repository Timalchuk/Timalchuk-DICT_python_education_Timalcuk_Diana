print("Hello! My name is, Airs" "\nI was created in 2022 " )

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

user_number = int(input("Now I will prove to you that I can count to any number you want"))
number = 0
while number <= user_number:
    print(number )
    number += 1
else:
    print("Completed, have a nice day!")

test = int(input("Let's test your programming knowledge." "\nWhy do we use methods?" 
                 "\n1. To repeat a statement multiple times." 
                 "\n2. To decompose a program into several small subroutines." 
                 "\n3. To determine the execution time of a program."
                 "\n4. To interrupt the execution of a program." 
                 "\n5. I dont know"))
print()
while test != 2:
    test = int(input("Please, try again." ))
    print()
else:
    test = 1
    print("Completed, have a nice day!")
    print("Congratulations, have a nice day!")