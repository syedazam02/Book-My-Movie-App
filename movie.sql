--Creation of Database
CREATE DATABASE movie;

--Selecting movie Database
USE movie;

--Creation of Table
CREATE TABLE customer(cid INT AUTO_INCREMENT,Name VARCHAR(30),Gender VARCHAR(10),Age INT,phone_num VARCHAR(12),seat_no INT UNIQUE,ticket_price INT,PRIMARY KEY(cid));

--To see the Schema of Table
DESC customer;

--To retrieve records from table
SELECT * FROM customer;

--To retrieve a record w.r.t seat number
--SELECT * FROM customer WHERE seat_no = 11; --search for ur seat number

--To insert a record in customer table
--INSERT INTO customer(Name,Gender,Age,phone_num,seat_no,ticket_price) VALUES (16,'SYED','MALE',22,'228373648',11,10);

--To retrieve a record w.r.t customer name
--SELECT * FROM customer WHERE Name = 'SYED';

--To find Current income earned by movie theatre
--select sum(ticket_price) from customer where seat_no <= %s

