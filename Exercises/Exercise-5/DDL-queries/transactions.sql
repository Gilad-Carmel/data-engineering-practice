CREATE TABLE transactions
(
    transaction_id VARCHAR ( 255 ) PRIMARY KEY,
    transaction_date DATE  NOT NULL,
    product_id SERIAL REFERENCES products(product_id),
    product_code INT NOT NULL,
    product_description VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    account_id SERIAL REFERENCES accounts(customer_id)
);
