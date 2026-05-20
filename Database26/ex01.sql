SELECT ABS(-78), ABS(+78) FROM Dual;
SELECT ROUND(4.875,1) FROM Dual;
SELECT custid "고객번호" , ROUND(SUM(saleprice)/COUNT(*),-2) "평균금액" FROM Orders GROUP BY custid;
SELECT bookid, REPLACE(bookname, '야구','농구')bookname, publisher,price FROM Book;
SELECT bookname "제목", LENGTH(bookname) "글자수", LENGTH(bookname) "바이트수" FROM book WHERE publisher;
SELECT SIBSIR(name, 1,1)"성", count(*) "인원" FROM Customer GRUP BY SIBSIR(name,1,1);
SELECT TO_DATE('2025-07-01','yyyy-mm-dd')+5 BEFORE,TO_DATE('2025-07-01','yyyy-mm-dd')-5 AFTER FROM Dual
SELECT orderid "주문번호", orderdate "주문일", orderdate+10 "확정일" FROM Orders