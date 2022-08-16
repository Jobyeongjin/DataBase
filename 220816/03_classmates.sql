CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates VALUES 
('홍길동', 30, '서울'), 
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');

-- classmates 안에 있는 모든 요소를 보여줘
SELECT * FROM classmates;

-- classmates 안에 있는 요소들의 rowid와 name을 보여줘
SELECT rowid, name FROM classmates;

-- classmates 안에 있는 요소들의 rowid와 name을 2개만 보여줘
SELECT rowid, name FROM classmates LIMIT 2;

-- classmates 안에 있는 요소들의 rowid와 name을 2개는 제외하고 1개만 보여줘
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT * FROM classmates WHERE address='서울';

-- classamtes 안에서 age가 30이상이면 name을 보여줘
SELECT name FROM classmates WHERE age >= 30;

-- classmates의 age를 중복없이 보여줘 
SELECT DISTINCT age FROM classmates;

-- classmates의 address를 중복없이 보여줘
SELECT DISTINCT address FROM classmates;

-- classmates의 rowid가 5인 요소를 제거할게
DELETE FROM classmates WHERE rowid=5;

-- 삽입
INSERT INTO classmates VALUES ('주세환', 40, '대전'); 
-- 조희
SELECT rowid, * FROM classmates;


-- 수정
-- classmates 안에 rowid가 5인 요소의 name과 address를 수정할게
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
-- 조회
SELECT rowid, * FROM classmates;
