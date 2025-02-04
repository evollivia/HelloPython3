import sqlite3


# 성적 데이터 총 갯수 조회
def getTotalSungJuk():
    sql = 'select count(sjno) + 1 toal from sungjuk;'
    cnt = 0
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchall()
    for r in rs:
        cnt = r[0]
    cursor.close()
    conn.close()
    return cnt


# 처리된 성적데이터를 테이블에 저장
def newSungJuk(sj):
    sql = 'insert into sungjuk(name, korean, english, math, total, average, grade)\
           values (?, ?, ?, ?, ?, ?, ?)'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sj[0], sj[1], sj[2], sj[3], sj[4], sj[5], sj[6])
    cursor.execute(sql, params)
    print(cursor.rowcount, '건의 데이터가 추가됨')
    conn.commit()
    cursor.close()
    conn.close()


# 성적 데이터 전체 조회
def readAllSungJuk():
    sql = 'select sjno, name, korean, english, math, substr(regdate,0,11) regdate from sungjuk'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    sjs = cursor.fetchall()
    cursor.close()
    conn.close()
    return sjs


# 학생 한명의 성적 상세 조회
def readOneSungJuk(sjno):
    sql = 'select * from sungjuk where sjno = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sjno,)
    cursor.execute(sql, params)
    sj = cursor.fetchone()
    cursor.close()
    conn.close()
    return sj


#
def delSungJuk(sjno):
    sql = 'delete from sungjuk where sjno = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sjno,)
    cursor.execute(sql, params)
    print(cursor.rowcount, ' 건의 데이터가 삭제됨')
    conn.commit()
    cursor.close()
    conn.close()

#
def updateSungJuk(sj):
    sql = 'update sungjuk set korean = ?, english = ?, math = ?, total = ?, average = ?, grade = ?\
           where sjno = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (sj[1], sj[2], sj[3], sj[4], sj[5], sj[6], sj[7])
    cursor.execute(sql, params)
    print(cursor.rowcount, '건의 데이터가 수정됨')
    conn.commit()
    cursor.close()
    conn.close()
