# import sqlite3
import pymysql

from ytafxt.oop.models import SungJuk

# 데이터베이스 연결 문자열
host = '3.34.139.36'
dbname = 'clouds2024'
user = 'clouds2024'
passwd = 'clouds2024'

# 성적 DAO 클래스
class SungJukDAO:
    # 데이터베이스 연결객체와 커서생성
    @staticmethod
    def _make_conn():
        """
        데이터베이스 연결을 생성하고 커서를 반환
        :return: conn, cursor
        """
        conn = pymysql.connect(host=host, user=user, password=passwd, database=dbname, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 연결객체와 커서 종료
    @staticmethod
    def _dis_conn(conn, cursor):
        """
        데이터베이스 연결과 커서를 닫음
        :param conn: 데이터베이스 연결 객체
        :param cursor: 데이터베이스 커서 객체
        :return:
        """
        cursor.close()
        conn.close()

    @staticmethod
    def insert_sungjuk(sj):
        """
        입력한 성적 데이터를 성적 테이블에 저장
        :param sj : 테이블에 저장할 성적데이터
        :return cnt : 테이블에 성공적으로 저장된 데이터 건수
        """
        sql = 'insert into sungjuk(name, korean, english, math, total, average, grade)\
           values (%s, %s, %s, %s, %s, %s, %s)'
        conn, cursor = SungJukDAO._make_conn()
        params = (sj.name, sj.korean, sj.english, sj.math, sj.total, sj.average, sj.grade)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def select_sungjuk():
        """
        성적 테이블에서 모든 성적 데이터(번호, 이름, 국어, 영어, 수학, 등록일)를 읽어옴
        :return sjs: 조회된 성적 데이터 객체
        """
        sjs = []
        sql = 'select sjno, name, korean, english, math, substr(regdate,1,11) regdate from sungjuk'
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
        """
        성적 테이블에서 특정 학생의 성적 데이터를 읽어옴
        :param sjno : 조회할 학생의 학생번호
        :return sj : 조회된 학생의 성적데이터
        """
        sql = 'select * from sungjuk where sjno = %s'
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

    @staticmethod
    def update_sungjuk(sj):
        """
        수정한 성적 데이터를 업데이트
        :param sj: 성적 데이터
        :return cnt: 수정된 성적 데이터의 갯수
        """
        sql = 'update sungjuk set korean = %s, english = %s, math = %s, total = %s, average = %s, grade = %s\
           where sjno = %s'
        conn, cursor = SungJukDAO._make_conn()
        params = (sj.korean, sj.english, sj.math, sj.total, sj.average, sj.grade, sj.sjno)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def delete_sungjuk(sjno):
        """
        선택한 학생번호의 성적 데이터를 삭제
        :param sjno: 삭제할 학생의 학생번호
        :return rss: 삭제된 성적 데이터의 갯수
        """
        sql = 'delete from sungjuk where sjno = %s'
        conn, cursor = SungJukDAO._make_conn()
        params = (sjno,)
        cursor.execute(sql, params)
        rss = cursor.rowcount
        conn.commit()
        SungJukDAO._dis_conn(conn, cursor)
        return rss
