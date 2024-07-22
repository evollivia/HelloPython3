import sqlite3

def displayMenu():
    # 프로그램 메뉴 정의
    main_menu = '''
==========================
    성적처리 프로그램 V5
==========================
   1. 성적 데이터 추가
   2. 성적 데이터 조회
   3. 성적 데이터 상세조회
   4. 성적 데이터 수정
   5. 성적 데이터 삭제
   0. 성적 프로그램 종료
==========================
'''
    print(main_menu, end='')
    menu = input('메뉴를 선택하세요 : ')
    return menu


# 성적 데이터 입력받는 함수
def readSungJuk():
    sj = []
    cnt = getTotalSungJuk()
    sj.append(input(f'{cnt+1}학생 이름 : '))
    sj.append(int(input(f'{cnt+1}학생 국어 성적 : ')))
    sj.append(int(input(f'{cnt+1}학생 영어 성적 : ')))
    sj.append(int(input(f'{cnt+1}학생 수학 성적 : ')))
    return sj

# 입력받은 성적 데이터를 처리하고 테이블에 저장
def addSungJuk(sj):
    computeSunJuk(sj)
    newSungJuk(sj)

# 테이블에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    sjs = readAllSungJuk()
    for sj in sjs:
        result += f'이름 : {sj[0]}, 국어 : {sj[1]}, 영어 : {sj[2]} ,수학 : {sj[3]}\n'
    print(result)

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

# 입력한 성적 데이터에 대해 성적처리하는 함수
def computeSunJuk(sj):
    sj.append(sj[1] + sj[2] + sj[3])
    sj.append(sj[4] / 3)
    grd = '수' if sj[5] >= 90 else \
        '우' if sj[5] >= 80 else \
            '미' if sj[5] >= 70 else \
                '양' if sj[5] >= 60 else '가'
    sj.append(grd)

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

#
def readAllSungJuk():
    sql = 'select name, korean, english, math from sungjuk'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    sjs = cursor.fetchall()
    cursor.close()
    conn.close()
    return sjs


