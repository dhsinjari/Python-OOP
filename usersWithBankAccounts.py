class BankAccount:
    
    accounts = []

    def __init__(self, int_rate, bankBalance): 
       self.int_rate = int_rate
       self.bankBalance = bankBalance
       BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.bankBalance += amount
        return self
    def withdraw(self, amount):
        if (self.bankBalance-amount) >=  0:
            self.bankBalance -= amount
        else: 
            print("insufficient funds.")
        return self
    def display_account_info(self):
        print('Balance is: ',self.bankBalance)

    def yield_interest(self):
        if self.bankBalance>0:
            self.bankBalance=(self.bankBalance*self.int_rate) + self.bankBalance
        return self

    @classmethod

    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.accounts = {
            "checking":BankAccount(0.2,0),
            "savings":BankAccount(0.5,0)
        }
        
        
    def deposit_checking(self, amount):
        self.accounts['checking'].deposit(amount)
        return self

    def deposit_savings(self, amount):
        self.accounts['savings'].deposit(amount)
        return self
    def see_balance(self):
        print('Balance is: ',self.accounts['checking'].bankBalance)
        print('Balance is: ',self.accounts['savings'].bankBalance)

    
    def withdraw_checking(self, amount):
        self.accounts['checking'].withdraw(amount)
        return self
    
    def withdraw_savings(self,amount):
        self.accounts['savings'].withdraw(amount)
        return self




#account1 = BankAccount(0.3, 1300)
#account1 = BankAccount(0.2, 1000)
#account1.deposit(200).deposit(100).deposit(300).withdraw(500).display_account_info()
#account1.deposit(100).deposit(10).deposit(30).withdraw(50).display_account_info()
#BankAccount.print_all_accounts()

user1 = User('Dhimitri','Sinjari')
user1.deposit_checking(1000)
user1.withdraw_checking(200)
user1.withdraw_savings(10)
user1.deposit_savings(100)
user1.withdraw_savings(10)
user1.see_balance()