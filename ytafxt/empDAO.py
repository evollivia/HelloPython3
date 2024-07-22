import sqlite3

# 성적 데이터 총 갯수 조회
def getTotalEmpData():
    sql = 'select count(empid) + 1 toal from Employees;'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchone()
    cnt = rs[0]
    cursor.close()
    conn.close()
    return cnt

# 사원 데이터를 테이블에 저장
def newEmpData(data):
    sql = "insert into Employees values (?, ?, ?, ?, ?, ?, ?, ?, ?, nullif(?,'null'), nullif(?,'null'))"
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
    cursor.execute(sql, params)
    print(cursor.rowcount, '건의 데이터가 추가됨')
    conn.commit()
    cursor.close()
    conn.close()

# 사원 데이터 전체 조회
def readAllEmpData():
    sql = 'select empid, fname, email, jobid, deptid from Employees'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()
    conn.close()
    return datas

# 사원 한명의 성적 상세 조회
def readOneEmpData(empid):
    sql = 'select * from Employees where empid = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (empid, )
    cursor.execute(sql,params)
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data

#
def delEmpData(empid):
    sql = 'delete from Employees where empid = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (empid,)
    cursor.execute(sql, params)
    cnt = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return  cnt


