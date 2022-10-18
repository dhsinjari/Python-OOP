


class User:
    def __init__(self, firstName, lastName, bankBalance):
        self.firstName = firstName
        self.lastName = lastName
        self.bankBalance = bankBalance
        
    
    def withdraw(self, amount):
        self.bankBalance -= amount
        return self.bankBalance
    
    def deposit(self, amount):
        self.bankBalance += amount
        return self.bankBalance
    
    def userBalance(self):
        x = '%s %s,User Bank Balance: %s' %\
        (self.firstName,self.lastName, self.bankBalance)
        print(x)
        return x
    '''
    def transferMoney(self,sender, receiver, amount):
        print('Enter the amount that you want to trasfer.')
        input(amount)
        user1.deposit(amount)
        user2.withdraw(amount)
        user1.bankBalance()
        user2.bankBalance()
 '''        

user1 = User('Dhimitri', 'Sinjari', 300)
user2 = User('Jon', 'Doe', 400)
user3 = User('Elon', 'Musk', 238000000000)

user1.deposit(200)
user1.deposit(200)
user1.deposit(200)
user1.withdraw(100)
user1.userBalance()

user2.deposit(1000)
user2.deposit(100)
user2.withdraw(100)
user2.withdraw(100)
user2.userBalance()

user3.deposit(100)
user3.withdraw(1000)
user3.withdraw(1000)
user3.withdraw(1000)
user3.userBalance()


#user1.transferMoney(user1,user2,100)
