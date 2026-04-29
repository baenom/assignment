-- 01 마당서점 고객이 알고 싶어 하는 내용

-- (1) 도서번호가 1인 도서의 이름
SELECT bookname FROM Book WHERE bookid = 1;

-- (2) 가격이 20,000원 이상인 도서의 이름
SELECT bookname FROM Book WHERE price >= 20000;

-- (3) '박지성'의 총구매액
SELECT SUM(saleprice) AS Total_Purchase FROM Orders WHERE custid = (SELECT custid FROM Customer WHERE name = '박지성');

-- (4) '박지성'이 구매한 도서의 수
SELECT COUNT(*) AS Purchase_Count FROM Orders WHERE custid = (SELECT custid FROM Customer WHERE name = '박지성');


-- 02 마당서점 운영자와 경영자가 알고 싶어 하는 내용

-- (1) 마당서점 도서의 총수
SELECT COUNT(*) AS Total_Books FROM Book;

-- (2) 마당서점에 도서를 출고하는 출판사의 총수
SELECT COUNT(DISTINCT publisher) AS Publisher_Count FROM Book;

-- (3) 모든 고객의 이름, 주소
SELECT name, address FROM Customer;

-- (4) 2025년 7월 4일부터 7월 7일 사이에 주문받은 도서의 주문번호
SELECT orderid FROM Orders WHERE orderdate BETWEEN '2025-07-04' AND '2025-07-07';

-- (5) 2025년 7월 4일부터 7월 7일 사이에 주문받은 도서를 제외한 도서의 주문번호
SELECT orderid FROM Orders WHERE orderdate NOT BETWEEN '2025-07-04' AND '2025-07-07';

-- (6) 성이 '김' 씨인 고객의 이름과 주소
SELECT name, address FROM Customer WHERE name LIKE '김%';

-- (7) 성이 '김' 씨이고 이름이 '아'로 끝나는 고객의 이름과 주소
SELECT name, address FROM Customer WHERE name LIKE '김%아';