create database buisness_intelligence;
use buisness_intelligence;


CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at DATE NOT NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE site_visits (
    visit_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    visit_date DATE NOT NULL
);


INSERT INTO customers (name, email, created_at) VALUES
('Alice Johnson', 'alice@example.com', '2025-06-05'),
('Bob Smith', 'bob@example.com', '2025-06-06'),
('Charlie Brown', 'charlie@example.com', '2025-06-07'),
('Diana Prince', 'diana@example.com', '2025-06-08'),
('Ethan Hunt', 'ethan@example.com', '2025-06-09'),
('Fiona Gallagher', 'fiona@example.com', '2025-06-10'),
('George Miller', 'george@example.com', '2025-06-11'),
('Hannah Lee', 'hannah@example.com', '2025-06-12'),
('Ian Carter', 'ian@example.com', '2025-06-13'),
('Julia Evans', 'julia@example.com', '2025-06-14');


INSERT INTO products (name, category, price) VALUES
('Laptop', 'Electronics', 800.00),
('Smartphone', 'Electronics', 500.00),
('Headphones', 'Accessories', 50.00),
('Coffee Mug', 'Kitchen', 10.00),
('Desk Chair', 'Furniture', 150.00),
('Tablet', 'Electronics', 300.00),
('Smartwatch', 'Electronics', 400.00),
('Backpack', 'Accessories', 40.00),
('Microwave', 'Kitchen', 200.00),
('Dining Table', 'Furniture', 550.00);


INSERT INTO orders (customer_id, total_amount, order_date) VALUES
(1, 860.00, '2025-07-02'),
(2, 500.00, '2025-07-03'),
(3, 150.00, '2025-07-04'),
(4, 1300.00, '2025-07-05'),
(5, 600.00, '2025-07-06'),
(6, 300.00, '2025-07-07'),
(7, 950.00, '2025-07-08'),
(8, 400.00, '2025-07-09'),
(9, 750.00, '2025-07-10'),
(10, 1200.00, '2025-07-11'),
(1, 500.00, '2025-07-15'),
(3, 400.00, '2025-07-16'),
(5, 700.00, '2025-07-17'),
(7, 300.00, '2025-07-18'),
(8, 200.00, '2025-07-19');


INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 800.00), (1, 3, 1, 60.00),
(2, 2, 1, 500.00),
(3, 4, 15, 10.00),
(4, 10, 2, 550.00), (4, 7, 1, 200.00),
(5, 6, 2, 300.00),
(6, 5, 2, 150.00),
(7, 8, 10, 40.00), (7, 3, 1, 50.00),
(8, 9, 2, 200.00),
(9, 1, 1, 800.00),
(10, 2, 2, 500.00),
(11, 6, 1, 300.00),
(12, 7, 1, 400.00),
(13, 10, 1, 550.00),
(14, 5, 2, 150.00),
(15, 4, 20, 10.00);


INSERT INTO site_visits (customer_id, visit_date) VALUES
(1, '2025-07-01'), (1, '2025-07-02'),
(2, '2025-07-03'), (2, '2025-07-04'),
(3, '2025-07-04'), (3, '2025-07-05'),
(4, '2025-07-05'), (4, '2025-07-06'),
(5, '2025-07-06'), (5, '2025-07-07'),
(6, '2025-07-07'), (6, '2025-07-08'),
(7, '2025-07-08'), (7, '2025-07-09'),
(8, '2025-07-09'), (8, '2025-07-10'),
(9, '2025-07-10'), (9, '2025-07-11'),
(10, '2025-07-11'), (10, '2025-07-12');



