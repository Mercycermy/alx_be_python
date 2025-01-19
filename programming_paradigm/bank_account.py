class BankAccount:
    def __init__(self, account_balance=0):
        """Initialize the BankAccount instance with an optional initial balance."""
        self.account_balance = account_balance
        
    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount}.00")
        else:
            print("Amount must be greater than zero.")
    
    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient funds are available."""
        if amount <= 0:
            print("Amount must be greater than zero.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}.00")
            return True
        else:
            print("Insufficient funds.")
            return False
        
    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Current Balance: ${self.account_balance}.00")
