from ytafxt.oop.models import SungJuk
from ytafxt.oop.dao import SungJukDAO as sjdao


# 성적 서비스 클래스
class SungJukService:
    # 데코레이터 : 함수에 추가기능을 구현할때 사용
    @staticmethod  # 정적static 매서드 : 객체화 없이 바로 사용 가능한 매서드
    # 정적 매서드로 정의된 함수는 self 매개변수 지정 x
    # 호출 방법 : 클래스명.함수명
    def display_menu():
        """
        프로그램 메뉴를 출력하고 사용자의 선택을 반환
        :return menu: 선택된 메뉴 항목
        """
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
        """
        학생의 이름, 성적을 입려받음
        :return: SungJuk 객체
        """
        name = (input(f'새로운 학생 이름 : '))
        korean = (int(input(f'새로운 학생 국어 성적 : ')))
        english = (int(input(f'새로운 학생 영어 성적 : ')))
        math = (int(input(f'새로운 학생 수학 성적 : ')))
        return SungJuk(name, korean, english, math)

    @staticmethod
    def add_sungjuk():
        """
        성적 데이터를 입력받고 처리한 후 데이터베이스에 저장
        :return:
        """
        sj = SungJukService.read_sungjuk()
        SungJukService.compute_sungjuk(sj)
        cnt = sjdao.insert_sungjuk(sj)
        result = f'{cnt}건의 데이터 추가 성공'
        print(result)

    @staticmethod
    def compute_sungjuk(sj):
        """
        입력받은 성적 데이터를 계산하여 총점, 평균, 등급을 구함
        :param sj: Sungjuk 클래스의 인스턴스 (korean, english, math 속성이 있어야 함)
        :return: None. sj 인스턴스의 총점, 평균, 등급 속성을 업데이트
        """
        sj.total = sj.korean + sj.english + sj.math
        sj.average = sj.total / 3
        sj.grade = '가'
        if (sj.average >= 90):
            sj.grade = '수'
        elif (sj.average >= 80):
            sj.grade = '우'
        elif (sj.average >= 70):
            sj.grade = '미'
        elif (sj.average >= 60):
            sj.grade = '양'

    @staticmethod
    def show_sungjuk():
        """
        성적 데이터를 조회하여 출력
        :return:
        """
        result = ''
        sjs = sjdao.select_sungjuk()
        for sj in sjs:
            result += (f'번호 : {sj.sjno}, 이름 : {sj.name}, 국어 : {sj.korean}, '
                       f'영어 : {sj.english} ,수학 : {sj.math}, 등록일 : {sj.regdate}\n')
        print(result)

    @staticmethod
    def showone_sungjuk():
        """
        성적 데이터를 상세 조회하여 출력
        :return:
        """
        sjno = input('조회할 학생 번호는? ')
        result = '데이터가 존재하지 않아요'
        sj = sjdao.selectone_sungjuk(sjno)
        if sj:  # 조회한 데이터가 존재한다면
            result = (f'번호 : {sj.sjno}, 이름 : {sj.name}, 국어 : {sj.korean}, 영어 : {sj.english} ,수학 : {sj.math}\n'
                      f'총점 : {sj.total}, 평균 : {sj.average:.1f}, 학점 : {sj.grade}, 등록일 : {sj.regdate}')
        print(result)

    @staticmethod
    def modify_sungjuk():
        """
        학생의 성적 데이터 수정
        :return:
        """
        sjno = int(input('수정할 학생번호를 입력하세요. '))
        sj = sjdao.selectone_sungjuk(sjno)
        result = '수정할 데이터가 존재하지 않아요'
        if sj:
            sj = SungJukService.readagain_sungjuk(sj)
            cnt = sjdao.update_sungjuk(sj)
            result = f'{cnt}건의 데이터가 수정됨'
            print(result)


    @staticmethod
    def readagain_sungjuk(sj):
        """
        학생의 성적 정보를 다시 입력받아 수정된 성적 객체를 반환
        :param sj: 기존의 성적 객체
        :return: 수정된 성적 객체
        """
        nsj = SungJuk(sj.name, None, None, None)
        nsj.korean = int(input(f'{sj.name} 학생의 국어 성적 수정({sj.korean}) : '))
        nsj.english = int(input(f'{sj.name} 학생의 영어 성적 수정({sj.english}) : '))
        nsj.math = int(input(f'{sj.name} 학생의 수학 성적 수정({sj.math}) : '))
        SungJukService.compute_sungjuk(nsj)
        nsj.sjno = sj.sjno  # nsj[8] 학생번호
        return nsj

    @staticmethod
    def remove_sungjuk():
        """
        학생 번호를 기반으로 성적 데이터를 삭제
        :return:
        """
        sjno = int(input('삭제할 학생번호를 입력하세요. '))
        result = '데이터가 존재하지 않음'
        cnt = sjdao.delete_sungjuk(sjno)
        if cnt > 0:
            result = f'{cnt}건의 데이터가 삭제됨'
        print(result)
