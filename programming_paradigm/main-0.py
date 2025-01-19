import sys
from bank_account import BankAccount

def main():
    # Create an account with an initial balance of 100
    account = BankAccount(100)

    # Check if sufficient arguments are provided
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    # Parse the command and optional parameters
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")
        print_usage()

def print_usage():
    """Displays usage instructions."""
    print("Usage: python main-0.py <command>:<amount>")
    print("Commands:")
    print("  deposit:<amount> - Deposit funds into the account")
    print("  withdraw:<amount> - Withdraw funds from the account")
    print("  display - Display the current account balance")

if __name__ == "__main__":
    main()
