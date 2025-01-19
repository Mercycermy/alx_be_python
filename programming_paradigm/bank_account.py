class BankAccount:
    def __init__(self, account_balance=0):
        """Initializes the account with an optional balance (default is 0)."""
        self.account_balance = account_balance

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the account if funds are sufficient."""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Displays the current balance of the account."""
        print(f"Current Balance: ${self.account_balance:.2f}")
