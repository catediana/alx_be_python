class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulation: Use a private attribute
        self.__account_balance = initial_balance

    def deposit(self, amount):
        #Adding the specified amount to the account balance.
        self.__account_balance = self.__account_balance + amount

    def withdraw(self, amount):
        #Deducting the amount from the account balance if there is sufficient funds.
        if self.__account_balance >= amount:
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False

    def display_balance(self):
        #Printing  the current balance.
        print(f"Current Balance: {self.__account_balance}")

# Example Usage
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.display_balance()  # Output: Current Balance: 120
