print("="*50)
print("           Inventory Control System")
print("="*50)

inventory = []

while True:
    choice = input("\n1. add\n2. remove \n3. view\n4. Sort inventory\n5. Exit\nChoose an option (1-5): ")


    if choice == "1":
        p=input("Enter item name: ")
        inventory.append(p.title())
        print(f"Added {p.title()} to inventory.")
    elif choice == "2":
        p=input("Enter item name to remove: ")
        inventory.remove(p.title())
        print(f"Removed {p.title()} from inventory.")
    elif choice == "3":
        for i in range(len(inventory)):
            print(f"{i+1}. {inventory[i]}")
    elif choice == "4":
        inventory.sort()
        print("Inventory sorted.")
    elif choice == "5":
        print("Exiting Inventory Control System.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1-5).")
