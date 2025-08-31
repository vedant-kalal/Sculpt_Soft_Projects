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

