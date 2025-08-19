from operations_file.operations import (
    create_tables, add_warehouse, add_product,
    show_products, update_product_quantity,
    delete_product, show_inventory, show_transactions
)

print("Welcome to the Inventory Tracker!")
create_tables()

print("1. Add Warehouse")
print("2. Add Product")
print("3. Show Products")
print("4. Update Product Quantity")
print("5. Delete Product")
print("6. Show Inventory")
print("7. Show Transactions")
print("8. Exit")

input_choice = input("Enter your choice: ")

if input_choice == "1":
    location = input("Enter warehouse location: ")
    capacity = int(input("Enter warehouse capacity: "))
    warehouse_id = int(input("Enter warehouse ID: "))
    add_warehouse(location, capacity, warehouse_id)

elif input_choice == "2":
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    warehouse_id = int(input("Enter warehouse ID for the product: "))
    product_id = int(input("Enter product ID: "))
    add_product(name, price, quantity, warehouse_id, product_id)

elif input_choice == "3":
    show_products()

elif input_choice == "4":
    product_id = int(input("Enter product ID to update: "))
    new_quantity = int(input("Enter new quantity: "))
    update_product_quantity(product_id, new_quantity)

elif input_choice == "5":
    product_id = int(input("Enter product ID to delete: "))
    delete_product(product_id)

elif input_choice == "6":
    show_inventory()

elif input_choice == "7":
    show_transactions()

elif input_choice == "8":
    print("Exiting the Inventory Tracker. Goodbye!")

else:
    print("Invalid choice. Please try again.")
