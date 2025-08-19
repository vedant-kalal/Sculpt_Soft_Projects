from config.config_db import Base, column, integer, st, fl, relationship
from sqlalchemy import ForeignKey

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = column(integer, primary_key=True)
    product_id = column(integer, ForeignKey("products.product_id",ondelete="SET NULL"),nullable=True)
    warehouse_id = column(integer, ForeignKey("warehouse.warehouse_id"), nullable=False)
    transaction_type = column(st(20), nullable=False)
    name = column(st(50), nullable=False)
    quantity = column(integer, nullable=False)
    price = column(fl, nullable=False)

    product = relationship("Product", back_populates="transactions")
    warehouse = relationship("Warehouse", back_populates="transactions")

    def __repr__(self):
        return f"Transaction(id={self.transaction_id}, product_id={self.product_id}, warehouse_id={self.warehouse_id}, transaction_type={self.transaction_type}, name={self.name}, quantity={self.quantity}, price={self.price})"

