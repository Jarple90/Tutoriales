SELECT * FROM mi_primeradbmysql.users
INNER JOIN dni;

SELECT * FROM mi_primeradbmysql.users
INNER JOIN dni
ON mi_primeradbmysql.users.user_id = dni.user_id
ORDER BY age ASC;

SELECT * FROM mi_primeradbmysql.companies
JOIN mi_primeradbmysql.users
ON mi_primeradbmysql.users.company_id = mi_primeradbmysql.companies.company_id;


SHOW COLUMNS FROM mi_primeradbmysql.users;

SELECT *  FROM mi_primeradbmysql.users_languages
JOIN mi_primeradbmysql.users 
ON users_languages.user_id = users.user_id
JOIN mi_primeradbmysql.languages 
ON users_languages.language_id = languages.language_id;