-- prepares a MySQL test server for the project

CREATE DATABASE IF NOT EXISTS kasi_kos_test_db;
CREATE USER IF NOT EXISTS 'kasi_kos_test'@'localhost' IDENTIFIED BY 'kasi_kos_test_pwd_667#';
GRANT ALL PRIVILEGES ON `kasi_kos_test_db`.* TO 'kasi_kos_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'kasi_kos_test'@'localhost';
FLUSH PRIVILEGES;