# 조건문
# 주어진 상황에 따라 적절한 명령문을 수행하는 문장
# 프로그래밍에서 조건을 판단하여
# 해당 조건에 맞는 상황을 수행하는데 사용됨
# 파이썬에서 조건문 작성시 반드시 들여쓰기를 사용함을 명심

# 파이썬의 코드 블록
# 특정 동작을 위해 관련된 코드를 한곳에 모아둔 것
# 이러한 코드들은 반드시 같은 들여쓰기 내에 존재해야 함

# if 문
# if 조건식 :
# 조건이 참일때 수행할 문장(들)

# 짝수 판별하기
num = int(input('숫자 : '))
if num % 2 == 0:
    print(f'짝수입니다')

if num % 2 == 0: print(f'짝수입니다')  # 코드 간략화

# 속도위반 경고하기
speed = int(input('자동차의 현재 속도는 : '))
warn = ''
if speed > 50:
    warn = '속도 위반!!'
print(warn)

# if ~ else
# if문은 조건이 참일 경우에만 지정한 코드를 실행하는데 비해
# if ~ else문은 조건이 참일 때와 거짓일 때 각각 지정한 코드를
# 실행한 다는 것이 다름
# if 조건식 :
#     수행할문장1
# else:
#     수행할문장2

# 짝수/홀수 판별하기
num = int(input('숫자 : '))
if num % 2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다')

# pass
# 조건문/반복문/함수/클래스나 다른 문 등에서
# 실행문이 정해지지 않은 경우 임시로 작성하는 명령문

if num % 2 ==0:
    pass
else:
    pass

# 마일리지 사용하기
# 방법1
mileage = 1200
if mileage >= 1000:
    print('마일리지 사용가능')
else:
    print('마일리지 사용불가')

# 방법2
mileage = 1200
result = ''
if mileage >= 1000:
    result = '마일리지 사용가능'
else:
    result = '마일리지 사용불가'
print(result)

# 방법3
mileage = 1200
result = '마일리지 사용불가'
if mileage >= 1000:
    result = '마일리지 사용가능'
print(result)

# 자동 온도 조절 장치 만들기
temp = float(input('기계 온도를 입력하세요. '))
out = '팬(Fan) 중지'
if temp >= 40:
    out = '팬(Fan) 가동'
print(out)

# 중첩 if문
# if문 속에 또 다른 if문을 포함시켜 작성하는 조건문
# 조건문을 중첩할 때는 들여쓰기에 유의해야함
# 다양한 조건에 따라 결과를 처리하고 싶을때 사용 - 복잡함

# 평균 점수에 따라서 ABCDF학점을 처리하는 조건문
avg = 73.5
grade = 'F'
if avg >= 90:
    grade = 'A'
else:
    if avg >= 80:
        grade = 'B'
    else:
        if avg >= 70:
            grade = 'C'
        else:
            if avg >= 60:
                grade = 'D'

print(grade)

# 다중 if문
# 중첩 if문을 작성하는 경우, 조건이 많으면 다소 복잡함
# 이러한 중첩 if문을 단순하게 작성할 수 있는 조건문
# if 조건1:
#    실행할 코드1
# elif 조건2:
#    실행할 코드2
# elif 조건3:
#    실행할 코드3
# else:
#    실행할 코드4

avg = 85.5
grade = 'F'
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
print(grade)

# 자동 주문 시스템 만들기
menuIntro = int(input('Good morning. Nice to meet you.\n'
                      'Where are you from?\n'
                      'Please select a number\n'
                      '1.대한민국 2.UAS 3.中國'))
msg = 'Would you like to order?'
if menuIntro == 1:
    msg = '주문하시겠어요?'
elif menuIntro == 3:
    msg = '您想訂購嗎？'
else:
    msg
print(msg)

# 국가 재난지원금 수령액 조회하기
people = int(input('인원수를 입력하세요. '))
money = '1,000,000원 지원'
if people == 1:
    money = '400,000원 지원'
elif people == 2:
    money = '600,000원 지원'
elif people == 3:
    money = '800,000원 지원'
print(money)

# 개선 BMI지수 출력
bmi = int(input('BMI지수를 입력하세요. '))
status = '저체중'
if bmi > 140: status = '고도비만'
elif bmi > 120: status = '비만'
elif bmi > 110: status = '과체중'
elif bmi > 90: status = '정상 체중'
print(f'BMI지수 : {bmi}\n'
      f'진단결과 : {status} 입니다.')


# if 조건문 대체 1 - switch 모방
# 조건이 많아지는 경우, 다중 조건문 역시 복잡해짐
# 이럴 경우, dict 자료 구조를 이용하면 간단하게 작성 가능

# if 조건문 대체 2
# py 3.10부터 switch와 비슷한 match ~ case 문 도입
# match 값:
#   case 값범위1: 실행문1
#   case 값범위2: 실행문2
#   default: 실행문3

# 주민번호 성별 코드에 따른 성별 출력
# 1 : 남자(2000년 이전 출생)
# 2 : 여자(2000년 이전 출생)
# 3 : 남자(2000년 이후 출생)
# 4 : 여자(2000년 이후 출생)

code = int(input('성별코드 : '))
result = ''
match code:
    case 1: result = '남자(2000년 이전 출생)'
    case 2: result = '여자(2000년 이전 출생)'
    case 3: result = '남자(2000년 이후 출생)'
    case 4: result = '여자(2000년 이후 출생)'
    case _: result = '외국인이군요!'

print(result)

# 다중 if문으로 작성한 학점계산 코드를
# match case로 바꿔 작성해보시오
avg = 85.5
grade = ''

match int(avg/10):
    case 10 | 9: grade = 'A'
    case 8: grade = 'B'
    case 7: grade = 'C'
    case 6: grade = 'D'
    case _: grade = 'F'
print(grade)

match avg:
    case avg if avg >= 90: grade = 'A'
    case avg if avg >= 80: grade = 'B'
    case avg if avg >= 70: grade = 'C'
    case avg if avg >= 60: grade = 'D'
    case _: grade = 'F'
print(grade)


# 버스 전용차로 단속
msg1 = '''1.월~금, 2.토요일, 3.공휴일'
요일을 선택하세요.'''
msg2 = '''
버스 전용차로 단속중 입니다.
1.버스, 2.승용차
차종을 선택하세요.'''
msg3 = '버스 전용차로 위반!'
msg4 = '버스입니다.'
msg5 = '토요일 및 공휴일은 단속하지 않습니다.'

dayweek = int(input(msg1))
result = ''
carType = ''
if dayweek == 1:                # 평일여부 확인
    carType = int(input(msg2))  # 차종 확인
    if carType == 1:
        result = msg4
    else:
        result = msg3
else:
    result = msg5
print(result)

# 마스크 구매가능 요일
endBirthYear = int(input('출생 연도 끝자리 입력 : '))
age = int(input('만 나이 입력 : '))
day = '언제든 구매 가능합니다.'
if age < 65:
    # if endBirthYear == 1 or endBirthYear == 6:
    #     day = '월요일 구매 가능합니다.'
    # elif endBirthYear ==2 or endBirthYear == 7:
    #     day = '화요일 구매 가능합니다.'
    # elif endBirthYear ==3 or endBirthYear == 8:
    #     day = '수요일 구매 가능합니다.'
    # elif endBirthYear ==4 or endBirthYear == 9:
    #     day = '목요일 구매 가능합니다.'
    # elif endBirthYear ==5 or endBirthYear == 0:
    #     day = '금요일 구매 가능합니다.'
    match endBirthYear:
        case 1 | 6:
            day = '월요일 구매 가능합니다.'
        case 2 | 7:
            day = '화요일 구매 가능합니다.'
        case 3 | 8:
            day = '수요일 구매 가능합니다.'
        case 4 | 9:
            day = '목요일 구매 가능합니다.'
        case 5 | 0:
            day = '금요일 구매 가능합니다.'
print(day)


# 차량 2부제
from datetime import datetime
num = int(input('차량 번호 4자리를 입력하세요.'))
day = int(datetime.today().day)  # 오늘 날짜의 일만 추출
msg1 = '오늘 입차 : 번호가 홀수인 차량'
msg2 = '귀하의 차량은 입차 불가능합니다.'
if day % 2 == 0:
    msg1 = '오늘 입차 : 번호가 짝수인 차량'
if day % 2 == num % 2:
    msg2 = '귀하의 차량은 입차 가능합니다.'
print(f'''
오늘 날짜 : {day}
{msg1}
{msg2}''')


# 생존율 출력
msg = '최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요. '
sec = int(input(msg))
rate = '생존율 : 25% 미만'
if sec <= 60: rate = '생존율 : 85%'
elif sec <= 120: rate = '생존율 : 76%'
elif sec <= 180: rate = '생존율 : 66%'
elif sec <= 240: rate = '생존율 : 57%'
elif sec <= 300: rate = '생존율 : 47%'
elif sec <= 300: rate = '생존율 : 35%'
elif sec <= 360: rate = '생존율 : 25% 미만'
print(rate)

# 전기요금 계산기
elc = int(input('전기 사용량을 입력하세요. '))
baseprice = 910
unitprice = 99.3
powerprice = 0

if elc > 400:
    baseprice = 7300
    unitprice = 280.6

elif elc > 200:
    baseprice = 1600
    unitprice = 187.9

powerprice = baseprice + (unitprice * elc)
print(f'''
사용량 : {elc} kwh
기본요금 : {baseprice:,} 원
단가 : {unitprice:,} 원
전기요금 : {powerprice:,}원''')