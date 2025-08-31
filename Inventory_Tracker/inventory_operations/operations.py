from class_file.warehouse import Warehouse
from config.config_connect import get_db_connection
from class_file.products import Products

# Add a product: adds to product table, inventory, and logs transaction
def add_product(product: Products):
    connection = get_db_connection()

    if not isinstance(product.product_id, int) or \
       not isinstance(product.name, str) or \
       not isinstance(product.price, float) or \
       not isinstance(product.quantity, int) or \
       not isinstance(product.warehouse_id, int):
        return "Invalid product data types"

    try:
        cursor = connection.cursor()

        # Insert product
        cursor.execute("""
            INSERT INTO product (product_id, name, price, quantity, warehouse_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (product.product_id, product.name, product.price, product.quantity, product.warehouse_id))

        # Insert into inventory
        cursor.execute("""
            INSERT INTO inventory (product_id, warehouse_id, quantity)
            VALUES (%s, %s, %s)
        """, (product.product_id, product.warehouse_id, product.quantity))

        # Log transaction
        cursor.execute("""
            INSERT INTO transaction_table (product_id, name, price, transaction_type, quantity, warehouse_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (product.product_id, product.name, product.price, "ADD", product.quantity, product.warehouse_id))

        connection.commit()
        return "Product added, inventory updated, transaction logged"

    except Exception as e:
        connection.rollback()
        return f"Error: {e}"

    finally:
        connection.close()

#  Show all products
def show_products():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()

    print("\n All Products:")
    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}, Warehouse: {product[4]}")

    connection.close()

# Update quantity in product & inventory, and log transaction
def update_product_quantity(product_id: int, new_quantity: int):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()

        # Update product
        cursor.execute("UPDATE product SET quantity = %s WHERE product_id = %s", (new_quantity, product_id))

        # Update inventory
        cursor.execute("UPDATE inventory SET quantity = %s WHERE product_id = %s", (new_quantity, product_id))

        # Log transaction
        cursor.execute("""
            INSERT INTO transaction_table (product_id, name, price, transaction_type, quantity, warehouse_id)
            SELECT product_id, name, price, %s, %s, warehouse_id FROM product WHERE product_id = %s
        """, ("UPDATE", new_quantity, product_id))

        connection.commit()
        return "Product & inventory updated, transaction logged"

    except Exception as e:
        connection.rollback()
        return f"Error: {e}"

    finally:
        connection.close()

# Delete product & inventory, log as DELETE
def delete_product(product_id: int):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()

        # Get product before deleting
        cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
        product = cursor.fetchone()
        if not product:
            return "Product not found"

        # Delete from product
        cursor.execute("DELETE FROM product WHERE product_id = %s", (product_id,))

        # Delete from inventory
        cursor.execute("DELETE FROM inventory WHERE product_id = %s", (product_id,))

        # Log transaction
        cursor.execute("""
            INSERT INTO transaction_table (product_id, name, price, transaction_type, quantity, warehouse_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (product[0], product[1], product[2], "DELETE", product[3], product[4]))

        connection.commit()
        return "Product deleted, inventory cleared, transaction logged"

    except Exception as e:
        connection.rollback()
        return f"Error: {e}"

    finally:
        connection.close()

# Add a warehouse
def add_warehouse(warehouse: Warehouse):
    connection = get_db_connection()

    if not isinstance(warehouse.warehouse_id, int) or \
       not isinstance(warehouse.location, str) or \
       not isinstance(warehouse.capacity, int):
        return "Invalid warehouse data types"

    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO warehouse (warehouse_id, location, capacity)
            VALUES (%s, %s, %s)
        """, (warehouse.warehouse_id, warehouse.location, warehouse.capacity))

        connection.commit()
        return "Warehouse added"

    except Exception as e:
        connection.rollback()
        return f"Error: {e}"

    finally:
        connection.close()

#Show all inventory
def show_inventory():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory")
    inventory_data = cursor.fetchall()

    print("\n Inventory Table:")
    for row in inventory_data:
        print(f"Product ID: {row[0]}, Warehouse ID: {row[1]}, Quantity: {row[2]}")

    connection.close()

# Show all transactions
def show_transactions():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transaction_table")
    transactions = cursor.fetchall()

    print("\n Transaction Log:")
    for tx in transactions:
        print(f"ID: {tx[0]}, Product ID: {tx[1]}, Name: {tx[2]}, Price: {tx[3]}, Type: {tx[4]}, Qty: {tx[5]}, Warehouse_ID: {tx[6]}")

    connection.close()
