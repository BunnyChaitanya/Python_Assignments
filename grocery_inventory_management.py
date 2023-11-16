# grocery_inventory_management.py

# Initialize an empty inventory
inventory = []

# Function to add a new item to the inventory
def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    item_type = input("Enter item type (kg, each, liters, etc.): ")
    
    # Create a dictionary to represent the item
    item = {"name": name, "quantity": quantity, "price": price, "item_type": item_type}
    
    # Add the item to the inventory
    inventory.append(item)
    print(f"{name} has been added to the inventory.\n")

# Function to update the information of an existing item
def update_item():
    name = input("Enter the name of the item to update: ")
    
    # Find the item in the inventory
    for item in inventory:
        if item["name"] == name:
            print("Select the information to update:")
            print("1. Name")
            print("2. Quantity")
            print("3. Price")
            print("4. Item Type")
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                new_name = input("Enter the new name: ")
                item["name"] = new_name
                print(f"Name of {name} updated to {new_name}\n")
            elif choice == "2":
                new_quantity = int(input("Enter the new quantity: "))
                item["quantity"] = new_quantity
                print(f"Quantity of {name} updated. New quantity: {new_quantity}\n")
            elif choice == "3":
                new_price = float(input("Enter the new price: "))
                item["price"] = new_price
                print(f"Price of {name} updated. New price: ${new_price}\n")
            elif choice == "4":
                new_item_type = input("Enter the new item type: ")
                item["item_type"] = new_item_type
                print(f"Item type of {name} updated to {new_item_type}\n")
            else:
                print("Invalid choice. No updates made.\n")
            return
    
    # If the item is not found
    print(f"Item '{name}' not found in the inventory.\n")

# Function to view the current inventory
def view_inventory():
    print("\nCurrent Inventory:")
    for item in inventory:
        print(f"{item['name']} - Quantity: {item['quantity']} {item['item_type']}, Price: ${item['price']} each")
    print()

# Function to remove an item from the inventory
def remove_item():
    name = input("Enter the name of the item to remove: ")
    
    # Find the item in the inventory
    for item in inventory:
        if item["name"] == name:
            # Remove the item
            inventory.remove(item)
            print(f"{name} has been removed from the inventory.\n")
            return
    
    # If the item is not found
    print(f"Item '{name}' not found in the inventory.\n")

# Main program loop
while True:
    print("Menu:")
    print("1. Add new item to inventory")
    print("2. Update item information")
    print("3. View current inventory")
    print("4. Remove item from inventory")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_item()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")
