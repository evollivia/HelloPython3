# 모듈
# 특정 ㄷ기능을 수행하는 코드들의 모음
# 코드 재사용 : 한번 작성한 코드를 여러번 사용 가능
# 코드 관리 : 큰 프로젝트를 작은 모듈로 나눠 관리 가능
# 협업 : 여러 개발자가 각각 모듈을 개발하고 함께 사용

# 표준 모듈 : 파이썬에서 기본적으로 제공하는 모듈 - 바로 사용 가능
# 외부 모듈 : 다른 조직, 개발자가 만든 모듈 - 별도 설치 필요
# 사용자 정의 모듈 : 직접 만든 모듈

# 모듈 사용 방법
# import 모듈명
# import 모듈명 as 별칭
# from 모듈명 import 함수명 as 별칭

# 난수 생성
import random
import random as rnd
from random import randint

# 1 ~ 10사이 임의의 난수 생성
print(random.randint(1, 10))
print(rnd.randint(1, 10))
print(randint(1, 10))
print(rnd.randint(1, 45))   # 1 ~ 45

# 특정 범위의 숫자들 중에서 하나 추출(표본 추출)
# range(n, m) :n ~ m-1 사이의 정수들
import random as rnd
print(rnd.sample(range(1, 46), 6))

# 날짜 시간 처리
import datetime as dt
print(dt.datetime.now())
print(dt.date.today())
print(dt.datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분 %S초'))

# operator 모듈

# 긴급 재난지원금 대상자 판별하기
import operator as op
tgsalary = 4000000
salary = int(input('월 소득을 입력하세요. '))
helpm = input('다른 지원금을 받고 있습니까? 1번 받고 있다. 2번 받고 있지 않다. ')
#result = '수급 대상자' if (salary <= 4000000 and helpm == '2') else '수급 대상자가 아님'
result = '수급 대상자' if op.and_(op.le(salary, tgsalary), op.eq(helpm, '2')) else '수급 대상자가 아님'
print(result)

# 수온 계산기
import operator as op
basetemp = 20

depth = float(input('수심을 입력하세요 '))
temp = op.sub(basetemp, op.mul(op.floordiv(depth, 10), 0.7))
print(f'수심 : {depth} m\n수온 : {temp} ℃')

# 자동차 주행거리 계산
import operator as op
speed = int(input('주행 속도 : '))
time = int(input('주행 시간 : '))
distance = op.mul(speed, time)
print(f'주행 이동 거리 : {distance} km')

# 컴퓨터 업무수량 파악
import math
import operator as op
time = int(input('근무시간을 입력하세요 : '))
com = math.ceil(op.truediv(op.mul(1,24),time))
print(com)

worktime = int(input('근무시간을 입력하세요 : '))
# comp = 3*8//worktime
# etcComp = 1 if (3*8%worktime) > 0 else 0
expr1 = op.mul(3,8)
comp = op.floordiv(expr1,worktime)
etcComp = 1 if (op.mod(expr1, worktime)) > 0 else 0
print(f'필요한 컴퓨터 : {comp+etcComp} 대')
