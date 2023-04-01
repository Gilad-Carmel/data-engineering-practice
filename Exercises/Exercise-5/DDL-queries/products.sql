CREATE TABLE products
(
    product_id serial PRIMARY KEY,
    product_code INT UNIQUE NOT NULL,
    product_description VARCHAR (255) UNIQUE NOT NULL
);

