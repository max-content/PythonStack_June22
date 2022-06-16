class BankAccount:
	def __init__(self, balance, int_rate): # don't forget to add some default values for these parameters!
		# your code here! (remember, this is where we specify the attributes for our class)
		# don't worry about user info here; we'll involve the User class soon
		self.int_rate = int_rate
		self.balance = balance

	def deposit(self, amount):
		# deposit(self, amount) - increases the account balance by the given amount taking in the parameters of self and amount
		self.balance += amount
		print(f'balance is {self.balance} you deposited {amount}')
		return self

	def withdraw(self, amount):
		# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
		fee = 5
		self.balance -= amount
		if self.balance <= 0:
			self.balance -= fee
			print('Insufficient funds: You have been charged a $5 fee')
		else:
			print(f'balance is {self.balance} you withrew {amount}')
		return self

	def display_account_info(self):
		# display_account_info(self) - print to the console: eg. "Balance: $100"
		print(f'balance is {self.balance}')
		return self

	def yield_interest(self):
		# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
		while self.balance > 0:
			self.balance = self.balance + (self.balance * self.int_rate)
			print(f'balance is {self.balance}')
			return self

user1 = BankAccount(1000, 0.02)
user2 = BankAccount(1500, 0.02)
user1.display_account_info()
user2.display_account_info()
user2.deposit(100000).deposit(10000).deposit(400).yield_interest()
user1.deposit(75000).deposit(1500).withdraw(75000).withdraw(25).withdraw(5).yield_interest()