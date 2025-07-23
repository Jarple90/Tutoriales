SELECT *,
CASE
    WHEN age >= 13 THEN 'Mayor o igual que 13'
    WHEN age <= 13 THEN 'Menor o igual que 13'
    ELSE 'Edad no especificada'
END AS edad_categoria
FROM mi_primeradbmysql.users;


