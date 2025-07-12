SELECT MAX(age) FROM mi_primeradbmysql.users GROUP BY age;

SELECT COUNT(age) FROM mi_primeradbmysql.users GROUP BY age;

SELECT COUNT(age), age FROM mi_primeradbmysql.users GROUP BY age ORDER BY age ASC;

SELECT COUNT(age), age FROM mi_primeradbmysql.users WHERE age > 13 GROUP BY age ORDER BY age ASC;