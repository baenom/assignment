import oracledb
try:
    user="system"
    password="manager1"
    dsn="127.0.0.1:1521/FREE"
    con = oracledb.connect(user=user, password=password, dsn=dsn)
except Exception as e:
    print(e)
try:
    cursor = con.cursor()

    cursor.execute("SELECT * FROM Book")
    data = cursor.fetchall()

    for i in data :
        print(i)
    cursor.close()
    con.close()
except Exception as e:
    print(e)

