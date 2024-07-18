# 모듈
# 매우 복잡하고 긴 코드를 하나의 파일에
# 모두 작성하는 것은 비효율적일 수 있음 - 유지보수 힘듦
# 또한, 여러 사람들과 함께 개발하는 경우
# 작업분담, 작업결과물 통합 역시 어려움

# 모듈 방식의 개발을 이용하려면
# 사용 용도에 따라 파일별로 나눠 작성 가능
# 타인이 만들어 둔 토드를 자신의 프로그램에 활용 가능
# 따라서, 모듈은 변수/함수/클래스들을 모아둔 파일

# 모듈은 현재 디렉토리에 있는 파일이나
# 파이썬 라이브러리, 디렉토리에 있는 파일을 불러올 수 있음
# 사용자/venv/py310/Lib/site-package

# 모듈 불러오기
# import 명령을 이용해서 불러올 수 있음
# 모듈 내 정의된 함구/클래스를 사용하려면
# 모듈명.함수명, 모듈명.클래스 형식으로 코드 작성

import ytafxt.hello

ytafxt.hello.sayHello()

###########################

from ytafxt import hello

hello.sayHello()

###########################

from ytafxt2 import hello2

hello2.sayHello2()

# 모듈 사용하기1 - 모듈명.함수명
import ytafxt.calc

val = ytafxt.calc.add(10, 5)
print(val)

# 모듈 사용하기2 - 함수명
from ytafxt.calc import add
from ytafxt.calc import div

val = add(10, 5)
val2 = div(10, 5)
print(val)
print(val2)

# 모듈 사용하기3 - 함수명
from ytafxt.calc import *

val = mul(10, 5)
val2 = minus(10, 5)
print(val)
print(val2)

# 모듈 사용하기4 - 별칭
import ytafxt.calc as zc

val = zc.add(10,20)
print(val)

# 외부 모듈 사용하기
# 내장 모듈이나 사용자 정의 모듈 이외에
# 다른 조직/기관이나 개인이 만든 모듈을 사용하려면
# 'pip install 모듈명'으로 설치하면 됨
# pip install scikit-learn
# pip install pymysql
# pip install fastapi

# ytafxt.example에 각 문제에 대한 모듈 작성
# 단위 환산(readUnit/printUnits/convertUnit)
mm = float(input('길이(mm)를 입력하세요'))

units = [mm]
units.append(mm * 0.1)
units.append(mm * 0.001)
units.append(mm * 0.03937)
units.append(mm * 0.003291)

print(f'''
    {units[0]} mm --> {units[1]} cm
    {units[0]} mm --> {units[2]} m
    {units[0]} mm --> {units[3]} inch
    {units[0]} mm --> {units[4]} ft
    ''')

import ytafxt.example as ex
mm = ex.readUnit()
units = ex.convertUnit(mm)
ex.printUnits(units)


# 할인된 산품 가격표 출력(readDiscount/printPtices/discountPtice)
product = [['쌀', 9900], ['상추', 1900],['고추', 2900],['마늘', 8900],['통닭', 5600],['햄', 6900],['치즈', 3900]]
print(f'''
{'-'*39}
-- 한빛마트 오늘의 할인 가격표 출력 시스템 --
{'-'*39}''')
dc = int(input('오늘의 할인율을 입력하세요. '))
for p in product:
    originprice = p[1]
    dcprice = originprice * ((100 - dc) / 100)
    print(f'''{p[0]}\t: {p[1]} 원 {dc} %DC -> {dcprice:.0f} 원''')
print('-'*39)

import ytafxt.example as dcex
rate = dcex.readDiscount()
dcprice = dcex.discountPrice(rate)
dcex.printPrices(dcprice, rate)


# 주민등록번호 길이가 13자리인지 확인합니다.
# 뒤 7자리 중 첫 번째 숫자가 1, 2, 3, 4 중 하나인지 확인합니다. (1, 3은 남자, 2, 4는 여자를 의미)
# 뒤 7자리 중 첫 번째 숫자를 제외한 나머지 6자리가 유효한 값인지 확인합니다. (000001 ~ 899999 사이의 값)
# 주민등록번호 유효성 검사 공식에 따라 계산한 결과가 맞는지 확인합니다.
# 이 때 은 다음과 같습니다.

# 주민등록번호 유효성 검사 공식
# 주민등록번호 앞 12자리에 각각 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 곱한 값을 모두 더합니다.
# 그 결과값을 11로 나눈 나머지를 11에서 뺍니다.
# 계산 결과값이 주민등록번호 마지막 자리 숫자와 일치하면 유효한 주민등록번호
# 1 2 3 4 5 6 - 1 2 3 4 5 6 7
# * * * * * * * * * * * * *
# 2 3 4 5 6 7   8 9 2 3 4 5
# 2+6+12+20+30+42+8+18+6+12+20+30
# 11 - (206 % 11) = 3 != 7
# 유효하지 않음
# 주민번호 유효성 체크(checkJumin/readJumin/printJumin)
sum = 0
jummin = input('주민번호를 입력하세요. ')
result = '주민번호가 유효하지 않습니다.'
sum += int(jummin[0]) * 2
sum += int(jummin[1]) * 3
sum += int(jummin[2]) * 4
sum += int(jummin[3]) * 5
sum += int(jummin[4]) * 6
sum += int(jummin[5]) * 7
sum += int(jummin[6]) * 8
sum += int(jummin[7]) * 9
sum += int(jummin[8]) * 2
sum += int(jummin[9]) * 3
sum += int(jummin[10]) * 4
sum += int(jummin[11]) * 5
checker = (11 - (sum % 11)) % 10
if checker == int(jummin[12]):
    result = '유효한 주민번호입니다.'
print(result)

import ytafxt.example as ju
ju.checkJumin('1234561234567')
