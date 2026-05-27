CREATE INDEX ix_Book ON Book (bookname);
CREATE INDEX ix_Book2 ON Book (publisher,price);

-- 프로시저

-- 1. bookid를 입력받아 해당 도서의 bookname, publisher, price를 출력하는 프로시저를 작성하시오.

CREATE OR REPLACE PROCEDURE problem1(
    mybookid IN NUMBER
)
IS
    mybookname VARCHAR2(40);
    mypublisher VARCHAR2(40);
    myprice NUMBER;
BEGIN
    SELECT bookname, publisher, price INTO mybookname, mypublisher, myprice FROM Book WHERE bookid = mybookid;
    DBMS_OUTPUT.PUT_LINE(mybookname || mypublisher || myprice);
END;
/

-- 2. 새로운 고객 정보(custid, name, address, phone)를 입력받아 Customer 테이블에 삽입하는 프로시저를 작성하시오.

CREATE OR REPLACE PROCEDURE problem2(
    mycustid IN NUMBER,
    myname IN VARCHAR2,
    myaddress IN VARCHAR2,
    myphone IN VARCHAR2
)
IS
    
BEGIN
    INSERT INTO Customer(custid, name, address, phone)
    VALUES(mycustid, myname, myaddress, myphone);
END;
/

-- 3. bookid와 새로운 price를 입력받아 해당 도서의 가격을 수정하는 프로시저를 작성하시오.

CREATE OR REPLACE PROCEDURE problem3(
    mybookid IN NUMBER,
    myprice IN NUMBER
)
IS   
BEGIN
    UPDATE Book SET price = myprice;
    UPDATE Book SET bookid = mybookid;
END;
/

-- 4. custid를 입력받아 해당 고객의 주문 내역을 Orders 테이블에서 모두 삭제한 후, Customer 테이블에서도 해당 고객을 삭제하는 프로시저를 작성하시오.

CREATE OR REPLACE PROCEDURE problem4(
    mycustid IN NUMBER,
)
IS   
BEGIN
    DELETE FROM 
END;
/