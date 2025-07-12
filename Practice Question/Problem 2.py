'''
Create account class with two attribites - balance and account number.
Create a method for debit, credit and display balance.
Create two objects of the class and perform debit and credit operations.
'''
class Account:
    def __init__(self, balance, account_number):
        self.balance = balance 
        self.account_number = account_number
        
    def debit(self, amount):
        self.balance -= amount
        print('Rs.', amount, 'debited. Now total balance:', self.balance)
        
    def credit(self, amount):
        self.balance += amount
        print('Rs.', amount, 'credited. Now total balance:', self.balance)
        
    def display_balance(self):
        print('Current balance:', self.balance)
        
acc = Account(100000, '123456789')
print(f'Account Number: {acc.account_number}, Initial Balance: {acc.balance}')
acc.debit(int(input('Enter amount to debit: ')))
acc.credit(int(input('Enter amount to credit: ')))
acc.display_balance()
