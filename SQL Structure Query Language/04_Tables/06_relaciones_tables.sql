USE mi_primeradbmysql;

--- Relación 1-1
CREATE TABLE dni (
	dni_id int AUTO_INCREMENT PRIMARY KEY,
    dni_number int NOT NULL,
    user_id int, 
    UNIQUE(dni_id),
    FOREIGN KEY(user_id) REFERENCES mi_primeradbmysql.users(user_id)
    );
    
--- Relación 1-n
CREATE TABLE companies(
	company_id int AUTO_INCREMENT PRIMARY KEY,
    name varchar(100) NOT NULL
    );
    
ALTER TABLE mi_primeradbmysql.users
ADD company_id varchar(150);

ALTER TABLE mi_primeradbmysql.users  
ADD CONSTRAINT fk_companies
FOREIGN KEY(company_id) 
REFERENCES companies(company_id)

SHOW CREATE TABLE companies;

--- Relación n-n 

CREATE TABLE users_languages(
	users_language_id int AUTO_INCREMENT PRIMARY KEY,
	user_id int,
    language_id int,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (language_id) REFERENCES languages(language_id),
    UNIQUE(user_id, language_id)
    );
--- Relación n-m, es el ejemplo de los jefazos