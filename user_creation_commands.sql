
--in terminal
sqlplus sys/SysPassword@localhost:1521/mypdb as sysdba

ALTER SESSION SET CONTAINER = mypdb;


--replace myuser with username
--replace mypassword with password
CREATE USER charanjith IDENTIFIED BY charanjith
DEFAULT TABLESPACE system
TEMPORARY TABLESPACE temp;


--granting privilleges
GRANT CREATE SESSION TO charanjith;
GRANT CONNECT TO charanjith;
GRANT RESOURCE TO charanjith;

--replace myuser with username
GRANT CREATE TABLE, CREATE SEQUENCE, CREATE VIEW TO charanjith;
GRANT CREATE PROCEDURE, CREATE TRIGGER TO charanjith;


--replace myuser with username
--replace mypassword with password
sqlplus myuser/mypassword@localhost:1521/mypdb

ALTER SESSION SET CONTAINER = mypdb;

CONN charanjith/charanjith@localhost:1521/mypdb


--create tables

--code to connect

import cx_Oracle

username = "myuser"
password = "mypassword"
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="mypdb")

connection = cx_Oracle.connect(username, password, dsn)
cursor = connection.cursor()


