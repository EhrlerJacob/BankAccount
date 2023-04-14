
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    

    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self 
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self 
    
    def display_user_balance(self):
        print(f"{self.name}'s balance is:")
        self.account.display_account_info()
        return self

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


# bank = BankAccount(.01,100)
# bank2 = BankAccount(.2, 100)

# bank.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display_account_info()
# bank2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()


user1 = User("Jacob", "jacob@gmail.com")
user1.make_deposit(100).make_deposit(100).display_user_balance()

user2 = User("Jessica", "jessica@gmail.com")
user2.make_deposit(1500).display_user_balance().make_withdrawal(500).display_user_balance()
