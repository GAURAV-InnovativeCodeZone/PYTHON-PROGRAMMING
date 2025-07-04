'''
▶ Getters and Setters in python are often used when:
  ● We use getters & setters to add validation logic around getting and setting a value.
  ● To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.
'''

''' Code Explanation:
The code prompts the user for the account holder's name and the initial balance when creating the account.
A loop is provided to allow the user to deposit, withdraw, or set a new balance until they choose to exit.
Each action is prompted for the necessary amount, and the current balance is displayed after each operation.
'''

class Account: 
    def __init__(self, name, balance):
        self.__name = name  # Private attribute - accessible only within the class
        self.__balance = balance 

    def deposit(self, amount): 
        self.__balance += amount 

    def withdraw(self, amount):
        if amount <= self.__balance: 
            self.__balance -= amount
        else:
            print("Insufficient funds") 

    def get_balance(self):  # Getter method to access the private balance 
        return self.__balance 

    def set_balance(self, amount):  # Setter method to update the balance
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

    def get_name(self):  # Getter method to access the private name 
        return self.__name 


# Example usage with user input
name = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))
my_account = Account(name, initial_balance)

while True:
    print("\nCurrent balance:", my_account.get_balance())
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Set Balance")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        my_account.deposit(amount)
        print(f"Deposited: {amount}")

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        my_account.withdraw(amount)
        print(f"Withdrew: {amount}")

    elif choice == '3':
        amount = float(input("Enter new balance: "))
        my_account.set_balance(amount)
        print(f"Balance updated to: {amount}")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid option. Please try again.")