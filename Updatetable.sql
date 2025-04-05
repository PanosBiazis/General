USE test2;

SELECT * FROM table1 WHERE id = 1  & name = 'panos';

UPDATE table1  SET name = 'panos2' WHERE id = 1;

SELECT * FROM table1 WHERE id = 1  & name = 'panos2' ;