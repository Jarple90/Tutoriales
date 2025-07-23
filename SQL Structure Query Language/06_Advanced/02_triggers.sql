SELECT * FROM users;

/*CREATE TABLE `mi_primeradbmysql`.`email_history` (
`email_history` INT NOT NULL AUTO_INCREMENT,
`user_id` INT NOT NULL,
`email` VARCHAR(100) NULL,
PRIMARY KEY (`email_history`),
UNIQUE INDEX `email_history_UNIQUE` (`email_history` ASC) VISIBLE);
*/

DELIMITER $$

CREATE TRIGGER tg_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        INSERT INTO email_history(user_id, email)
        VALUES (OLD.user_id, OLD.email);
    END IF;
END$$

DELIMITER ;

UPDATE users SET email = "jarptgd@gmail.com" WHERE user_id = 3