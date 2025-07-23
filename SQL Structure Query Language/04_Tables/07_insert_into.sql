SELECT * FROM mi_primeradbmysql.dni;

INSERT INTO dni (dni_number, user_id) VALUES (111111, 1);

INSERT INTO dni (dni_number, user_id) VALUES (222222, 2);

INSERT INTO dni (dni_number, user_id) VALUES (333333, 3);

INSERT INTO dni (dni_number) VALUES (444444);

SELECT * FROM mi_primeradbmysql.users;

UPDATE mi_primeradbmysql.users SET company_id = 1 WHERE user_id = 1;
UPDATE mi_primeradbmysql.users SET company_id = 2 WHERE user_id = 2;
UPDATE mi_primeradbmysql.users SET company_id = 3 WHERE user_id = 3;
UPDATE mi_primeradbmysql.users SET company_id = 4 WHERE user_id = 7;

SELECT * FROM mi_primeradbmysql.languages;

INSERT INTO languages (name) VALUES ('Python');
INSERT INTO languages (name) VALUES ('Kotlin');
INSERT INTO languages (name) VALUES ('JavaScript');
INSERT INTO languages (name) VALUES ('C#');
INSERT INTO languages (name) VALUES ('COBOL');

SELECT * FROM mi_primeradbmysql.users_languages;

INSERT INTO mi_primeradbmysql.users_languages (user_id, language_id) VALUES (1,1);
INSERT INTO mi_primeradbmysql.users_languages (user_id, language_id) VALUES (1,2);
INSERT INTO mi_primeradbmysql.users_languages (user_id, language_id) VALUES (1,5);
INSERT INTO mi_primeradbmysql.users_languages (user_id, language_id) VALUES (2,3);
INSERT INTO mi_primeradbmysql.users_languages (user_id, language_id) VALUES (2,5);

--- Importante tener el campo not null en users_languages