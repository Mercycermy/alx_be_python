def display_menu():
    """Display the menu options."""
    print("\nShopping List Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Add an item you want: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == '2':
            item = input("Remove an item you don't want: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")
        
        elif choice == '3':
            print("\nYour shopping list:")
            if shopping_list:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
