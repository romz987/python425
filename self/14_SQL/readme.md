# SQL и База Данных  

## Контент  

[Основные операции](#Основные-операции)  
[Сложные запросы](#Сложные-запросы) 
[Темы ищут место](#Темы-ищут-место)

----  
## Основные операции  
**DML (DATA MANIPULATION LANGUAGE)**  

C - create:    

    INSERT INTO <table_name> () VALUES ();  

R - read:    

    SELECT * FROM <table_name>;  
    SELECT DISTINCT * FROM <table_name>;  
    JOIN  

U - update:    

    UPDATE <table_name> SET foo = bar WHERE <condition>;  

D - delete:    

    DELETE FROM <table_name> WHERE <condition>;  

**DDL (DATA DEFENITION LANGUAGE)**    

    CREATE TABLE <table_name> ();   
    
    DROP TABLE <table_name>;    

    ALTER TABLE <table_name> [ADD <column_name> / DROP COLUMN <column_name] <data_type> <constraints>;  

**DCL (DATA CONTROL LANGUAGE)**    

**TCL (TRANSACTION CONTROL LANGUAGE)**    

----
## Сложные запросы 
JOIN
LEFT JOIN
Прочие операторы о которых стоит знать
Запросы и подзапросы

----
## Темы ищут место
ACID - атомарность, согласованность, изоляция, долговечность
