#I don,t know if i have any python in my brain or not but..Let's try :)
# Okay so i'm deciding to make a vending machine..is'nt it great

class Vending_machine:
    def __init__(self, money):
        self.stock = {
            1: {'name': 'Coke', 'quantity': 10, 'price': 30},
            2: {'name': 'Pepsi', 'quantity': 10, 'price': 30},
            3: {'name': 'Prime', 'quantity': 10, 'price': 400},
            4: {'name': 'Mojo', 'quantity':20, 'price': 25},
            5: {'name':'Drinko', 'quantity':20, 'price': 30}
        }
        self.money = money

    def display(self):
         for num, drink in self.stock.items():
            print(f"{num}: {drink['name']} - {drink['quantity']}")
        
    def get_drink(self):
        try:
            userinp = int(input("Choose your drink by number: "))
            pay = int(input("Insert money: "))
        except ValueError:
            return "Invalid input. Please enter a valid number."

        if userinp in self.stock:
            drink = self.stock[userinp]
            if drink['quantity'] > 0:
                if pay >= drink['price']:
                    change = pay - drink['price']
                    self.money += drink['price']
                    drink['quantity'] -= 1
                    return f"Here is your {drink['name']}. Change: {change}. Remaining: {drink['quantity']}"
                else:
                    return f"Insufficient funds. {drink['name']} costs {drink['price']}, but you only provided {pay}."
            else:
                return f"{drink['name']} is out of stock."
        else:
            return "Invalid selection."



vm = Vending_machine(5000)
vm.display()
print(vm.get_drink())