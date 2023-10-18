-- creates the table unique_id on your MySQL server if it dosn't exist
-- conforming to required attrib
CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
