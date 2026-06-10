SET TRANSACTION NAME 'T1';
SELECT * FROM Book WHERE bookid=1;
UPDATE Book
SET price=7100
WHERE bookid=1;
SELECT * FROM Book WHERE bookid=1;
COMMIT;

SET TRANSACTION NAME 'T2';
SELECT * FROM Book WHERE bookid=1;
UPDATE Book
SET price=price+100
WHERE bookid=1;
SELECT * FROM Book WHERE bookid=1;
COMMIT;


ALTER TABLE Book ADD (stock NUMBER DEFAULT 1);
UPDATE Book SET stock = 1 WHERE bookid = 1;
COMMIT;

SELECT stock
FROM Book
WHERE bookid = 1
FOR UPDATE;

UPDATE Book
SET stock = stock - 1
WHERE bookid = 1;

INSERT INTO Orders (orderid, custid, bookid, saleprice, orderdate)
VALUES (11, 1, 1, 15000, SYSDATE);

COMMIT;

SELECT stock FROM Book WHERE bookid = 1;

SELECT stock
FROM Book
WHERE bookid = 1
FOR UPDATE; 