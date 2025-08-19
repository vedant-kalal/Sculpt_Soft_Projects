create database inventory_tracker;
use inventory_tracker;
-- Create warehouse table
CREATE TABLE IF NOT EXISTS warehouse (
    warehouse_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(100) UNIQUE,   -- Unique warehouse location
    capacity INT not null               -- Max quantity of products it can store
);
-- Create product table
CREATE TABLE product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE,   -- Unique product name
    quantity INT not null check (quantity>0),               -- Number of items in stock
    price DECIMAL(10,2),        -- Price per unit
    warehouse_id INT,           -- Foreign key to warehouse table
    FOREIGN KEY (warehouse_id) REFERENCES warehouse(warehouse_id)
);
CREATE TABLE inventory (
    product_id INT,
    warehouse_id INT,
    quantity INT,
    PRIMARY KEY (product_id, warehouse_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouse(warehouse_id)
    );
CREATE TABLE transaction_table (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    name VARCHAR(100),
    price FLOAT,
    transaction_type VARCHAR(10), -- 'ADD', 'DELETE', 'UPDATE'
    quantity INT,
    warehouse_id INT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouse(warehouse_id)
);
