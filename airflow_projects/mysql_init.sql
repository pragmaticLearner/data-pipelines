CREATE DATABASE airflow_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'admin' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON airflow_db.* TO 'admin';