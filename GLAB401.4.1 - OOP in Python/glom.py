class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = []

    def get_accounts(self):
        return self.__accounts

    def create_account(self, account):
        self.__accounts.append(account)

    def generate_account_statements(self):
        for account in self.__accounts:
            print(f"Account Number: {account.get_account_no()}")
            print(f"Customer Name: {account.get_customer_name()}")
            print(f"Balance: {account.get_balance()}")

class Customer:
    def __init__(self, name):
        self.__name = name
        self.name = self.__name.upper()
    def get_customer_name(self):
        return self.__name

class Account:
    def __init__(self, account_number, customer):
        self.__account_number = account_number
        self.__customer = customer
        self.__balance = 0
    
    def get_balance(self):
        return self.__balance
    
    def get_account_no(self):
        return self.__account_number
    
    def get_customer_name(self):
        return self.__customer.get_customer_name()

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

# creating derived class checking account from
# account class.  Checking account will add
# a transaction fee 
class CheckingAccount(Account):
    def __init__(self, amount, customer, fee):
        super().__init__(amount,customer)
        self.__fee = fee
    
    # override base-class methods and add the fee
    def deposit(self,amount):
        super().deposit(amount + self.__fee)

    def withdraw(self, amount):
        return super().withdraw(amount + self.__fee)
    
class SavingsAccount(Account):
    def __init__(self, amount, customer, rate):
        super().__init__(amount,customer)
        self.__rate = rate
    
    # multiply balance by rate to get
    # interest then use base class
    # to deposit that amount
    def ApplyInterest(self):
        interest = self.get_balance() * self.__rate
        self.deposit(interest)

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

account4 = SavingsAccount(21211, customer1, .04)
account4.deposit(1000)
account4.ApplyInterest()

bank = Bank("MyBank")
bank.create_account(account1)
bank.create_account(account2)
bank.create_account(account3)
bank.create_account(account4)
bank.generate_account_statements()
