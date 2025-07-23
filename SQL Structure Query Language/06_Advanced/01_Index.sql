CREATE INDEX idx_name ON USERS(name);

CREATE UNIQUE INDEX idx_name ON USERS(name);

CREATE UNIQUE INDEX idx_name_surname ON USERS(name,surname);

SELECT * FROM users WHERE name = "Romero";

--- DROP INDEX idx_name ON users(name);