class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)

    def generate_account_statements(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}")
            print(f"Customer Name: {account.customer.name}")
            print(f"Balance: {account.balance}")

class Customer:
    def __init__(self, name):
        self.name = name

class Account:
    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.customer = customer
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

# creating derived class checking account from
# account class.  Checking account will add
# a transaction fee 
class CheckingAccount(Account):
    def __init__(self, amount, customer, fee):
        super().__init__(amount,customer)
        self.fee = fee
    
    def deposit(self,amount):
        super().deposit(amount + self.fee)

    def withdraw(self, amount):
        return super().withdraw(amount + self.fee)
         

# Create objects and perform banking operations
customer1 = Customer("John Doe")
account1 = Account(12345, customer1)
account1.deposit(1000)
account1.withdraw(500)

customer2 = Customer("Jane Smith")
account2 = Account(54321, customer2)
account2.deposit(2000)

account3 = CheckingAccount(11111, customer2, .50)
account3.deposit(20)
account3.deposit(5000)
account3.withdraw(5000)

bank = Bank("MyBank")
bank.create_account(account1)
bank.create_account(account2)
bank.create_account(account3)
bank.generate_account_statements()
