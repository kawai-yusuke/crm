--customersテーブルが既存の場合に削除する

DROP TABLE IF EXISTS customers;

--カスタマーテーブルを作る
CREATE TABLE customers(
    name TEXT,
    age INTEGER
);

--予めデータを入れておく
INSERT INTO customers
    (name, age)
VALUES
    ("Bob", 15),
    ("Tom", 57),
    ("Ken", 73)
;