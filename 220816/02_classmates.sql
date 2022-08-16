-- classmates 라는 테이블을 생성한다. 
-- 이름과 주소는 문자열로 입력이 되고, 나이는 숫자로 입력된다.
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);

-- CREATE
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('김철수', 40, '서울');

-- rowidsms SQLite에서 자동으로 제공하는 PK
SELECT rowid, * FROM classmates;

DROP TABLE classmates;