import ytafxt.empDAO as empdao

# 메뉴 선택 창
def displayMenu():
    # 프로그램 메뉴 정의
    main_menu = '''
===========================
    사원 정보 관리 프로그램    
===========================
   1. 사원 데이터 추가
   2. 사원 데이터 조회
   3. 사원 데이터 상세조회
   4. 사원 데이터 수정
   5. 사원 데이터 삭제
   0. 프로그램 종료
============================
'''
    print(main_menu, end='')
    menu = input('메뉴를 선택하세요 : ')
    return menu

#####################################################

# 사원 데이터 입력받는 함수
def readEmpData():
    data = []
    cnt = empdao.getTotalEmpData()
    data.append(input(f'{cnt}번 사원 ID : '))
    data.append(input(f'{cnt}번 사원 First Name : '))
    data.append(input(f'{cnt}번 사원 Last Name : '))
    data.append(input(f'{cnt}번 사원 Email : '))
    data.append(input(f'{cnt}번 사원 Phone Number : '))
    data.append(input(f'{cnt}번 사원 Hire Date : '))
    data.append(input(f'{cnt}번 사원 Job Id : '))
    data.append(input(f'{cnt}번 사원 Salary : '))
    data.append(input(f'{cnt}번 사원 Commission Pct(없으면 0) : '))
    data.append(input(f'{cnt}번 사원 Manager Id(없으면 0) : '))
    data.append(input(f'{cnt}번 사원 Department Id(없으면 0) : '))
    return data

# 입력받은 사원 데이터를 테이블에 저장
# 입력받은 수당, 매니저번호, 부서번호는 적절한 형변환 필요
def addEmpData():
    data =readEmpData()
    data[8] = float(data[8]) if data[8] != 0 else None
    data[9] = int(data[9]) if data[9] != 0 else 'null'
    data[10] = int(data[10]) if data[10] != 0 else 'null'
    empdao.newEmpData(data)


# 테이블에 저장된 사원 데이터들 중 기본 데이터만 모아서 출력
def showEmpData():
    result = ''
    datas = empdao.readAllEmpData()
    for data in datas:
        result += f'사원번호 : {data[0]}, 이름 : {data[1]}, 이메일 : {data[2]}, 직책 : {data[3]} ,부서번호 : {data[4]}\n'
    print(result)

# 사원번호로 사원 데이터 조회 후 출력
def showOneEmpData():
    empid = input('조회할 사원 번호를 입력하세요. ')
    result = '데이터가 존재하지 않아요'
    data = empdao.readOneEmpData(empid)
    if data:      # 조회한 데이터가 존재한다면
        result = (f'''Employee ID     : {data[0]} 
First Name      : {data[1]} 
Last Name       : {data[2]} 
Email           : {data[3]}
Phone Number    : {data[4]}
Hire Date       : {data[5]} 
Job ID          : {data[6]} 
Salary          : {data[7]} 
Commission PCT  : {data[8]} 
Manager ID      : {data[9]}
Department ID   : {data[10]:}''')
    print(result)
