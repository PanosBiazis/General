use test;

-- ALTER TABLE your_table_name ADD COLUMN new_column_name data_type;

ALTER TABLE test ADD COLUMN email varchar(255);

-- ALTER TABLE your_table_name MODIFY COLUMN column_name data_type;

ALTER TABLE test MODIFY COLUMN email varchar(100);

-- ALTER TABLE your_table_name DROP COLUMN column_name;

ALTER TABLE test DROP COLUMN email;

-- ALTER TABLE your_table_name ENGINE = new_engine;

ALTER TABLE test ENGINE = InnoDB;

-- ALTER TABLE your_table_name RENAME TO new_table_name;

ALTER TABLE test RENAME TO test2

SELECT * from test;


ALTER TABLE table1 MODIFY COLUMN id INT(50);

