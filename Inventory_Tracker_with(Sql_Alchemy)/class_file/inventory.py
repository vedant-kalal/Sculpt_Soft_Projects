from config.config_db import Base, column, integer, fl, relationship
from sqlalchemy import ForeignKey

class Inventory(Base):
    __tablename__ = "inventory"

    warehouse_id = column(integer, ForeignKey("warehouse.warehouse_id"), primary_key=True, nullable=False)
    product_id = column(integer, ForeignKey("products.product_id"), primary_key=True, nullable=False)
    quantity = column(integer, nullable=False)
    total_price = column(fl, nullable=False)

    warehouse = relationship("Warehouse", back_populates="inventory")
    product = relationship("Product", back_populates="inventory")

    def __repr__(self):
        return f"Inventory(warehouse_id={self.warehouse_id}, product_id={self.product_id}, quantity={self.quantity}, total_price={self.total_price})"
