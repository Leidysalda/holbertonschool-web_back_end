-- 0. We are all unique
--SQL script that creates a table users
CRAETE TABLE IF NOT EXIST users (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255)
);