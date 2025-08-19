from config.config_db import Base, column, integer, st, relationship

class Warehouse(Base):
    __tablename__ = "warehouse"

    warehouse_id = column(integer, primary_key=True)
    location = column(st(100), nullable=False)
    capacity = column(integer, nullable=False)

    products = relationship("Product", back_populates="warehouse")
    inventory = relationship("Inventory", back_populates="warehouse")
    transactions = relationship("Transaction", back_populates="warehouse")

    def __repr__(self):
        return f"Warehouse(id={self.warehouse_id}, location={self.location}, capacity={self.capacity})"
