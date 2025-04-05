USE test2;

-- Select all data from table1
SELECT * FROM table1;

-- Create a view named 'table_view' that includes 'idNumber' and 'Name' from 'table1'
CREATE VIEW table_view AS
SELECT id, Name
FROM table1;

-- Select all data from the view 'table_view'
SELECT * FROM table_view;