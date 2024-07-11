# 수식 / 표현식 expression
# 숫자, 변수, 연산자를 이용해서 수학적 관계를 나타내는 것
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 -> 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연상의 대상들을 의미

# 산술연산자

# 자료형 승격 promotion

# 매출액 입력시 총합을 출력
firstm = int(input('1월 매출 : '))
secondm = int(input('2월 매출 : '))
thirdm = int(input('3월 매출 : '))
total = firstm + secondm + thirdm
print(f'''1분기 전체 매출 : {total} 원''')

# 1분기 수익 계산
firstquarters = int(input('1월 매출 : '))
firstquarterp = int(input('1월 매입 : '))
sales = firstquarters - firstquarterp
print(f'''수익 : {sales} 원''')

# 방의 넓이 구하기
width = int(input('가로길이 : '))
length = int(input('세로길이 : '))
area = width * length
print(f'''넓이 : {area} cm^2''')

# 신체질량지수BMI 구하기
weight = float(input('몸무계(kg) : '))
hight = float(input('신장(m) : '))
BMI = int(weight / hight ** 2)
print(f'''BMI = {BMI}''')

# 홀짝게임
coin = int(input('손 안에 동전 수를 입력하세요 : '))
if coin % 2 == 0:
    print(0)
else:
    print(1)

coins = int(input('손 안에 동전 수를 입력하세요 : '))
result = coins % 2
print(f'{coins}')

# 빵나누기
students = 97 // 3
left = 97 % 3
print(f'''
빵을 나누어 줄 수 있는 학생수 : {students}
남는 빵 개수 : {left}
''')

# 전염병 예상 감염자 구하기
# 1일차 -> 2명
# 2일차 -> 4명
# 3일차 -> 8명
# 4일차 -> 16명
# ...
# n일차 -> 2 ** n명
day = int(input('감염발생 후 일자 : '))
infectedp = 2 ** day
print(f'''
{day}일 이후 예상 감염자 수 : {infectedp}
''')

# 할당 연산자

# 논리 연산자

# 논리연산자 단축식 평가

# 삼항 연산자
# 조건문을 한 줄록 표형할 수 있는 연산자
# 참일때 값 if 조건식 else 거짓일때 값
myscore = 70
result = '합격' if myscore >= 90 else '불합격'
print(result)

# 복리계산기
save = 5_000_000
rate = 0.05
years = 5

save = save + (save * rate)
save = save + (save * rate)
save = save + (save * rate)
save = save + (save * rate)
save = save + (save * rate)
print(f'5년 후 총 수령액 : {int(save)} 원')

ci = int(save * ((1 + rate) ** years))
print(f'{years}년 후 총 수령액 : {ci} 원')

# 범퍼카 탑승
hight = float(input('어린이의 신장을 입력하세요 : '))
isRide = hight >= 120
print(isRide)

hight = float(input('어린이의 신장을 입력하세요 : '))
isRide = 'True' if hight >= 120 else 'False'
print(isRide)

# 범퍼카탑승 가능 판별
hight = float(input('어린이의 신장을 입력하세요 : '))
isRide = (hight >= 120) and (hight < 170)
print(isRide)

isRide = 'True' if hight >= 120 and hight < 170 else 'False'
print(isRide)

# 적자/흑자 판별
income = int(input('수입 : '))
outcome = int(input('지출 : '))
disc = '흑자' if (income > outcome) else '적자'
print(f'{disc}')
