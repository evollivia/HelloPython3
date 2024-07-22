# 사원등록 프로그램
# 사원 데이터 기반 CRUD 기능이 제공되는 프로그램
# 사원 - empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid
# 조회 - 사원번호, 이름, 이메일, 직책, 부서번호
# 상세조회 - 특정 사원 번호 대상 모든 컬럼 추가
# emp 테이블

import sys
import ytafxt.emp as emp

# 메뉴 출력 및 메뉴별 처리
while True:
    # 메뉴 입력받음
    menu = emp.displayMenu()

    # 선택한 메뉴에 따라 해당 기능 제공
    if menu == '1':
        print('사원 데이터 추가')
        emp.addEmpData()

    elif menu == '2':
        print('사원 데이터 조회')
        emp.showEmpData()

    elif menu == '3':
        print('사원 데이터 상세조회')
        emp.showOneEmpData()

    elif menu == '4':
        print('사원 데이터 수정')

    elif menu == '5':
        print('사원 데이터 삭제')

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)

    else:
        print('메뉴를 잘못 선택하셨습니다')
