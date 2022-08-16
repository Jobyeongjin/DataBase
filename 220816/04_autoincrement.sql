CREATE TABLE members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

INSERT INTO members VALUES 
(1, '홍길동'), 
(2, '김철수'),
(3, '이호영'),
(4, '박민희'),
(5, '최혜영');

-- rowid가 5인 요소를 삭제 후 새로 추가한다. 여기서 짚고 넘어가는 부분💡
-- 새로 추가한 요소의 id값이 5가 아닌 6이 된다?
-- autoincrement를 사용하면 유일한 값을 가지게 되고, 삭제한 id값은 재사용이 불가하다.
-- 만약 데이터가 5에서 끝이 아니라 수많은 데이터가 줄지어 있는 상황에서 중간의 데이터를 삭제했다고 가정해보면 쉽게 이해할 수 있다. 
DELETE FROM members WHERE rowid=5;
INSERT INTO members (name) VALUES ('주세환'); 
SELECT * FROM members;

-- id  name
-- --  ----
-- 1   홍길동
-- 2   김철수
-- 3   이호영
-- 4   박민희
-- 6   주세환  