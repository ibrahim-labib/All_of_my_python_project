class Account:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance
    
    def credit(self, amount):
        self.balance += amount
        print(f"TK {amount} is credited and your total balance is now {self.balance}")

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"TK {amount} was debited and your total balance is {self.balance}")
        else:
            print("You don't have sufficient balance!")
    
    def transfer(self , amount , transfer_account):
        if self.balance > 0:
            self.balance -= amount
            print(f"TK {amount} was transferred to {transfer_account} id and your total balance is {self.balance}")
        else:
            print("You do not have enough balance")
acc1 = Account(12345, 10000)
acc1.credit(500)
acc1.debit(1000)
acc1.transfer(5000,1010)
