class Coffee_machine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "normal"
        
    def do_action(self, action):
        if self.state == "normal":
            if action == "remaining":
                self.display_ing()
            elif action == "buy":
                self.state = "prepare_coffee"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")    
            elif action == "fill":
                print("Write how many ml of water do you want to add:")
                self.state = "add_water"
            elif action == "take":
                self.take_money() 
            elif action == "exit":
                return True  
        elif self.state == "prepare_coffee":
            if action == "1":
                if self.if_enough_esspresso():
                    self.buy_espresso()
            elif action == "2":
                if self.if_enough_late():
                    self.buy_latte()
            elif action == "3":
                if self.if_enough_cappucino():
                    self.buy_cappucino()
            elif action == "back":
                self.state = "normal"
            self.state = "normal" 
        elif self.state == "add_water":
            self.water += int(action)
            print("Write how many ml of milk do you want to add:")
            self.state = "add_milk"
        elif self.state == "add_milk":
            self.milk += int(action)
            print("Write how many grams of coffee beans do you want to add:")
            self.state = "add_beans"
        elif self.state == "add_beans":
            self.beans += int(action)
            print("Write how many disposable cups of coffee do you want to add:")
            self.state = "add_cups"
        elif self.state == "add_cups":
            print("Write how many disposable cups of coffee do you want to add:")
            self.cups += int(action)
            self.state = "normal"
        return False
        

    def display_ing(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("$" + str(self.money), "of money")

    def buy_espresso(self):
        self.water -= 250
        self.beans -= 16
        self.money += 4
        self.cups -= 1 

    def buy_latte(self):
        self.water -= 350
        self.milk -= 75
        self.beans -= 20
        self.money += 7
        self.cups -= 1 
    
    def buy_cappucino(self):
        self.water -= 200
        self.milk -= 100
        self.beans -= 12
        self.money += 6
        self.cups -= 1 
        
    def if_enough_esspresso(self):
        if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            return True
        else:
            if self.water < 250:
                print("Sorry, not enough water!")    
            elif self.beans < 16:
                print("Sorry, not enough beans!")
            elif self.cups == 0:
                print("Sorry, not enough cups!")
            return False

    def if_enough_late(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            return True
        else:
            if self.water < 350:
                print("Sorry, not enough water!")   
            elif self.milk < 75:
                print("Sorry, not enough milk!") 
            elif self.beans < 20:
                print("Sorry, not enough beans!")
            elif self.cups == 0:
                print("Sorry, not enough cups!")
            return False

    def if_enough_cappucino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            return True
        else:
            if self.water < 200:
                print("Sorry, not enough water!")   
            elif self.milk < 100:
                print("Sorry, not enough milk!") 
            elif self.beans < 12:
                print("Sorry, not enough beans!")
            elif self.cups == 0:
                print("Sorry, not enough cups!")
            return False
        
    def take_money(self):
        money_now = self.money
        self.money = 0
        print("I gave you $" + str(money_now))
        




coffee_m = Coffee_machine() 

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if coffee_m.do_action(action):
        break
    
    
    
    
    
