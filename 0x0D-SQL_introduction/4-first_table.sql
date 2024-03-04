-- This script creates a table called first_table with
-- description: id INT, name VARCHAR(256) in the current database
-- The database name will be passed as an argument of the
-- mysql command and if the table first_table already exists, your script should not fail

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
EOF
