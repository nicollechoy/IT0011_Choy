class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price:.2f}"

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self):
        try:
            item_id = input("Enter item ID: ").strip()
            if item_id in self.items:
                print("Error: Item ID already exists.")
                return
            
            name = input("Enter item name: ").strip()
            description = input("Enter item description: ").strip()
            price = float(input("Enter item price: "))

            if price < 0:
                print("Error: Price cannot be negative.")
                return

            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!")

        except ValueError:
            print("Invalid input. Price must be a number.")

    def read_items(self):
        if not self.items:
            print("No items available.")
            return
        for item in self.items.values():
            print(item)

    def update_item(self):
        item_id = input("Enter the item ID to update: ").strip()
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        
        name = input("Enter new item name: ").strip()
        description = input("Enter new item description: ").strip()
        
        try:
            price = float(input("Enter new item price: "))
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item updated successfully!")
        
        except ValueError:
            print("Invalid input. Price must be a number.")

    def delete_item(self):
        item_id = input("Enter the item ID to delete: ").strip()
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Error: Item not found.")

def main():
    manager = ItemManager()
    
    while True:
        print("\nItem Management System")
        print("[C] - Create Item")
        print("[R] - Read Items")
        print("[U] - Update Item")
        print("[D] - Delete Item")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'C':
            manager.create_item()
        elif choice == 'R':
            manager.read_items()
        elif choice == 'U':
            manager.update_item()
        elif choice == 'D':
            manager.delete_item()
        elif choice == 'Q':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
