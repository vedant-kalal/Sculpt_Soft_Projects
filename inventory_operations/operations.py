# There is no code at the $SELECTION_PLACEHOLDER$ location. 
# This placeholder should be removed or replaced with actual code if needed.
from class_file.warehouse import Warehouse
from config.config_connect import get_db_connection
from class_file.products import Products

def add_product(product:Products):
    connection=get_db_connection()
    if not isinstance(product.product_id,int) or not isinstance(product.name,str) or not isinstance(product.price,float) or not isinstance(product.quantity,int) or not isinstance(product.warehouse_id,int):
        return "Invalid product data types" 
    
    cursor=connection.cursor()
    query="INSERT INTO product (product_id, name, price, quantity, warehouse_id) VALUES (%s, %s, %s, %s, %s)"
    values=(product.product_id, product.name, product.price, product.quantity, product.warehouse_id)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return "Product added successfully"
    

def show_products():
    connection=get_db_connection()
    cursor=connection.cursor()
    query="SELECT * FROM product"  
    cursor.execute(query)
    products=cursor.fetchall()  
    for product in products:
        print(f"Product ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}, Warehouse ID: {product[4]}")
    connection.close()

def update_product_quantity(product_id:int, quantity:int):
    connection=get_db_connection()
    cursor=connection.cursor()
    query="UPDATE product SET quantity = %s WHERE product_id = %s"
    values=(quantity, product_id)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return "Product quantity updated successfully"

def delete_product(product_id:int):
    connection=get_db_connection()
    cursor=connection.cursor()
    query="DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    connection.commit()
    connection.close()
    return "Product deleted successfully"

def add_warehouse(warehouse:Warehouse):
    connection=get_db_connection()
    if not isinstance(warehouse.warehouse_id,int) or not isinstance(warehouse.location,str) or not isinstance(warehouse.capacity,int):
        return "Invalid warehouse data types"
    
    cursor=connection.cursor()
    query="INSERT INTO warehouse (warehouse_id, location, capacity) VALUES (%s, %s, %s)"
    values=(warehouse.warehouse_id, warehouse.location, warehouse.capacity)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return "Warehouse added successfully"



    