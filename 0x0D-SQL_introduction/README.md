*********** 0x0D. SQL - Introduction ***********

What’s a database
A database is an organized collection of data, so that it can be accessed, updated and managed.

What’s a relational database
A relational database is a type of database that organizes data into rows and columns to form a table where the data points are related to each other.

What does SQL stand for
SQL stands for Structured Query Language

What’s MySQL
MySQL is a relational database management system, developed, distributed and supported by Oracle Corporation. It is named after co-founder Monty Widenius's daughter: My.

How to create a database in MySQL
To create a new database in MySQL, you use the CREATE DATABASE statement as thus:
CREATE DATABASE [IF NOT EXISTS] database_name
[CHARACTER SET charset_name]
[COLLATE collation_name];

What does DDL and DML stand for
Data Definition Language (DDL) commands help to define the structure of the databases or schema.
When we execute DDL statements, it takes effect immediately.
The changes made in the database using this command are saved permanently because its commands are auto-committed.
The following commands come under DDL language: 
CREATE
ALTER
DROP
TRUNCATE
RENAME


Data Manipulation Language (DML) is responsible for all changes that occur in the database.
The changes made in the database using this command cannot be saved permanently because its commands are not auto-committed.
Therefore, changes can be rollback. The following commands come under DML language:
SELECT
INSERT
UPDATE
DELETE
MERGE
CALL
EXPLAIN PLAN
LOCK TABLE


How to CREATE or ALTER a table
To create a table, you use this syntax:
CREATE TABLE table_name
(
column1 DATA_TYPE,
column2 DATA_TYPE CONSTRAINT,
column3 DATA_TYPE
);

To alter a table, you use this syntax:
ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE table_name RENAME TO new_table_name;
ALTER TABLE table_name RENAME COLUMN column_name TO  new_column_name ;

How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
To insert into a database, you use this syntax:
-- INSERT INTO table_name (column1, column2, column3) VALUES ("value1", "value2", "value3");
-- INSERT INTO table_name VALUES ("value1", "value2", "value3");
-- INSERT INTO table_name VALUES
('Row1-value1', 'Row1-value2', 'Row1-value3"),
('Row2-value1', 'Row2-value2', 'Row2-value3'),
('Row3-value1', 'Row3-value2', 'Row3-value3');

To update from a database, you use this syntax:
UPDATE table_name SET column1 = 'new value' WHERE column2 = 'value';
UPDATE table_name SET column1 = 'new value', column3 = 'new value' WHERE column2 = 'value';

To delete from a database, you use this syntax:
DELETE FROM table_name;
DELETE FROM table_name WHERE column1 = "value";
What are subqueries
A Subquery in SQL is a query embedded within another query, typically in the WHERE, HAVING, or FROM clauses.
It can be used with SELECT, UPDATE, INSERT, DELETE statements and various expression operators.
Subqueries are enclosed in parentheses and placed on the right side of a comparison operator.
They can be employed in single-row or multiple-row contexts, and ORDER BY is not applicable to subqueries, while GROUP BY can serve a similar purpose.
When there is no correlation with the main query, the subquery generally executes first.
Otherwise, the parser dynamically decides the execution order based on precedence.

How to use MySQL functions
MySQL functions are built-in operations or procedures that perform specific tasks and can be used in SQL statements.
This is a brief guide on how to use MySQL functions:

1. **Syntax:**
   - MySQL functions have a standard syntax, typically with the function name followed by parentheses, which may contain parameters.
   - Example: `FUNCTION_NAME(parameter1, parameter2, ...)`

2. **String Functions:**
   - Examples:
     ```sql
     SELECT CONCAT('Hello', ' ', 'World') AS greeting;
     -- Output: Hello World

     SELECT UPPER('hello') AS uppercase;
     -- Output: HELLO
     ```

3. **Mathematical Functions:**
   - Examples:
     ```sql
     SELECT ABS(-5) AS absolute_value;
     -- Output: 5

     SELECT ROUND(5.678, 2) AS rounded_number;
     -- Output: 5.68
     ```

4. **Date and Time Functions:**
   - Examples:
     ```sql
     SELECT NOW() AS current_datetime;
     -- Output: Current date and time

     SELECT DATE_FORMAT(NOW(), '%Y-%m-%d') AS formatted_date;
     -- Output: Formatted date
     ```

5. **Aggregate Functions:**
   - Used with GROUP BY for summary calculations.
   - Examples:
     ```sql
     SELECT AVG(salary) AS average_salary FROM employees;
     -- Output: Average salary

     SELECT COUNT(*) AS total_records FROM customers;
     -- Output: Total number of records
     ```

6. **Control Flow Functions:**
   - Examples:
     ```sql
     SELECT IF(salary > 50000, 'High', 'Low') AS salary_category FROM employees;
     -- Output: Salary category based on condition
     ```

7. **User-Defined Functions (UDFs):**
   - MySQL allows the creation of custom functions.
   - Example: Create a simple UDF:
     ```sql
     DELIMITER //

     CREATE FUNCTION custom_function(parameter INT)
     RETURNS INT
     BEGIN
       DECLARE result INT;
       -- Custom logic here
       RETURN result;
     END //

     DELIMITER ;
     ```

8. **Using Functions in WHERE Clause:**
   - Functions can be used in the WHERE clause to filter data.
   - Example:
     ```sql
     SELECT * FROM products WHERE LENGTH(product_name) > 10;
     -- Output: Products with names longer than 10 characters
     ```

The appropriate function to use depends on the specific task or operation you need to perform.
