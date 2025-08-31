from config.config_db import session, Base, engine
from class_file.transaction import Transaction
from class_file.inventory import Inventory  
from class_file.warehouse import Warehouse
from class_file.products import Product

def create_tables():
    Base.metadata.create_all(engine)

def add_warehouse(location, capacity, warehouse_id):
    new_warehouse = Warehouse(warehouse_id=warehouse_id, location=location, capacity=capacity)
    session.add(new_warehouse)
    session.commit()
    print(f"Added: {new_warehouse}")

def add_product(name, price, quantity, warehouse_id, product_id):
    try:
        new_product = Product(product_id=product_id, name=name, price=price, quantity=quantity, warehouse_id=warehouse_id)
        session.add(new_product)

        new_inventory = Inventory(warehouse_id=warehouse_id, product_id=product_id, quantity=quantity, total_price=price * quantity)
        session.add(new_inventory)

        new_transaction = Transaction(product_id=product_id, warehouse_id=warehouse_id, transaction_type="add", name=name, quantity=quantity, price=price)
        session.add(new_transaction)

        session.commit()
        print(f"Added: {new_product}")
    except Exception as e:
        session.rollback()
        print(f"Error adding product: {e}")

def show_products():
    products = session.query(Product).all()
    if products:
        for product in products:
            print(product)
    else:
        print("No products found.")
        

def update_product_quantity(product_id, new_quantity):
    try:
        product = session.query(Product).filter(Product.product_id == product_id).first()
        if product:
            product.quantity = new_quantity

            inventory = session.query(Inventory).filter(Inventory.product_id == product_id).first()
            if inventory:
                inventory.quantity = new_quantity
                inventory.total_price = product.price * new_quantity

            transaction = Transaction(product_id=product_id, warehouse_id=product.warehouse_id, transaction_type="update", name=product.name, quantity=new_quantity, price=product.price)
            session.add(transaction)

            session.commit()
            print(f"Updated: {product}")
        else:
            print("Product not found.")
    except Exception as e:
        session.rollback()
        print(f"Error updating product quantity: {e}")

def delete_product(product_id):
    try:
        product = session.query(Product).filter(Product.product_id == product_id).first()

        if product:
            # Delete inventory first
            transaction = Transaction(
                product_id=product.product_id,
                warehouse_id=product.warehouse_id,
                transaction_type="delete",
                name=product.name,
                quantity=0,
                price=0   
            )
            session.add(transaction)
            
            inventory = session.query(Inventory).filter(Inventory.product_id == product_id).first()
            session.delete(inventory)

            session.delete(product)
            session.commit()
            print(f"Deleted: {product}")
        else:
            print("Product not found.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting product : {e}")


def show_inventory():
    inventory_items = session.query(Inventory).all()
    if inventory_items:
        for inventory_item in inventory_items:
            print(inventory_item)
    else:
        print("no product in inventory")

def show_transactions():
    transactions = session.query(Transaction).all()
    for transaction in transactions:
        print(transaction)