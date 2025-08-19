from config.config_db import Base, column, integer, st, fl, relationship
from sqlalchemy import ForeignKey

class Product(Base):
    __tablename__ = "products"

    product_id = column(integer, primary_key=True)
    name = column(st(50), nullable=False)
    price = column(fl, nullable=False)
    quantity = column(integer, default=0)
    warehouse_id = column(integer, ForeignKey("warehouse.warehouse_id"), nullable=False)

    warehouse = relationship("Warehouse", back_populates="products")
    inventory = relationship("Inventory", back_populates="product")
    transactions = relationship("Transaction", back_populates="product",passive_deletes=True )

    def __repr__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price}, quantity={self.quantity}, warehouse_id={self.warehouse_id})"
