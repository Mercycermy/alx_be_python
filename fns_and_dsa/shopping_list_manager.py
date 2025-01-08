def display_menu():
    """Display the menu options."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """Main function to manage the shopping list."""
    shopping_list = [] 
    
    while True:
        display_menu()  
        choice = input("Enter your choice (1-4): ").strip()  

        if choice == '1':
            # Prompt for and add an item
            item = input('Enter the item to add: ')
            shopping_list.append(item)
        elif choice == '2':
            # Prompt for and remove an item
            item = input('Enter the item to remove: ')
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print('This item is not in your shopping list.')
        elif choice == '3':
            # Display the shopping list
            print("\nCurrent Shopping List:")
            if shopping_list:  # Check if the list is not empty
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")  # Print each item
            else:
                print("The shopping list is empty.")  # Handle empty list case
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
