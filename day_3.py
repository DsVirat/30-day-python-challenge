# Inventory Tracking System

inventory = {"pen" : {"Quantity":15,"Price":5},
             "pencil": {"Quantity":20, "Price":10},
             "boxes": {"Quantity":10, "Price":30},
             "notebooks": {"Quantity":20, "Price":50},
             "books": {"Quantity":5, "Price":100}
             }

while True:
    print('''Welcome To Inventory
Here's your inventory menu''')
    print('1. View Inventory')
    print('2. Add New Item')
    print('3. Update The Quantity Of An Item')
    print('4. Delete An Item')
    print('5. Exit the System')

    choice = input("Make your choice (1-5): ")

    match choice:
        case "1":
            if not inventory:
                print("Inventory is empty")
            else:
                for item, value in inventory.items():
                    print(f"Item: {item}| Quantity: {value['Quantity']}| Price: ₹{value['Price']}")

        case "2":
            item = input("Enter item name: ")
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price : "))
            if item in inventory:
                print("Item already exists. Choose 3 to update.")
            else:
                inventory[item] = {"Quantity": quantity, "Price": price}
                print(f"{item} added to the inventory")

        case "3":
            item = input("Enter item name: ")
            if item in inventory:
                quantity = int(input("Enter the quantity: "))
                inventory[item]["Quantity"] += quantity
                print(f"Quantity Updated !! New Quantity of {item} is {inventory[item]['Quantity']}")
            else:
                print(f"{item} not present in Inventory. Choose 2 to add item.")

        case "4":
            item = input("Enter the item name to be deleted: ")
            if item not in inventory:
                print(f"{item} is not present in the Inventory.")
            else:
                del inventory[item]
                print(f"{item} deleted from the Inventory.")

        case "5":
            print("Existing from system!! Goodbye.")
            break

        case _:
            print("Invalid choice. Please enter 1 to 5.")