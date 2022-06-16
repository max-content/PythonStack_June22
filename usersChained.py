class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        print(f'{self.name} balance is {self.balance} you deposited {amount}')
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        print(f'{self.name} balance is {self.balance} you withrew {amount}')
        return self

    def display_user_balance(self):
        print(f'{self.name} balance is {self.balance}')
        return self
    
    def transfer_money(self, other_user, amount):
        #withdraw ammount from user account
        #deposit ammount to recipient account
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f'{other_user.name} has received your transfer of {amount}')
        return self


user1 = User("Beth")
user2 = User("Alison")
user3 = User("Cosima")

user2.make_deposit(100000).make_deposit(5000).transfer_money(user1, 75000)
user3.make_withdrawal(100)
user1.display_user_balance()


# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance