import sqlite3



with sqlite3.connect('contacts.db') as con:
    sql = """
        DELETE FROM CONTACTS WHERE NAME=?
    """;
    try:
        name = input('삭제할 이름 : ')
        cursor = con.execute(sql, (name,))
        print(cursor.rowcount)
    except Exception as err:
        print('데이터 베이스 에러 : %s'%err)
    else:
        con.commit()

with sqlite3.connect('contacts.db') as con:
    sql = """
        SELECT * FROM CONTACTS
    """;
    try:
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    except Exception as err:
        print('데이터베이스 에러 %s' %err)
    else:
        con.commit()