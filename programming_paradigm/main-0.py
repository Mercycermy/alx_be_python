import sys
from bank_account import BankAccount

def main():
    # Initialize the account with an example starting balance
    account = BankAccount(100)

    # Check if sufficient arguments are provided
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    # Parse the command and optional parameters
    try:
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None
    except ValueError:
        print("Invalid amount. Please provide a valid number.")
        sys.exit(1)

    # Execute the command
    if command == "deposit":
        handle_deposit(account, amount)
    elif command == "withdraw":
        handle_withdraw(account, amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")
        print_usage()

def handle_deposit(account, amount):
    if amount is not None and amount > 0:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    else:
        print("Invalid deposit amount. Please provide a positive number.")

def handle_withdraw(account, amount):
    if amount is not None and amount > 0:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid withdrawal amount. Please provide a positive number.")

def print_usage():
    print("Usage: python main.py <command>:<amount>")
    print("Commands:")
    print("  deposit:<amount> - Add funds to the account")
    print("  withdraw:<amount> - Withdraw funds from the account")
    print("  display - Display the current account balance")

if __name__ == "__main__":
    main()
