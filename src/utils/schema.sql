CREATE DATABASE IF NOT EXISTS projeto_vaga_backend;

CREATE TABLE IF NOT EXISTS `projeto_vaga_backend`.`tb_departament` (
  `uuid` VARCHAR(100) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`uuid`)
  );

CREATE TABLE IF NOT EXISTS `projeto_vaga_backend`.`tb_employee` (
    `uuid` VARCHAR(100) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `departament_uuid` VARCHAR(100) NOT NULL,
    `dependents` INT NOT NULL,
    PRIMARY KEY (`uuid`),
    FOREIGN KEY (`departament_uuid`) REFERENCES `tb_departament`(`uuid`)
    );