-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS kasi_kos_dev_db;
CREATE USER IF NOT EXISTS 'kasi_kos_dev'@'localhost' IDENTIFIED BY 'kasi_kos_dev_pwd_50584';
GRANT ALL PRIVILEGES ON `kasi_kos_dev_db`.* TO 'kasi_kos_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'kasi_kos_dev'@'localhost';
FLUSH PRIVILEGES;