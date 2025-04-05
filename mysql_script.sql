/*Database is a collection of data,while DBMS is a management system.
DBMS helps in managing and organizing data efficiently.
Data management system also known as DBMS,is a collection of programs which enables users:
1.create a database
2.access the database
3.manipulate the data
It also provides protection and security to the database.
Databases contain files(documents) while Relational Database Management System(RDBMS) contain tables.
A table contains rows and colums and the bisecting cell is known as "field".Horizontal rows are also known as records.
Columns define the data that the rows under it must hold. 
Entity Relationship model is the structured representation of a database with the help of a diagram.
An entity can be a place,person or it may be an object with a conceptual existence-college ,job,course.
If we consider Student as an Entity,then Student ID,Name,Age,etc. are attributes describing the entity.
You first identify the entity,next scribble an ER diagram and finally convert the diagram into a table.
ER diagram is solery for your reference.it enables better planning of attributes,keys and other crusial aspects. 
Also,remember that ER is a visual representation of the database used by designers.It doesn't exist anywhere as such.
ER diagram is used to idetify
Entity-The larger block about which you wish to store data(College)
Attributes A column name and the fields that fall under it(College Name)
Relationships-The link between 2 tables
Rectangle denotes entity,rhombus denotes action(Relationships),ellliptical denotes attributes
Entity is the biggest data item !It's like the shipping container.
Attributes are the individual corrugated boxes.loaded in the shipping container!It's part of the entity.
Relationships are the links between the entities!It's part of the entity.
Tables and attributes mush have a name which has to have something to do with its superset.!It's part of the entity.
No space between the names.
We call fields or columns as attributes.We call rows as records and also call them tuples.
Tables are called "relations" sometimes.
To create a database we use the command "create database databasename;"
to  create a table we use the command "create table tablename (columnname datatype);"
A database can have multiple tables but each table can have only one database.
Keys is what helps to in maintaining an invisible relationship amongst all the required tables.
Keys helps us to identify the primary key.
keys are common attributes which are spread across all the tables.
Primary Key(PK) is a special type of key that consists of unique values.
Each row in the table has a Primary Key.
Only one attribute from a table can be declared as a primary key.
It should be unique in its value.
it cannot be left empty or null.
Foreign Key(FK) is a special type of key that consists of unique values.
it can be left empty or null.
it cannot be a primary key.
It is a reference to a primary key in another table.
One table can refer to more than one foreign keys
Unique key(UK) is a special type of key that consists of unique values.
All the values in a UK field should be unique.
None of the values in a UK field can be left empty or null.
A table can have multiple columns designated as unique key.
This key helps more in the data entry process where an erroneus entry is identified while filling in data in the table itself.
Keys:
1.Create a 'link' between two tables
2.Has unique nature
3.Ensures consistency and validity of data in a table
4.Easy data retrieval
SQL is a jungle of queries!
The DDL commands include the queries that define the data structure.
This includes CREATE,to create a table.
ALTER,to modify a table,which lets you alter the number of columns.
TRUNCATE deletes the table and frees the space.
RENAME lets you change the name of a table.
DML is a group of queries that used to store,modify,delete data.
This include some of the most used commands!
INSERT lets you add a new row
DELETE lets you delete a particular row,either conditionally or entirely.
UPDATE lets you change a particular column's value conditionally
SELECT let's you retrieve data from a database.(DQL-Data Query Language)
These commands directly impact the DML Commands.(Transaction Control Language(TCL))
This include COMMIT,SAVEPOINT,ROLLBACK.
COMMIT confirms that the changes made in the DML are permanent.
SAVEPOINT lets you save the data temporarily.
ROLLBACK lets you undo the changes made in the DML.
Data Control Language(DCL)
DCL commands help implement security measures
GRANT gives permission to users/roles on a database.
REVOKE removes permission from users/roles on a database.
CREATE USER creates a user account.
DROP USER deletes a user account.
CREATE ROLE assigns permissions to roles.
DROP ROLE removes permissions from roles.
'*' denotes NOTHING
SELECT * FROM table_name;
SELECT column_name FROM table_name;
SELECT name,phone FROM CANDIDATE;
SELECT * FROM CANDIDATE WHERE name='John';
SELECT * FROM CANDIDATE WHERE name='John' AND phone='1234567890';
SELECT * FROM CANDIDATE WHERE name='John' OR phone='1234567890';
SELECT * FROM CANDIDATE WHERE name LIKE 'J%';
A sub query is a query within a query.
SELECT StudentNo,StudentName FROM Student WHERE TotalScore=(SELECT MAX(TotalScore) FROM Student);
SQL has 3 main clauses
The GROUP BY,ORDER BY and WHERE clauses
The WHERE clause is used to apply additional filters to the data.
The GROUP BY clause is used to group the data.
The ORDER BY clause is used to sort the data.
GROUP BY groups rows with similar values together.
ORDER BY sorts rows in ascending or descending order.
Having is an optional part of SQL which can be used with GROUP BY.
A view is a virtual table that is created based on the result-set of an SQL query.
There are two types of views:
1.Simple view
2.Complex view
Simple Views display certain columns of a table.
Complex views display all the columns of a table.
certain pre-defined data is the column names that you specify when you chalk out a view.
You cannot use aggregate functions in simple views.
To create a complex view, you need to have a query.
In a complex view, you can use aggregate functions.
You can Create,Replace the attributes, and also Drop off the View.
This lets you show up the most relevant and updated data.
It also help you conceal the sensitive portions
CREATE VIEW [Mexico Doctors] AS DoctorName,PhoneNo FROM Doctor WHERE Country=Mexico;
SELECT * FROM [Mexico Doctors]; to access the data to see the names and phone numbers of the doctors from Mexico
DROP VIEW [Mexico Doctors]; to delete the view
REPLACE VIEW [Mexico Doctors] AS SELECT DoctorName,Address,EmailID FROM Doctors Country=Mexico; to replace the view
SELECT Name,Result FROM Candidate WHERE Result=Negative
SELECT * FROM InterviewCandidates WHERE TestResult=Pass ORDER BY AggregateMarks DESC
DESC(Highest-Lowest) denotes descending order and ASC(Lowest-Highest) denotes ascending order.
Constraints=limits
Rules for creating constraints:
1.Primary Key Constraint: It is used to uniquely identify each record in a database
2.Foreign Key Constraint: It is used to link two tables
3.Unique Constraint: It is used to ensure that all values in a column are unique
4.Check Constraint: It is used to limit the value of a column
5.Default Constraint: It is used to set a default value for a column
6.Not Null Constraint: It is used to ensure that a column cannot have a null value
7.Index Constraints: It is used to improve the performance of a query by creating indexes on specific columns.
Syntax for Creating Primary Key Constraints: 
ALTER TABLE Table_name ADD CONSTRAINT constraint_name PRIMARY KEY(column_name);
Address varchar (500) NULL EmailID nvarchar (100) NOT NULL
NOT NULL makes the required data to be filled else an error will be thrown.
EmployeeID varchar (100) UNIQUE
Country char (30) DEFAULT 'US'
CHECK (Age >= 18)
DEFAULT specifies a default value for a column.
Index Constraints are used to improve the performance of a query by creating indexes on specific columns. Indexes make searching faster by storing key information in the index.
If we don’t provide any value while inserting data into a table, the default value is NULL.
SQL Server does not support CHECK Constraints.
Operators are wordsor symbols that impact the result in a certain manner.They approach the data in a certain manner and filter the results accordingly.
There are several types of operators,depending upon how they impact the results.
Logical Operators derive a logical output depending on which one you choose.
Arithmetic Operators perform mathematical operations on numbers.
Comparison Operators compare two values and return a boolean value
Logical Operators: AND,OR,NOT (all of them used with WHERE)
Bitwise Operators: & , | , ^ , ~ , << , >>
String Operators: LIKE, NOT LIKE, IN, NOT IN, BETWEEN, NOT BETWEEN
Arithmetic Operators: +,-,*,/,%,//
Comparison Operators: =,>,<,>=,<=,!=,<>
LIKE lets you filter the records that fulfil a certain parameter
NOT LIKE lets you filter the records that fulfill a certain parameter
IN allows us to specify multiple conditions at once using comma separated list inside brackets.
IN lets you filter the records that fulfill a certain parameter
BETWEEN lets you filter the records that fulfill a certain parameter between two values
The % symbol represents zero or more characters
The _ symbol represents exactly one character
SELECT * FROM Employess WHERE EmployeeName IN (Apple,Mi,IBM);
NOT IN lets you filter the records that fulfill a certain parameter but do not match the specified criteria.
Triggers are used to automate certain actions in a database. They can be created by executing the following SQL statements:
SELECT * FROM Employees WHERE Department NOT IN (IT,HR);
DDL Triggers are defined with the CREATE,ALTER,DROP statements
DML Triggers are the ones that are defined with the INSERT,UPDATE,DELETE statements
If you have 2 or more tables tat their data is related  just type JOIN to retrieve the data.
JOIN keyword can be used to combine rows from two or more tables.
It returns records that have matching values in both tables.
INNER JOIN shows only matching Data from multiple tables.
LEFT JOIN shows all the records from the left table. Even if there is no match in right table it will show.
RIGHT JOIN shows all the records from the right table. Even if there is no match in left table it will show.
FULL OUTER JOIN shows all the records from both tables. If there is a match then it will display those records.
Equi join makes use of'=' sign to derive data having equal value.
Non-Equi join does just the opposite and the sign '!=' is used in the query.
CROSS JOIN combines every row from one table with every row from another table.
A self-join occurs when a table is joined with itself. It is also known as an inner loop join.
Natural join is the most common type of join. It matches columns by name rather than position.
Using NATURAL JOIN clause helps to find the common columns between two tables.
To avoid Cartesian product we can use ON clause.
An index is a database object that improves the performance of a query.
UNION is used to combine the results of 2 or more queries.
NULL means unknown or uninitialized value.
UNION ALL is used to combine the results of 2 or more queries. All duplicates are retained.
INTERSECT is used to get the common records from 2 or more queries.
EXCEPT is used to get the unique records from 2 or more queries.
DISTINCT is used to eliminate duplicate rows.*/
/*Practice time*/
/*create database my_first_db;//to create a database*/
/*show databases;//to show the databases*/
/*SELECT 'my_first_db';//to see and select the database*/