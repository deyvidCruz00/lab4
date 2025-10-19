CREATE DATABASE IF NOT EXISTS customerorders;
CREATE USER IF NOT EXISTS 'exporter'@'%' IDENTIFIED BY 'exporter_password';
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'%';
CREATE USER IF NOT EXISTS 'appuser'@'%' IDENTIFIED BY 'app_password';
GRANT ALL PRIVILEGES ON customerorders.* TO 'appuser'@'%';
FLUSH PRIVILEGES;
