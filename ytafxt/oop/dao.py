import sqlite3

from ytafxt.oop.models import SungJuk


# 성적 DAO 클래스
class SungJukDAO:
    # 데이터베이스 연결객체와 커서생성
    @staticmethod
    def _make_conn():
        conn = sqlite3.connect('db/python.db')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 연결객체와 커서 종료
    @staticmethod
    def _dis_conn(conn, cursor):
        cursor.close()
        conn.close()

    @staticmethod
    def insert_sungjuk(sj):
        sql = 'insert into sungjuk(name, korean, english, math, total, average, grade)\
           values (?, ?, ?, ?, ?, ?, ?)'
        conn, cursor = SungJukDAO._make_conn()
        params = (sj.name, sj.korean, sj.english, sj.math, sj.total, sj.average, sj.grade)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def select_sungjuk():
        sjs = []
        sql = 'select sjno, name, korean, english, math, substr(regdate,0,11) regdate from sungjuk'
        conn, cursor = SungJukDAO._make_conn()
        cursor.execute(sql)

        rs = cursor.fetchall()
        for r in rs:    # 조회 결과를 SungJuk 객체에 개별 저장
            sj = SungJuk(r[1], r[2], r[3], r[4])
            sj.sjno = r[0]
            sj.regdate = r[5]
            sjs.append(sj)

        SungJukDAO._dis_conn(conn, cursor)
        return sjs

    @staticmethod
    def selectone_sungjuk(sjno):
        sql = 'select * from sungjuk where sjno = ?'
        conn, cursor = SungJukDAO._make_conn()
        params = (sjno,)
        cursor.execute(sql, params)
        rs = cursor.fetchone()
        if rs:
            sj = SungJuk(rs[1], rs[2], rs[3], rs[4])
            sj.sjno = rs[0]
            sj.total = rs[5]
            sj.average = rs[6]
            sj.grade = rs[7]
            sj.regdate = rs[8]
        else:
            sj = None

        SungJukDAO._dis_conn(conn, cursor)
        return sj

    def update_sungjuk(self):
        pass

    @staticmethod
    def delete_sungjuk(sjno):
        sql = 'delete from sungjuk where sjno = ?'
        conn, cursor = SungJukDAO._make_conn()
        params = (sjno,)
        cursor.execute(sql, params)
        rss = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return rss
