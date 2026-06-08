CREATE INDEX ix_Book ON Book (bookname);
CREATE INDEX ix_Book2 ON Book (publisher,price);

-- 프로시저

-- 1. bookid를 입력받아 해당 도서의 bookname, publisher, price를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem1(
    p_bookid IN NUMBER
)
IS
    v_bookname VARCHAR2(50);
    v_publisher VARCHAR2(50);
    v_price NUMBER;
BEGIN
    SELECT bookname, publisher, price 
    INTO v_bookname, v_publisher, v_price 
    FROM Book 
    WHERE bookid = p_bookid;
    
    DBMS_OUTPUT.PUT_LINE(v_bookname || ' ' || v_publisher || ' ' || v_price);
END;
/

-- 2. 새로운 고객 정보(custid, name, address, phone)를 입력받아 Customer 테이블에 삽입하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem2(
    p_custid IN NUMBER,
    p_name IN VARCHAR2,
    p_address IN VARCHAR2,
    p_phone IN VARCHAR2
)
IS
BEGIN
    INSERT INTO Customer(custid, name, address, phone)
    VALUES(p_custid, p_name, p_address, p_phone);
    COMMIT;
END;
/

-- 3. bookid와 새로운 price를 입력받아 해당 도서의 가격을 수정하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem3(
    p_bookid IN NUMBER,
    p_price IN NUMBER
)
IS   
BEGIN
    UPDATE Book 
    SET price = p_price
    WHERE bookid = p_bookid;
    COMMIT;
END;
/

-- 4. custid를 입력받아 해당 고객의 주문 내역을 Orders 테이블에서 모두 삭제한 후, Customer 테이블에서도 해당 고객을 삭제하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem4(
    p_custid IN NUMBER
)
IS   
BEGIN
    DELETE FROM Orders 
    WHERE custid = p_custid;
    
    DELETE FROM Customer 
    WHERE custid = p_custid;
    COMMIT;
END;
/

-- 1. bookid를 입력받아 해당 도서의 bookname, publisher, price를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem1(
    p_bookid IN NUMBER
)
IS
    v_bookname VARCHAR2(50);
    v_publisher VARCHAR2(50);
    v_price NUMBER;
BEGIN
    SELECT bookname, publisher, price 
    INTO v_bookname, v_publisher, v_price 
    FROM Book 
    WHERE bookid = p_bookid;
    
    DBMS_OUTPUT.PUT_LINE(v_bookname || ' ' || v_publisher || ' ' || v_price);
END;
/

-- 2. 새로운 고객 정보(custid, name, address, phone)를 입력받아 Customer 테이블에 삽입하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem2(
    p_custid IN NUMBER,
    p_name IN VARCHAR2,
    p_address IN VARCHAR2,
    p_phone IN VARCHAR2
)
IS
BEGIN
    INSERT INTO Customer(custid, name, address, phone)
    VALUES(p_custid, p_name, p_address, p_phone);
    COMMIT;
END;
/

-- 3. bookid와 새로운 price를 입력받아 해당 도서의 가격을 수정하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem3(
    p_bookid IN NUMBER,
    p_price IN NUMBER
)
IS   
BEGIN
    UPDATE Book 
    SET price = p_price
    WHERE bookid = p_bookid;
    COMMIT;
END;
/

-- 4. custid를 입력받아 해당 고객의 주문 내역을 Orders 테이블에서 모두 삭제한 후, Customer 테이블에서도 해당 고객을 삭제하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem4(
    p_custid IN NUMBER
)
IS   
BEGIN
    DELETE FROM Orders 
    WHERE custid = p_custid;
    
    DELETE FROM Customer 
    WHERE custid = p_custid;
    COMMIT;
END;
/

-- 5. orderid를 입력받아 해당 주문의 고객 이름, 도서명, 주문금액, 주문날짜를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem5(
    p_orderid IN NUMBER
)
IS
    v_name VARCHAR2(50);
    v_bookname VARCHAR2(50);
    v_saleprice NUMBER;
    v_orderdate DATE;
BEGIN
    SELECT name, bookname, saleprice, orderdate
    INTO v_name, v_bookname, v_saleprice, v_orderdate
    FROM Orders 
    JOIN Customer ON Orders.custid = Customer.custid
    JOIN Book ON Orders.bookid = Book.bookid
    WHERE Orders.orderid = p_orderid;

    DBMS_OUTPUT.PUT_LINE(v_name || ' ' || v_bookname || ' ' || v_saleprice || ' ' || v_orderdate);
END;
/

-- 6. 출판사 이름을 입력받아 해당 출판사의 도서 목록(bookid, bookname, price)을 모두 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem6(
    p_publisher IN VARCHAR2
)
IS
    CURSOR c_books IS
        SELECT bookid, bookname, price
        FROM Book
        WHERE publisher = p_publisher;
BEGIN
    FOR r_book IN c_books LOOP
        DBMS_OUTPUT.PUT_LINE(r_book.bookid || ' ' || r_book.bookname || ' ' || r_book.price);
    END LOOP;
END;
/

-- 7. custid를 입력받아 해당 고객의 전체 주문 내역(도서명, 주문금액, 주문날짜)을 주문날짜 오름차순으로 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem7(
    p_custid IN NUMBER
)
IS
    CURSOR c_orders IS
        SELECT bookname, saleprice, orderdate
        FROM Orders
        JOIN Book ON Orders.bookid = Book.bookid
        WHERE Orders.custid = p_custid
        ORDER BY orderdate ASC;
BEGIN
    FOR r_order IN c_orders LOOP
        DBMS_OUTPUT.PUT_LINE(r_order.bookname || ' ' || r_order.saleprice || ' ' || r_order.orderdate);
    END LOOP;
END;
/

-- 8. 시작 날짜와 종료 날짜를 입력받아 해당 기간 내 주문된 모든 주문 정보(고객명, 도서명, 주문금액, 주문날짜)를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem8(
    p_start_date IN DATE,
    p_end_date IN DATE
)
IS
    CURSOR c_period_orders IS
        SELECT name, bookname, saleprice, orderdate
        FROM Orders
        JOIN Customer ON Orders.custid = Customer.custid
        JOIN Book ON Orders.bookid = Book.bookid
        WHERE orderdate BETWEEN p_start_date AND p_end_date;
BEGIN
    FOR r_order IN c_period_orders LOOP
        DBMS_OUTPUT.PUT_LINE(r_order.name || ' ' || r_order.bookname || ' ' || r_order.saleprice || ' ' || r_order.orderdate);
    END LOOP;
END;
/

-- 9. 도서 이름을 입력받아 해당 도서를 주문한 고객의 이름과 주문금액을 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem9(
    p_bookname IN VARCHAR2
)
IS
    CURSOR c_book_customers IS
        SELECT name, saleprice
        FROM Orders
        JOIN Customer ON Orders.custid = Customer.custid
        JOIN Book ON Orders.bookid = Book.bookid
        WHERE bookname = p_bookname;
BEGIN
    FOR r_cust IN c_book_customers LOOP
        DBMS_OUTPUT.PUT_LINE(r_cust.name || ' ' || r_cust.saleprice);
    END LOOP;
END;
/

-- 10. 특정 주문금액 이상의 주문을 한 고객의 custid, name, 주문 건수를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem10(
    p_min_price IN NUMBER
)
IS
    CURSOR c_high_cust IS
        SELECT Orders.custid, name, COUNT(orderid) AS order_count
        FROM Orders
        JOIN Customer ON Orders.custid = Customer.custid
        WHERE saleprice >= p_min_price
        GROUP BY Orders.custid, name;
BEGIN
    FOR r_cust IN c_high_cust LOOP
        DBMS_OUTPUT.PUT_LINE(r_cust.custid || ' ' || r_cust.name || ' ' || r_cust.order_count);
    END LOOP;
END;
/

-- 11. custid를 입력받아 해당 고객의 총 주문금액 합계를 OUT 매개변수로 반환하고 화면에도 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem11(
    p_custid IN NUMBER,
    p_total_price OUT NUMBER
)
IS
BEGIN
    SELECT SUM(saleprice)
    INTO p_total_price
    FROM Orders
    WHERE custid = p_custid;

    IF p_total_price IS NULL THEN
        p_total_price := 0;
    END IF;

    DBMS_OUTPUT.PUT_LINE(p_total_price);
END;
/

-- 12. 출판사 이름을 입력받아 해당 출판사 도서들의 평균 주문금액, 최고 주문금액, 최저 주문금액을 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem12(
    p_publisher IN VARCHAR2
)
IS
    v_avg_price NUMBER;
    v_max_price NUMBER;
    v_min_price NUMBER;
BEGIN
    SELECT AVG(saleprice), MAX(saleprice), MIN(saleprice)
    INTO v_avg_price, v_max_price, v_min_price
    FROM Orders
    JOIN Book ON Orders.bookid = Book.bookid
    WHERE publisher = p_publisher;

    DBMS_OUTPUT.PUT_LINE(ROUND(v_avg_price, 2) || ' ' || v_max_price || ' ' || v_min_price);
END;
/

-- 13. 전체 도서 중 주문 횟수가 가장 많은 도서의 이름과 주문 횟수를 OUT 매개변수로 반환하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem13(
    p_bookname OUT VARCHAR2,
    p_order_count OUT NUMBER
)
IS
BEGIN
    SELECT bookname, order_count
    INTO p_bookname, p_order_count
    FROM (
        SELECT bookname, COUNT(orderid) AS order_count
        FROM Orders
        JOIN Book ON Orders.bookid = Book.bookid
        GROUP BY bookname
        ORDER BY COUNT(orderid) DESC
    )
    WHERE ROWNUM = 1;
END;
/

-- 14. 주문 삽입 시 입력한 saleprice가 해당 도서의 price보다 크면 오류 메시지를 출력하고 삽입을 중단하며, 정상이면 Orders 테이블에 삽입하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem14(
    p_orderid IN NUMBER,
    p_custid IN NUMBER,
    p_bookid IN NUMBER,
    p_saleprice IN NUMBER,
    p_orderdate IN DATE
)
IS
    v_original_price NUMBER;
BEGIN
    SELECT price INTO v_original_price FROM Book WHERE bookid = p_bookid;

    IF p_saleprice > v_original_price THEN
        DBMS_OUTPUT.PUT_LINE('오류');
    ELSE
        INSERT INTO Orders (orderid, custid, bookid, saleprice, orderdate)
        VALUES (p_orderid, p_custid, p_bookid, p_saleprice, p_orderdate);
        COMMIT;
    END IF;
END;
/

-- 15. custid를 입력받아 해당 고객의 총 주문금액이 30,000원 이상이면 'VIP 고객', 10,000원 이상이면 '일반 고객', 그 미만이면 '신규 고객'으로 등급을 분류하여 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE problem15(
    p_custid IN NUMBER
)
IS
    v_total_price NUMBER;
    v_grade VARCHAR2(50);
BEGIN
    SELECT SUM(saleprice) INTO v_total_price FROM Orders WHERE custid = p_custid;

    IF v_total_price IS NULL THEN
        v_total_price := 0;
    END IF;

    IF v_total_price >= 30000 THEN
        v_grade := 'VIP 고객';
    ELSIF v_total_price >= 10000 THEN
        v_grade := '일반 고객';
    ELSE
        v_grade := '신규 고객';
    END IF;

    DBMS_OUTPUT.PUT_LINE(v_grade);
END;
/


-- 1. 특정 극장번호를 입력받아 해당 극장의 이름과 위치를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem1(
    p_theater_no IN NUMBER
)
IS
    v_theater_name VARCHAR2(50);
    v_location VARCHAR2(50);
BEGIN
    SELECT 극장이름, 위치 
    INTO v_theater_name, v_location
    FROM 극장
    WHERE 극장번호 = p_theater_no;

    DBMS_OUTPUT.PUT_LINE(v_theater_name || ' ' || v_location);
END;
/

-- 2. 새로운 극장 정보(극장번호, 극장이름, 위치)를 입력받아 극장 테이블에 삽입하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem2(
    p_theater_no IN NUMBER,
    p_theater_name IN VARCHAR2,
    p_location IN VARCHAR2
)
IS
BEGIN
    INSERT INTO 극장 (극장번호, 극장이름, 위치)
    VALUES (p_theater_no, p_theater_name, p_location);
    COMMIT;
END;
/

-- 3. 극장번호와 새로운 위치를 입력받아 해당 극장의 위치를 수정하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem3(
    p_theater_no IN NUMBER,
    p_new_location IN VARCHAR2
)
IS
BEGIN
    UPDATE 극장
    SET 위치 = p_new_location
    WHERE 극장번호 = p_theater_no;
    COMMIT;
END;
/

-- 4. 극장번호를 입력받아 해당 극장과 그 극장의 모든 상영관 정보를 삭제하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem4(
    p_theater_no IN NUMBER
)
IS
BEGIN
    DELETE FROM 상영관 WHERE 극장번호 = p_theater_no;
    DELETE FROM 극장 WHERE 극장번호 = p_theater_no;
    COMMIT;
END;
/

-- 5. 상영관번호와 극장번호를 입력받아 해당 상영관의 영화제목, 가격, 좌석수를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem5(
    p_screen_no IN NUMBER,
    p_theater_no IN NUMBER
)
IS
    v_movie_title VARCHAR2(50);
    v_price NUMBER;
    v_seats NUMBER;
BEGIN
    SELECT 영화제목, 가격, 좌석수 
    INTO v_movie_title, v_price, v_seats
    FROM 상영관
    WHERE 극장번호 = p_theater_no AND 상영관번호 = p_screen_no;

    DBMS_OUTPUT.PUT_LINE(v_movie_title || ' ' || v_price || ' ' || v_seats);
END;
/

-- 6. 특정 가격 이하의 상영관 목록을 모두 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem6(
    p_max_price IN NUMBER
)
IS
    CURSOR c_screens IS
        SELECT 극장번호, 상영관번호, 영화제목, 가격, 좌석수
        FROM 상영관
        WHERE 가격 <= p_max_price;
BEGIN
    FOR r_screen IN c_screens LOOP
        DBMS_OUTPUT.PUT_LINE(r_screen.극장번호 || ' ' || r_screen.상영관번호 || ' ' || r_screen.영화제목 || ' ' || r_screen.가격 || ' ' || r_screen.좌석수);
    END LOOP;
END;
/

-- 7. 특정 날짜를 입력받아 그날 예약된 모든 예약 정보(극장번호, 상영관번호, 고객번호, 좌석번호)를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem7(
    p_date IN DATE
)
IS
    CURSOR c_reservations IS
        SELECT 극장번호, 상영관번호, 고객번호, 좌석번호
        FROM 예약
        WHERE 날짜 = p_date;
BEGIN
    FOR r_res IN c_reservations LOOP
        DBMS_OUTPUT.PUT_LINE(r_res.극장번호 || ' ' || r_res.상영관번호 || ' ' || r_res.고객번호 || ' ' || r_res.좌석번호);
    END LOOP;
END;
/

-- 8. 고객번호를 입력받아 해당 고객의 전체 예약 내역(극장이름, 영화제목, 날짜, 좌석번호)을 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem8(
    p_cust_no IN NUMBER
)
IS
    CURSOR c_cust_res IS
        SELECT 극장이름, 영화제목, 날짜, 좌석번호
        FROM 예약
        JOIN 극장 ON 예약.극장번호 = 극장.극장번호
        JOIN 상영관 ON 예약.극장번호 = 상영관.극장번호 AND 예약.상영관번호 = 상영관.상영관번호
        WHERE 예약.고객번호 = p_cust_no;
BEGIN
    FOR r_res IN c_cust_res LOOP
        DBMS_OUTPUT.PUT_LINE(r_res.극장이름 || ' ' || r_res.영화제목 || ' ' || r_res.날짜 || ' ' || r_res.좌석번호);
    END LOOP;
END;
/

-- 9. 영화제목을 입력받아 해당 영화를 상영 중인 극장 이름과 위치를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem9(
    p_movie_title IN VARCHAR2
)
IS
    CURSOR c_theaters IS
        SELECT DISTINCT 극장이름, 위치
        FROM 상영관
        JOIN 극장 ON 상영관.극장번호 = 극장.극장번호
        WHERE 영화제목 = p_movie_title;
BEGIN
    FOR r_th IN c_theaters LOOP
        DBMS_OUTPUT.PUT_LINE(r_th.극장이름 || ' ' || r_th.위치);
    END LOOP;
END;
/

-- 10. 특정 극장번호를 입력받아 해당 극장의 상영관별 총 예약 건수를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem10(
    p_theater_no IN NUMBER
)
IS
    CURSOR c_counts IS
        SELECT 상영관.상영관번호, COUNT(고객번호) AS reservation_count
        FROM 상영관
        LEFT JOIN 예약 ON 상영관.극장번호 = 예약.극장번호 AND 상영관.상영관번호 = 예약.상영관번호
        WHERE 상영관.극장번호 = p_theater_no
        GROUP BY 상영관.상영관번호;
BEGIN
    FOR r_cnt IN c_counts LOOP
        DBMS_OUTPUT.PUT_LINE(r_cnt.상영관번호 || ' ' || r_cnt.reservation_count);
    END LOOP;
END;
/

-- 11. 극장 번호를 입력받아 해당 극장 전체 상영관의 평균 좌석수를 OUT 매개변수로 반환하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem11(
    p_theater_no IN NUMBER,
    p_avg_seats OUT NUMBER
)
IS
BEGIN
    SELECT AVG(좌석수) INTO p_avg_seats
    FROM 상영관
    WHERE 극장번호 = p_theater_no;
    
    IF p_avg_seats IS NULL THEN
        p_avg_seats := 0;
    END IF;
END;
/

-- 12. 상영관 번호와 극장 번호를 입력받아 해당 상영관의 좌석 예약률(예약건수 / 좌석수 × 100)을 계산하여 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem12(
    p_screen_no IN NUMBER,
    p_theater_no IN NUMBER
)
IS
    v_seats NUMBER;
    v_bookings NUMBER;
    v_rate NUMBER;
BEGIN
    SELECT 좌석수 INTO v_seats FROM 상영관 WHERE 극장번호 = p_theater_no AND 상영관번호 = p_screen_no;
    SELECT COUNT(*) INTO v_bookings FROM 예약 WHERE 극장번호 = p_theater_no AND 상영관번호 = p_screen_no;
    
    IF v_seats > 0 THEN
        v_rate := (v_bookings / v_seats) * 100;
    ELSE
        v_rate := 0;
    END IF;
    
    DBMS_OUTPUT.PUT_LINE(ROUND(v_rate, 2));
END;
/

-- 13. 특정 고객 번호를 입력받아 해당 고객이 지출한 총 예약 금액(예약 건수 × 가격)을 OUT 매개변수로 반환하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem13(
    p_cust_no IN NUMBER,
    p_total_spent OUT NUMBER
)
IS
BEGIN
    SELECT SUM(가격) INTO p_total_spent
    FROM 예약
    JOIN 상영관 ON 예약.극장번호 = 상영관.극장번호 AND 예약.상영관번호 = 상영관.상영관번호
    WHERE 고객번호 = p_cust_no;

    IF p_total_spent IS NULL THEN
        p_total_spent := 0;
    END IF;
END;
/

-- 14. 예약 삽입 시 해당 상영관의 좌석 수보다 예약 건수가 많으면 오류 메시지를 출력하고 삽입을 중단하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem14(
    p_theater_no IN NUMBER,
    p_screen_no IN NUMBER,
    p_cust_no IN NUMBER,
    p_seat_no IN NUMBER,
    p_date IN DATE
)
IS
    v_max_seats NUMBER;
    v_current_bookings NUMBER;
BEGIN
    SELECT 좌석수 INTO v_max_seats FROM 상영관 WHERE 극장번호 = p_theater_no AND 상영관번호 = p_screen_no;
    SELECT COUNT(*) INTO v_current_bookings FROM 예약 WHERE 극장번호 = p_theater_no AND 상영관번호 = p_screen_no AND 날짜 = p_date;

    IF v_current_bookings >= v_max_seats THEN
        DBMS_OUTPUT.PUT_LINE('오류');
    ELSE
        INSERT INTO 예약 (극장번호, 상영관번호, 고객번호, 좌석번호, 날짜)
        VALUES (p_theater_no, p_screen_no, p_cust_no, p_seat_no, p_date);
        COMMIT;
    END IF;
END;
/

-- 15. 특정 극장번호와 날짜를 입력받아, 그날 예약이 없는 상영관 목록을 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE theater_problem15(
    p_theater_no IN NUMBER,
    p_date IN DATE
)
IS
    CURSOR c_empty_screens IS
        SELECT 상영관번호, 영화제목
        FROM 상영관
        WHERE 극장번호 = p_theater_no
          AND 상영관번호 NOT IN (
              SELECT 상영관번호 
              FROM 예약 
              WHERE 극장번호 = p_theater_no AND 날짜 = p_date
          );
BEGIN
    FOR r_scr IN c_empty_screens LOOP
        DBMS_OUTPUT.PUT_LINE(r_scr.상영관번호 || ' ' || r_scr.영화제목);
    END LOOP;
END;
/

-- 1. 학번을 입력받아 해당 학생의 이름, 전공, 학년을 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem1(
    p_student_id IN NUMBER
)
IS
    v_name VARCHAR2(50);
    v_major VARCHAR2(50);
    v_grade NUMBER;
BEGIN
    SELECT 이름, 전공, 학년 
    INTO v_name, v_major, v_grade
    FROM 학생
    WHERE 학번 = p_student_id;

    DBMS_OUTPUT.PUT_LINE(v_name || ' ' || v_major || ' ' || v_grade);
END;
/

-- 2. 새로운 학생 정보(학번, 이름, 전공, 학년)를 입력받아 학생 테이블에 삽입하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem2(
    p_student_id IN NUMBER,
    p_name IN VARCHAR2,
    p_major IN VARCHAR2,
    p_grade IN NUMBER
)
IS
BEGIN
    INSERT INTO 학생 (학번, 이름, 전공, 학년)
    VALUES (p_student_id, p_name, p_major, p_grade);
    COMMIT;
END;
/

-- 3. 학번과 새로운 학년을 입력받아 해당 학생의 학년 정보를 수정하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem3(
    p_student_id IN NUMBER,
    p_new_grade IN NUMBER
)
IS
BEGIN
    UPDATE 학생
    SET 학년 = p_new_grade
    WHERE 학번 = p_student_id;
    COMMIT;
END;
/

-- 4. 학번을 입력받아 해당 학생의 수강 내역을 모두 삭제한 후 학생 정보도 삭제하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem4(
    p_student_id IN NUMBER
)
IS
BEGIN
    DELETE FROM 수강 WHERE 학번 = p_student_id;
    DELETE FROM 학생 WHERE 학번 = p_student_id;
    COMMIT;
END;
/

-- 5. 과목코드를 입력받아 해당 과목의 과목이름, 강의실, 요일, 담당교수를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem5(
    p_course_code IN VARCHAR2
)
IS
    v_course_name VARCHAR2(50);
    v_room VARCHAR2(50);
    v_day VARCHAR2(50);
    v_professor VARCHAR2(50);
BEGIN
    SELECT 과목이름, 강의실, 요일, 담당교수
    INTO v_course_name, v_room, v_day, v_professor
    FROM 과목
    WHERE 과목코드 = p_course_code;

    DBMS_OUTPUT.PUT_LINE(v_course_name || ' ' || v_room || ' ' || v_day || ' ' || v_professor);
END;
/

-- 6. 전공을 입력받아 해당 전공 학생들의 학번과 이름 전체를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem6(
    p_major IN VARCHAR2
)
IS
    CURSOR c_students IS
        SELECT 학번, 이름
        FROM 학생
        WHERE 전공 = p_major;
BEGIN
    FOR r_stu IN c_students LOOP
        DBMS_OUTPUT.PUT_LINE(r_stu.학번 || ' ' || r_stu.이름);
    END LOOP;
END;
/

-- 7. 학번을 입력받아 해당 학생이 수강한 과목명, 수강학기, 성적을 모두 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem7(
    p_student_id IN NUMBER
)
IS
    CURSOR c_courses IS
        SELECT 과목이름, 수강학기, 성적
        FROM 수강
        JOIN 과목 ON 수강.과목코드 = 과목.과목코드
        WHERE 수강.학번 = p_student_id;
BEGIN
    FOR r_crs IN c_courses LOOP
        DBMS_OUTPUT.PUT_LINE(r_crs.과목이름 || ' ' || r_crs.수강학기 || ' ' || r_crs.성적);
    END LOOP;
END;
/

-- 8. 담당교수 이름을 입력받아 해당 교수가 강의하는 과목을 수강한 학생들의 이름과 성적을 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem8(
    p_professor IN VARCHAR2
)
IS
    CURSOR c_prof_students IS
        SELECT 이름, 성적
        FROM 수강
        JOIN 학생 ON 수강.학번 = 학생.학번
        JOIN 과목 ON 수강.과목코드 = 과목.과목코드
        WHERE 담당교수 = p_professor;
BEGIN
    FOR r_stu IN c_prof_students LOOP
        DBMS_OUTPUT.PUT_LINE(r_stu.이름 || ' ' || r_stu.성적);
    END LOOP;
END;
/

-- 9. 수강학기를 입력받아 해당 학기에 수강 인원이 가장 많은 과목 이름과 인원수를 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem9(
    p_semester IN VARCHAR2
)
IS
    v_course_name VARCHAR2(50);
    v_student_count NUMBER;
BEGIN
    SELECT 과목이름, student_count
    INTO v_course_name, v_student_count
    FROM (
        SELECT 과목이름, COUNT(학번) AS student_count
        FROM 수강
        JOIN 과목 ON 수강.과목코드 = 과목.과목코드
        WHERE 수강학기 = p_semester
        GROUP BY 과목이름
        ORDER BY COUNT(학번) DESC
    )
    WHERE ROWNUM = 1;

    DBMS_OUTPUT.PUT_LINE(v_course_name || ' ' || v_student_count);
END;
/

-- 10. 특정 요일을 입력받아 그 요일에 강의가 있는 과목 목록과 강의실을 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem10(
    p_day IN VARCHAR2
)
IS
    CURSOR c_day_courses IS
        SELECT 과목이름, 강의실
        FROM 과목
        WHERE 요일 = p_day;
BEGIN
    FOR r_crs IN c_day_courses LOOP
        DBMS_OUTPUT.PUT_LINE(r_crs.과목이름 || ' ' || r_crs.강의실);
    END LOOP;
END;
/

-- 11. 학번을 입력받아 해당 학생의 전체 평균 성적을 OUT 매개변수로 반환하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem11(
    p_student_id IN NUMBER,
    p_avg_score OUT NUMBER
)
IS
BEGIN
    SELECT AVG(성적) INTO p_avg_score
    FROM 수강
    WHERE 학번 = p_student_id;

    IF p_avg_score IS NULL THEN
        p_avg_score := 0;
    END IF;
END;
/

-- 12. 과목코드를 입력받아 해당 과목의 수강생 평균 성적과 최고 성적, 최저 성적을 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem12(
    p_course_code IN VARCHAR2
)
IS
    v_avg NUMBER;
    v_max NUMBER;
    v_min NUMBER;
BEGIN
    SELECT AVG(성적), MAX(성적), MIN(성적)
    INTO v_avg, v_max, v_min
    FROM 수강
    WHERE 과목코드 = p_course_code;

    DBMS_OUTPUT.PUT_LINE(ROUND(v_avg, 2) || ' ' || v_max || ' ' || v_min);
END;
/

-- 13. 학년을 입력받아 해당 학년 학생들의 전공별 평균 성적을 출력하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem13(
    p_grade IN NUMBER
)
IS
    CURSOR c_stats IS
        SELECT 전공, AVG(성적) AS avg_score
        FROM 수강
        JOIN 학생 ON 수강.학번 = 학생.학번
        WHERE 학년 = p_grade
        GROUP BY 전공;
BEGIN
    FOR r_stat IN c_stats LOOP
        DBMS_OUTPUT.PUT_LINE(r_stat.전공 || ' ' || ROUND(r_stat.avg_score, 2));
    END LOOP;
END;
/

-- 14. 수강 신청 시 동일 학번 and 과목코드로 이미 수강 내역이 존재하면 '이미 수강 중입니다' 메시지를 출력하고 삽입을 중단하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem14(
    p_course_code IN VARCHAR2,
    p_student_id IN NUMBER,
    p_semester IN VARCHAR2,
    p_score IN NUMBER
)
IS
    v_exists NUMBER;
BEGIN
    SELECT COUNT(*) INTO v_exists
    FROM 수강
    WHERE 과목코드 = p_course_code AND 학번 = p_student_id;

    IF v_exists > 0 THEN
        DBMS_OUTPUT.PUT_LINE('오류');
    ELSE
        INSERT INTO 수강 (과목코드, 학번, 수강학기, 성적)
        VALUES (p_course_code, p_student_id, p_semester, p_score);
        COMMIT;
    END IF;
END;
/

-- 15. 특정 수강학기를 입력받아 성적이 NULL인 학생의 학번, 이름, 과목이름을 출력하고 성적 미입력 건수를 OUT 매개변수로 반환하는 프로시저를 작성하시오.
CREATE OR REPLACE PROCEDURE student_problem15(
    p_semester IN VARCHAR2,
    p_null_count OUT NUMBER
)
IS
    CURSOR c_null_students IS
        SELECT 수강.학번, 이름, 과목이름
        FROM 수강
        JOIN 학생 ON 수강.학번 = 학생.학번
        JOIN 과목 ON 수강.과목코드 = 과목.과목코드
        WHERE 수강학기 = p_semester AND 성적 IS NULL;
BEGIN
    p_null_count := 0;

    FOR r_stu IN c_null_students LOOP
        DBMS_OUTPUT.PUT_LINE(r_stu.학번 || ' ' || r_stu.이름 || ' ' || r_stu.과목이름);
        p_null_count := p_null_count + 1;
    END LOOP;
END;
/