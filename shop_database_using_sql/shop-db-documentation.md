# Shop Database

## Contents

- The contents of each table.
- Relationship between tables.
- Keys that link the records between tables.
- How to run sql queries in docker-compose.
- How to run sql queries in Adminer.

## The contents of each table.

### Customers Table:

This table lists customers' personal details, organized under the following headings:

- id
- first_name
- last_name
- gender
- address
- phone
- email
- city
- country

### Employees Table:

This table lists employees' personal details, organized under the following headings:

- id
- first_name
- last_name
- email
- job_title

### Products Table:

This table lists products available for purchase, organized under the following headings:

- id
- product_name
- description
- buy_price

### Payments Table:

This table lists payments made by customers on specific dates.
These payments are organized under the following headings:

- id
- customer_id
- payment_date
- amount

### Orders Table:

This table lists customer orders for purchased products.
These orders are organized under the following headings:

- id
- product_id
- payment_id
- fulfilled_by_employee_id
- date_required
- date_shipped

## Relationship between tables.

In the Payments Table:

- `id` (which singles out each payment) corresponds with `customer_id` to show which customers made payments.

In the Orders Table:

- `id` (which singles out each order) corresponds with `product_id`, `payment_id`, and `fulfilled_by_employee_id`.
- This lets us see which employee created a specific order for a customer who bought a specific product.

## Keys that link the records between tables.

In the Payments Table:

- The foreign key `customer_id` links the `customers` table to the `payments` table through the `id` column in the `customers` table.

In the Orders Table:

- The foreign key `product_id` links the `products` table to the `orders` table through the `id` column in the `products` table.
- The foreign key `payment_id` links the `payments` table to the `orders` table through the `id` column in the `payments` table.
- The foreign key `fulfilled_by_employee_id` links the `employees` table to the `orders` table through the `id` column in the `employees` table.

## How to run sql queries in docker-compose.

**_If you are using Windows os, WSL is recommended for this project._**

1. Start by cloning this repo using a linux terminal (WSL terminal for Windows os):

   - `git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-200-sql-.git`

2. Ensure that Docker Desktop is installed if it hasn't been already. Open Docker Desktop.

3. On the terminal, navigate to where this repo was cloned then run:

   - `docker-compose up -d`
   - run `docker ps` to see if `postgres_shop_db` is running.
   - If it is running, continue to instruction 4.
   - If it is not running, stop and remove docker containers: `docker-compose down`
   - Then check if `nhlakanipho-ngubo-200-sql-_postgres_data` docker volume exists by running: `docker volume ls`
   - If it exists, there is likely a conflict, so delete it by running: `docker volume rm nhlakanipho-ngubo-200-sql-_postgres_data`
     - Then run `docker-compose up -d` again.
   - If it does not exist, this means Docker failed to create it automatically:
     - So create it by running: `docker volume create nhlakanipho-ngubo-200-sql-_postgres_data`
     - Then run `docker-compose up -d` again.
   - Then run `docker ps`, `postgres_shop_db` should be running.
   - Continue to instruction 4.

4. Then run the following in the same terminal to open a psql prompt:

   - `docker exec -it postgres_shop_db psql -U shop_user -d shop`
     - The above command also connects to the shop database configured in docker-compose.yml, so there is no need to create a shop database.

5. To see where the sql files of this repo are mounted, run the following in the psql prompt:

   - `\! ls /docker-entrypoint-initdb.d/`

6. Create all the tables by running the following sql script:

   - `\i /docker-entrypoint-initdb.d/create-tables.sql`

7. Populate the tables by running the following sql script:

   - `\i /docker-entrypoint-initdb.d/populate-tables.sql`

8. To run queries in query-database.sql all at once:

   - `\i /docker-entrypoint-initdb.d/query-database.sql`

9. To run one sql command at a time:

   - Open a code editor.
   - On the code editor, navigate to where this repo was cloned and open it.
   - Open query-database.sql.
   - Copy the command you wish to run.
   - Paste the command in the psql prompt in the terminal.
   - Press `Enter` on your keyboard.

10. To clear the psql prompt display, run:

    - `\! clear`

11. To drop all tables, run:

    - ` DROP TABLE IF EXISTS customers, employees, payments, products, orders;`

12. To exit the psql prompt, run:

    - `\q`

13. To stop and remove docker containers, run:

    - `docker-compose down`
    - Navigate to Docker Desktop to make sure that there are no containers running and they have been removed.

## How to run sql queries in Adminer.

1.  Make sure that this repo is cloned if it hasn't been already.

    - `git clone git@github.com:Umuzi-org/Nhlakanipho-Ngubo-200-sql-.git`

2.  Open Docker Desktop

3.  Open a terminal and run:

    - `docker-compose up`

4.  Open a browser and search for:

    - localhost:8080
      - The above should open an Adminer login screen.

5.  On the login screen, enter the following information:

    - System: PostgreSQL
    - Server: postgres_shop_db
    - Username: shop_user
    - Password: shop_password
    - Database: shop

6.  Then press `Login`

7.  Navigate to `SQL command` on the left.

8.  Open a code editor, then navigate to where this repo is cloned and open that repo.

9.  Open `create-tables.sql` in the code editor, copy everything.

10. Paste the contents of `create-tables.sql` in the text box of SQL command in Adminer.

11. Press `Execute` to execute the sql commands.

12. Repeat points 7 to 11, but to execute the sql commands in `populate-tables.sql`.

13. To execute the commands in `query-database.sql`, copy and paste the command you wish to execute in `SQL command` text box, then press `Execute`.

14. To drop tables, copy and paste the following in `SQL command` text box:

    - ` DROP TABLE IF EXISTS customers, employees, payments, products, orders;`
    - Then press `Execute`

15. Press `Logout` at the top right of the screen.

16. Open a terminal in the code editor, run the following to stop and remove the docker containers:
    - `docker-compose down`
    - Check Docker Desktop to see if the containers have stopped and have been removed.
