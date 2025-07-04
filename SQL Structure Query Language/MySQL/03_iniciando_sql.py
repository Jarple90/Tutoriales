
### Crear la tabla usuarios de nuestro ejemplo "mi_primeradbmysql" 

# CREATE TABLE `mi_primeradbmysql`.`users` (
#   `user_id` INT NOT NULL AUTO_INCREMENT,
#    `name` VARCHAR(50) NOT NULL,
#    `surname` VARCHAR(100) NULL,
#    `age` INT NULL,
#    `init_date` DATE NULL,
#    `email` VARCHAR(100) NULL,
#    PRIMARY KEY (`user_id`));

### Introducción de datos, se puede hacer manualmente, es más fácil desde el icono de formulario o la creación del código:

# INSERT INTO `mi_primeradbmysql`.`users` (
#  `user_id`, `name`, `surname`, `age`, `init_date`, `email`)
# VALUES ('1', 'José Antonio', 'Romero Pérez', '2', '2023-07-04', 'jarptgd@gmail.com');

### Realizamos pruebas para ver el autoincremental y valores null ###

# INSERT INTO `mi_primeradbmysql`.`users` (
# `user_id`, `name`, `surname`, `age`, `init_date`, `email`) 
# VALUES ('2', 'Snow', 'Ice', '14', '2004-05-09', 'jarple90@gmail.com');
# INSERT INTO `mi_primeradbmysql`.`users` (
# `name`, `surname`, `age`, `init_date`) 
# VALUES ('Snow', 'D Ice', '1', '2025-07-04');

