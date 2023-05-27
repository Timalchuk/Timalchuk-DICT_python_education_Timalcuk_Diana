    # Симулято кофе машины
class CoffeeMachine:
    def __init__(self):
        # Задаем начальные данные
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = "main_menu"

    def process_input(self, user_input):
        # делаем ввод в текущее состояние машины
        if self.state == "main_menu":
            if user_input == "buy":
                self.state = "buy_menu"
            elif user_input == "fill":
                self.state = "fill_menu"
            elif user_input == "take":
                self.take_money()
            elif user_input == "remaining":
                self.print_state()
            elif user_input == "exit":
                return False
            else:
                print("Invalid action! Please try again.")
        elif self.state == "buy_menu":
            if user_input == "back":
                self.state = "main_menu"
            else:
                self.buy_coffee(user_input)
        elif self.state == "fill_menu":
            self.fill_machine(user_input)

        return True

    def print_state(self):
        # Выводим текущее состояние кофейной машины
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money")

    def can_make_coffee(self, water_needed, milk_needed, coffee_beans_needed):
        # Проверяем, достаточно ли ингредиентов для приготовления кофе
        if self.water < water_needed:
            return "water"
        if self.milk < milk_needed:
            return "milk"
        if self.coffee_beans < coffee_beans_needed:
            return "coffee beans"
        if self.disposable_cups == 0:
            return "disposable cups"
        return None

    def buy_coffee(self, coffee_type):
        # Определяем необходимые ингредиенты и стоимость для выбранного кофе
        if coffee_type == "1":
            water_needed = 250
            milk_needed = 0
            coffee_beans_needed =16
            cost = 4
        elif coffee_type == "2":
            water_needed = 350
            milk_needed = 75
            coffee_beans_needed = 20
            cost = 7
        elif coffee_type == "3":
            water_needed = 200
            milk_needed = 100
            coffee_beans_needed = 12
            cost = 6
        else:
            print("Invalid coffee type! Please try again.")
            return

        # Проверяем, достаточно ли ингредиентов для приготовления кофе
        ingredient = self.can_make_coffee(water_needed, milk_needed, coffee_beans_needed)
        if ingredient:
            print(f"Sorry, not enough {ingredient}!")
        else:
            # Если ингредиентов достаточно, приготавливаем кофе и списываем необходимое количество ингредиентов
            print("I have enough resources, making you a coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= coffee_beans_needed
            self.disposable_cups -= 1
            self.money += cost

    def fill_machine(self, user_input):
        # Пополняем запасы ингредиентов в зависимости от текущего состояния кофейноймашины
        if self.state == "fill_menu":
            if user_input.isdigit():
                self.water += int(user_input)
                self.state = "fill_menu_milk"
            else:
                print("Invalid input! Please enter a number.")
        elif self.state == "fill_menu_milk":
            if user_input.isdigit():
                self.milk += int(user_input)
                self.state = "fill_menu_coffee_beans"
            else:
                print("Invalid input! Please enter a number.")
        elif self.state == "fill_menu_coffee_beans":
            if user_input.isdigit():
                self.coffee_beans += int(user_input)
                self.state = "fill_menu_disposable_cups"
            else:
                print("Invalid input! Please enter a number.")
        elif self.state == "fill_menu_disposable_cups":
            if user_input.isdigit():
                self.disposable_cups += int(user_input)
                self.state = "main_menu"
            else:
                print("Invalid input! Please enter a number.")

    def take_money(self):
        # Забираем деньги
        print(f"I gave you {self.money}")
        self.money = 0


def main():
    # Создаем класса CoffeeMachine и запускаем в бесконечный цикл пользовательского ввода coffee_machine = CoffeeMachine()
    while True:
        user_input = input("Write action (buy, fill, take, remaining, exit):\n")
        if not coffee_machine.process_input(user_input):
            break


if __name__ == "__main__":
    main()



