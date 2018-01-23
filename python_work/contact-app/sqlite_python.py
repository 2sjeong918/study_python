import sqlite3

# try:
#     con = sqlite3.connect("contacts.db")
#     print('con:',con)
# except Exception as err:
#     print('데이터베이스 에러 : %s'%err)
# finally:
#     con.close()

# with sqlite3.connect("contacts.db") as con:
#     sql="""
#         INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL)
#         VALUES('고길동동', '010-1111-3333', 'GOGO@naver.com')
#     """;
#     try:
#         con.execute(sql)
#         print('데이터 삽입 저장 완료')
#     except Exception as err:
#         print('데이터베이스 에러: %s'%err)
#     else:
#         con.commit()

# name = input('이름 : ')
# cell_phone = input('전화번호 : ')
# email = input('이메일 : ')
#
# with sqlite3.connect("contacts.db") as con:
#     sql = """
#         INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL)
#         VALUES(?, ?, ?)
#     """;
#     try:
#         con.execute(sql, (name, cell_phone, email))
#         print('데이터 삽입 저장 완료')
#     except Exception as err:
#         print('데이터베이스 에러: %s' % err)
#     else:
#         con.commit()

# name = '이세돌'
# cell_phone = '010-3333-3333'
# email = 'lee@gmail.com'
#
# with sqlite3.connect("contacts.db") as con:
#     sql = """
#         INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL)
#         VALUES(:name, :cell_phone, :email)
#     """;
#     try:
#         con.execute(sql,
#                     {'name' : name, 'cell_phone': cell_phone, 'email': email})
#         print('데이터 삽입 저장 완료')
#     except Exception as err:
#         print('데이터베이스 에러: %s' % err)
#     else:
#         con.commit()

# data = (
#     ('홍길동1', '010-1111-1111', 'h1.gmail.com'),
#     ('홍길동2', '010-2222-2222', 'h2.gmail.com'),
#     ('홍길동3', '010-3333-3333', 'h3.gmail.com')
# )
#
# with sqlite3.connect("contacts.db") as con:
#     sql = """
#         INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL)
#         VALUES(?, ?, ?)
#     """;
#     try:
#         con.executemany(sql, data)
#         print('데이터 삽입 완료')
#     except Exception as err:
#         print('데이터 베이스 에러 : %s'%err)
#     else:
#         con.commit()

with sqlite3.connect('contacts.db') as con:
    sql = """
        SELECT * FROM CONTACTS
        where NAME = "ddd"
    """;
    # try:
    #     cursor = con.cursor()
    #     cursor.execute(sql)
    #     for row in cursor:
    #         print(row)
    #       cursor는 이터러블 객체이기 때문에 __next__로 반복문을 돈다

    try:
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchone()
        print(type(rows))
        # for row in rows:
        #     print(row)
    except Exception as err:
        print('데이터베이스 에러 %s' %err)
    else:
        con.commit()
    
    #  ORM( object relationship model ) > 비슷한 부분을 중복되지 않게 객체로 만들어서 서로 공유할 수 있도록 만듦