# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3
```

### Column 출력 설정

```sql
sqlite3> .headers on
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
    id PRIMARY KEY,
    sido INTEGER NOT NULL,
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,
    va_left REAL NOT NULL,
    va_right REAL NOT NULL,

    blood_pressure INTEGER
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare;
```

```
count(*)
----------
1000000
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT max(age), min(age) FROM healthcare;
```

```
max(age)    min(age)
----------  ----------
18          9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT max(height), max(weight), min(height), min(weight) FROM healthcare;
```

```
max(height)  max(weight)  min(height)  min(weight)
-----------  -----------  -----------  -----------
195          135          130          30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT count(height) FROM healthcare WHERE 160<=height AND height<=170;
```

```
count(height)
-------------
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오.

```sql
SELECT * FROM healthcare WHERE is_drinking=1 ORDER BY round(waist) DESC LIMIT 5;
```

```
id          sido        gender      age         height      weight      waist       va_left     va_right    blood_pressure  smoking     is_drinking
----------  ----------  ----------  ----------  ----------  ----------  ----------  ----------  ----------  --------------  ----------  -----------
993531      48          1           9           170         130         146.0       0.6         0.8         150             3           1
87897       48          1           10          170         130         142.0       0.6         0.8         140             1           1
826643      48          1           9           180         135         141.4       1.2         0.9         136             3           1
567314      26          1           11          170         110         140.0       0.3         0.6         125             3           1
611146      36          1           12          165         120         140.0       0.4         0.8         141             3           1
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE va_left>=1.5 AND va_right>=1.5 AND is_drinking=1;
```

```
count(*)
----------
36697
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE blood_pressure<120;
```

```
count(*)
----------
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT avg(waist) FROM healthcare WHERE blood_pressure>=140;
```

```
avg(waist)
----------------
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT avg(height), avg(weight) FROM healthcare WHERE gender=1;
```

```
avg(height)       avg(weight)
----------------  ----------------
167.452735422145  69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC LIMIT 1 OFFSET 1;
```

```
id          height      weight
----------  ----------  ----------
46642       195         100
```

### 11. BMI가 30이상인 사람의 수를 출력하시오.

> BMI는 체중/(키\*키)의 계산 결과이다.
> 키는 미터 단위로 계산한다.

```sql
SELECT count(*) FROM healthcare WHERE round(weight/(height*height*0.0001),1)>=30;
```

```
count(*)
----------
53121
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키\*키)의 계산 결과이다.
> 키는 미터 단위로 계산한다.

```sql
SELECT id, round(weight/(height*height*0.0001),1) FROM healthcare WHERE smoking=3 ORDER BY round(weight/(height*height*0.0001),1) DESC LIMIT 5;
```

```
id          round(weight/(height*height*0.0001),1)
----------  --------------------------------------
231431      50.8
934714      49.9
722707      48.8
947281      47.8
948801      47.8
```

### 13. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

> 몸무게가 가장 많은 5명의 아이디, 성별, 나이, 키, 몸무게 출력

```sql
SELECT id, gender, age, height, weight FROM healthcare ORDER BY weight DESC LIMIT 5;
```

```
id          gender      age         height      weight
----------  ----------  ----------  ----------  ----------
99120       1           10          170         135
100174      1           9           180         135
119639      1           11          175         135
142639      1           9           175         135
161992      1           9           175         135
```

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

> 키가 가장 큰 5명의 아이디, 성별, 나이, 키, 몸무게 출력

```sql
SELECT id, gender, age, height, weight FROM healthcare ORDER BY height DESC LIMIT 5;
```

```
id          gender      age         height      weight
----------  ----------  ----------  ----------  ----------
8832        1           10          195         95
46642       1           9           195         100
170951      1           12          195         85
219595      1           9           195         105
229284      1           9           195         105
```

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

> 키가 가장 큰 사람 중 몸무게가 가장 많은 5명의 아이디, 성별, 나이, 키, 몸무게 출력

```sql
SELECT id, gender, age, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 5;
```

```
id          gender      age         height      weight
----------  ----------  ----------  ----------  ----------
428261      1           9           195         125
836005      1           9           195         110
219595      1           9           195         105
229284      1           9           195         105
255109      1           9           195         105
```

### 16. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

> 몸무게가 가장 많은 사람 중 키가 가장 큰 5명의 아이디, 성별, 나이, 키, 몸무게 출력

```sql
SELECT id, gender, age, height, weight FROM healthcare ORDER BY weight DESC, height DESC LIMIT 5;
```

```
id          gender      age         height      weight
----------  ----------  ----------  ----------  ----------
791483      1           9           190         135
916677      1           9           190         135
382698      1           9           185         135
709813      1           9           185         135
959061      1           9           185         135
```
