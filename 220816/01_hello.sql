-- SQLite๐

-- classmates๋ผ๋ ์ด๋ฆ์ ํ์ด๋ธ ์์ฑ
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
);


-- ํ์ด๋ธ ๋ชฉ๋ก ์กฐํ
.tables


-- ํน์  ํ์ด๋ธ ์คํค๋ง ์กฐํ
.schema classmates


-- ๊ฐ ์ถ๊ฐ
INSERT INTO classmates VALUES (1, '์กฐ์ธํธ');


-- ํ์ด๋ธ ์กฐํ
SELECT * FROM classmates;


-- ๊ฐ ์ถ๊ฐ
INSERT INTO classmates VALUES (2, '์ด๋ํฌ');


-- ํ์ด๋ธ ์ญ์ 
DROP TABLE classmates;