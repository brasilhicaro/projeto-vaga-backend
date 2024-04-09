CREATE DATABASE IF NOT EXISTS projeto_vaga_backend;

CREATE TABLE IF NOT EXISTS `projeto_vaga_backend`.`tb_departament` (
  `id` VARCHAR(100) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`)
  );

CREATE TABLE IF NOT EXISTS `projeto_vaga_backend`.`tb_employeer` (
    `id` VARCHAR(100) NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `departament_id` VARCHAR(100) NOT NULL,
    `dependents` INT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`departament_id`) REFERENCES `tb_departament`(`id`)
    );
    