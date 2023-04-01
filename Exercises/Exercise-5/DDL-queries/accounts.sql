CREATE TABLE accounts
(
    customer_id serial PRIMARY KEY,
    first_name VARCHAR ( 50 ) NOT NULL,
    last_name VARCHAR ( 50 ) NOT NULL,
    address_1 VARCHAR ( 255 ) NOT NULL,
    address_2 VARCHAR ( 255 ),
    city VARCHAR ( 50 ) NOT NULL,
    state VARCHAR ( 50 ) NOT NULL,
    zip_code INT NOT NULL,
    join_date TIMESTAMP
);
