class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount

        return self 


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self 


    def display_account_info(self):
        print("-----------------")
        print(f"Interest Rate: {self.int_rate}")
        print(f"Account Balance: {self.balance}")
        print("-----------------")
        return self 


    def yield_interest(self):
        if self.balance < 0:
            print("Insufficient Funds for Yielded Interest")
        else:
            self.balance += self.int_rate * self.balance 
        return self 


bank = BankAccount(.01,100)
bank2 = BankAccount(.2, 100)

bank.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()
bank2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()