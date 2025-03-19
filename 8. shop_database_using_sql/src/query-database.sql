-- 1. Select all records from the Customers table.
SELECT
    *
FROM
    customers;

-- 2. Select only the FirstName column from the Customers table
SELECT
    first_name
FROM
    customers;

-- 3. Display the full name of the customer with CustomerID 1.
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name
FROM
    customers
WHERE
    id = 1;

-- 4. Update the record for CustomerID 1 in the Customers table to change the name to “Lerato Mabitso”.
UPDATE customers
SET
    first_name = 'Lerato',
    last_name = 'Mabitso'
WHERE
    id = 1;

-- 5. Delete the record for the customer with CustomerID 2 from the Customers table.
DELETE FROM customers
WHERE
    id = 2;

-- 6. Select all unique statuses from the Orders table and count the number of orders for each status.
SELECT
    status,
    COUNT(*) AS number_of_orders
FROM
    orders
GROUP BY
    status;

-- 7. Return the maximum payment made in the Payments table.
SELECT
    MAX(amount)
FROM
    payments;

-- 8. Select all customers from the Customers table, sorted by the Country column.
SELECT
    *
FROM
    customers
ORDER BY
    country ASC;

-- 9. Select all products with a price between R100 and R600.
SELECT
    *
FROM
    products
WHERE
    buy_price BETWEEN 100 AND 600;

-- 10. Select all fields from Customers where the Country is “Germany” AND the City is “Berlin”.
SELECT
    *
FROM
    customers
WHERE
    country = 'Germany'
    AND city = 'Berlin';

-- 11. Select all fields from Customers where the City is either “Cape Town” OR “Durban”.
SELECT
    *
FROM
    customers
WHERE
    city = 'Cape Town'
    OR city = 'Durban';

-- 12. Select all records from Products where the price is greater than R500.
SELECT
    *
FROM
    products
WHERE
    buy_price > 500;

-- 13. Return the total sum of the amounts in the Payments table.
SELECT
    SUM(amount)
FROM
    payments;

-- 14. Count the number of shipped orders in the Orders table.
SELECT
    COUNT(status) AS shipped_orders
FROM
    orders
WHERE
    status = 'Shipped';

-- 15. Return the average price of all products, both in Rands and in Dollars (assuming the exchange rate is R12 to the Dollar).
SELECT
    CONCAT('R', CAST(ROUND(AVG(buy_price), 2) AS VARCHAR)) AS in_rands,
    CONCAT(
        '$',
        CAST(ROUND(AVG(buy_price / 12), 2) AS VARCHAR)
    ) AS in_dollars
FROM
    products;

-- 16. Using an INNER JOIN, create a query that selects all payments along with the corresponding customer information.
SELECT
    *
FROM
    payments
    INNER JOIN customers ON payments.customer_id = customers.id;

-- 17. Select all products that have turnable front wheels.
SELECT
    *
FROM
    products
WHERE
    description ILIKE '%turnable front wheels%';