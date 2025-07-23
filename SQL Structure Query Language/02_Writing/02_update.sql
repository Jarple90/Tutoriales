UPDATE mi_primeradbmysql.users SET age = '21' WHERE user_id = 4; ---- Super importante siempre que actualices algo ten cuidado de poner un where para no modificarlo todo

UPDATE mi_primeradbmysql.users SET age = 22, init_date = '2023-10-01' WHERE user_id = 4;  ---- Si el age es int, no hace falta poner las comillas