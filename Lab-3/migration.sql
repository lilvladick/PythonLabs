CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    price FLOAT,
    category VARCHAR(255),
    images TEXT, --IMAGES нужны для расширения функционала в будущем
    seller_contacts VARCHAR(255)
);