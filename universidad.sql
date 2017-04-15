CREATE DATABASE universidad;
USE universidad;

CREATE TABLE tipo_clase(
 id_tipo_clase INT (10) AUTO_INCREMENT PRIMARY KEY,
 nombre_tipo_clase VARCHAR(30) UNIQUE
);

CREATE TABLE clase(
 id_clase INT(10) AUTO_INCREMENT PRIMARY KEY,
 nombre_clase VARCHAR(30) UNIQUE,
 id_tipo_clase INT(10),
 FOREIGN KEY (id_tipo_clase) REFERENCES tipo_clase(id_tipo_clase)
);