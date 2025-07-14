
CREATE DATABASE test_db; 

USE test_db;

CREATE TABLE persons(
    id int ,
    name varchar(100),
    age int,
    email varchar (70),
    created date
);

CREATE TABLE persons2(
    id int NOT NULL,
    name varchar(100) NOT NULL,
    age int,
    email varchar (70),
    created date
);

CREATE TABLE persons3(
    id int NOT NULL,
    name varchar(100) NOT NULL,
    age int,
    email varchar (70),
    created datetime,
    UNIQUE(id)
);

CREATE TABLE persons4(
    id int NOT NULL,
    name varchar(100) NOT NULL,
    age int,
    email varchar (70),
    created datetime,
    UNIQUE(id),
    PRIMARY KEY(id)
);