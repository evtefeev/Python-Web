-- Створення таблиці товарів
CREATE TABLE goods (
    id SERIAL PRIMARY KEY,
    product VARCHAR(255),
    value INT,
    price DECIMAL(10, 2)
);



INSERT INTO goods_nikita (product, value, price)
SELECT
    CASE
        WHEN id % 20 = 0 THEN 'banana'
        WHEN id % 20 = 1 THEN 'milk'
        WHEN id % 20 = 2 THEN 'potato'
        WHEN id % 20 = 3 THEN 'bread'
        WHEN id % 20 = 4 THEN 'meat'
        WHEN id % 20 = 5 THEN 'fish'
        WHEN id % 20 = 6 THEN 'egg'
        WHEN id % 20 = 7 THEN 'garlic'
        WHEN id % 20 = 8 THEN 'ham'
        WHEN id % 20 = 9 THEN 'sausage'
        WHEN id % 20 = 10 THEN 'pizza'
        WHEN id % 20 = 11 THEN 'porridge'
        WHEN id % 20 = 12 THEN 'chicken'
        WHEN id % 20 = 13 THEN 'pork'
        WHEN id % 20 = 14 THEN 'cheese'
        WHEN id % 20 = 15 THEN 'bean'
        WHEN id % 20 = 16 THEN 'salt'
        WHEN id % 20 = 17 THEN 'fruit'
        WHEN id % 20 = 18 THEN 'tea'
        WHEN id % 20 = 19 THEN 'coffee'
    END AS product,
    FLOOR(RANDOM() * 100) + 1 AS value,  -- Генерує кількість товару
    FLOOR(RANDOM() * 50 + 10) AS price   -- Генерує випадкову ціну від 10 до 60
FROM generate_series(1, 100) AS id;