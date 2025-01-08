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
        choice = input("Enter your choice: ").strip()
        
        
        if not choice.isdigit() or int(choice) not in range(1, 5):
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        choice = int(choice)  
        
        if choice == 1:
            
            item = input("Enter the item you want to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item cannot be empty.")
        
        elif choice == 2:
           
            item = input("Enter the item you want to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")
        
        elif choice == 3:
            
            print("\nYour Shopping List:")
            if shopping_list:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == 4:
            
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
