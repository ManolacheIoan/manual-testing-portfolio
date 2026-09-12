-- ============================================
-- E-commerce practice schema + queries
-- Covers: JOINs, aggregation, integrity checks
-- ============================================

-- SCHEMA
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC(10,2)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    order_date DATE,
    status VARCHAR(50)
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER
);

-- SAMPLE DATA
INSERT INTO users (name, email) VALUES
('Ana Popescu', 'ana@test.com'),
('Bogdan Ionescu', 'bogdan@test.com'),
('Carmen Radu', 'carmen@test.com');

INSERT INTO products (name, price) VALUES
('Laptop', 3500.00),
('Mouse', 50.00),
('Tastatura', 150.00);

INSERT INTO orders (user_id, order_date, status) VALUES
(1, '2026-09-01', 'completed'),
(1, '2026-09-05', 'pending'),
(2, '2026-09-03', 'completed');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(3, 1, 1);

-- ============================================
-- 3.1: JOINs
-- ============================================

-- INNER JOIN: only users with at least one order (Carmen excluded)
SELECT users.name, orders.id AS order_id, orders.status
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- LEFT JOIN: all users, including those with no orders (Carmen appears with NULLs)
SELECT users.name, orders.id AS order_id, orders.status
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

-- Find users with NO orders at all (classic LEFT JOIN + IS NULL pattern)
SELECT users.name
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.id IS NULL;

-- ============================================
-- 3.2: Aggregation
-- ============================================

-- Order count per user (includes 0 for users with no orders)
SELECT users.name, COUNT(orders.id) AS total_orders
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.name;

-- Only users with more than 1 order (HAVING filters post-aggregation)
SELECT users.name, COUNT(orders.id) AS total_orders
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.name
HAVING COUNT(orders.id) > 1;

-- Total spent per user (INNER JOIN is correct here — a user with
-- no orders has nothing to sum, so absence from the report is
-- the correct signal, not a 0)
SELECT users.name, SUM(products.price * order_items.quantity) AS total_spent
FROM users
INNER JOIN orders ON users.id = orders.user_id
INNER JOIN order_items ON orders.id = order_items.order_id
INNER JOIN products ON order_items.product_id = products.id
GROUP BY users.name;

-- ============================================
-- 3.3: Data integrity checks
-- ============================================

-- Orphaned order_items: rows referencing a non-existent order
-- (should return 0 rows if FOREIGN KEY constraints are enforced)
SELECT order_items.id, order_items.order_id
FROM order_items
LEFT JOIN orders ON order_items.order_id = orders.id
WHERE orders.id IS NULL;

-- Duplicate emails (should return 0 rows if email uniqueness holds)
SELECT email, COUNT(*) AS count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
