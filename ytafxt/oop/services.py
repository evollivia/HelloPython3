from ytafxt.oop.models import SungJuk
from ytafxt.oop.dao import SungJukDAO as sjdao

# 성적 서비스 클래스
class SungJukService:
    # 데코레이터 : 함수에 추가기능을 구현할때 사용
    @staticmethod   # 정적static 매서드 : 객체화 없이 바로 사용 가능한 매서드
                    # 정적 매서드로 정의된 함수는 self 매개변수 지정 x
                    # 호출 방법 : 클래스명.함수명
    def display_menu():
        # 프로그램 메뉴 정의
        main_menu = '''
==========================
    성적처리 프로그램 V8
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

    @staticmethod
    def read_sungjuk():
        name = (input(f'새로운 학생 이름 : '))
        korean = (int(input(f'새로운 학생 국어 성적 : ')))
        english = (int(input(f'새로운 학생 영어 성적 : ')))
        math = (int(input(f'새로운 학생 수학 성적 : ')))
        return SungJuk(name, korean, english, math)

    @staticmethod
    def add_sungjuk():
        sj = SungJukService.read_sungjuk()
        SungJukService.compute_sungjuk(sj)
        cnt = sjdao.insert_sungjuk(sj)
        result = f'{cnt}건의 데이터 추가 성공'
        print(result)

    @staticmethod
    def compute_sungjuk(sj):
        sj.total = sj.korean + sj.english + sj.math
        sj.average = sj.total / 3
        sj.grade = '가'
        if (sj.average >= 90): sj.grade = '수'
        elif (sj.average >= 80): sj.grade = '우'
        elif (sj.average >= 70): sj.grade = '미'
        elif (sj.average >= 60): sj.grade = '양'

    @staticmethod
    def show_sungjuk():
        result = ''
        sjs = sjdao.select_sungjuk()
        for sj in sjs:
            result += (f'번호 : {sj.sjno}, 이름 : {sj.name}, 국어 : {sj.korean}, '
                       f'영어 : {sj.english} ,수학 : {sj.math}, 등록일 : {sj.regdate}\n')
        print(result)

    @staticmethod
    def showone_sungjuk():
        pass

    @staticmethod
    def modify_sungjuk():
        pass

    def readagain_sungjuk(self):
        pass

    @staticmethod
    def remove_sungjuk():
        pass

