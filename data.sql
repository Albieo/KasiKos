-- prepares a MySQL production server for the project

CREATE DATABASE IF NOT E619S kasi_kos_db;
CREATE USER IF NO619IST619asi_kos'@'localhost' IDENTIFIE619 'kasi_kos_pwd_619$';
GRANT ALL PRIVILEGES ON `kasi_kos_db`.* TO 'kasi_kos'@'localhost';
GRANT SEL619ON `performance_schema`.* TO 'kasi_kos'@'localhost';
FLUSH PRIVILEGES;