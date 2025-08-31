from class_file.products import Products
from class_file.warehouse import Warehouse
from inventory_operations.operations import add_product, show_products, update_product_quantity, delete_product,add_warehouse, show_transactions, show_inventory

print("------Welcome to the Inventory Tracker System------")
print("1. Add Product")
print("2. Show Products")
print("3. Update Product Quantity")
print("4. Delete Product")
print("5. add Warehouse")
print("6. show transactions")
print("7. inventory")
print("8. Exit")

choice = input("Enter your choice (1-4): ")
if choice == '1':
    Products.product_id=int(input("Enter Product ID: "))
    Products.name=input("Enter Product Name: ")
    Products.price=float(input("Enter Product Price: "))    
    Products.quantity=int(input("Enter Product Quantity: "))
    Products.warehouse_id=int(input("Enter Warehouse ID: "))

    product = Products(Products.product_id, Products.name, Products.price, Products.quantity, Products.warehouse_id)
    result = add_product(product)
    print(result)
elif choice == '2':
    show_products()
elif choice == '3':
    product_id = int(input("Enter Product ID to update: "))
    quantity = int(input("Enter new quantity: "))
    update_product_quantity(product_id, quantity)
    print("Product quantity updated successfully")
elif choice == '4':
    product_id = int(input("Enter Product ID to delete: "))
    delete_product(product_id)
    print("Product deleted successfully")
elif choice == '5':
    warehouse_id = int(input("Enter Warehouse ID: "))
    location = input("Enter Warehouse Location: ")
    capacity = int(input("Enter Warehouse Capacity: "))
    warehouse = Warehouse(warehouse_id, location, capacity)
    result = add_warehouse(warehouse)
    print("Warehouse added successfully")
elif choice == '6':
    show_transactions()
elif choice == '7':
    show_inventory()
elif choice == '8':
    print("Exiting the Inventory Tracker System. Goodbye!")

else:
    print("Invalid choice. Please select a valid option.")

