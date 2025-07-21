CREATE TABLE persons8(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    age int,
    email varchar (70),
    created datetime DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(id),
    PRIMARY KEY(id),
    CHECK(age>=18)
);

ALTER PERSONS8
ADD surname varchar (150);