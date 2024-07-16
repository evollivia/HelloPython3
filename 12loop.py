# while문
# 조건을 만족 할 때까지 반복 수행 - 반복횟수는 모름

# 변수 = 초기값
# while 조건식:
#   반복할 문장
#   변수증가/감소

# 1 ~ 10 까지 정수 출력
# for 문
for i in range(1, 10 + 1):
    print(i, end='')

# while 문
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1

# 1 ~ 50 사이의 정수중 홀수만 출력
i = 1
while i <= 50:
    if i % 2 == 1:
        print(i, end=' ')
    i += 1

while i <= 50:
    print(i, end=' ')
    i += 2

# 1 ~ 50 사이의 정수중 9의 배수만 출력
i = 1
while i <= 50:
    if i % 9 == 0:
        print(i, end=' ')
    i += 1

# 반복문 내 실행중지 : break
#  for, while문 내에서 반복흐름을 벗어나기 위해 사용
# 1 ~ 10000 사이 정수의 합을 출력
# 단, 정수의 합이 12345678보다 크면 계산을 중지
# for 문
plus = 0
for i in range(1, 10000 + 1):
    if plus > 12345678:
        break
    plus += i
print(plus)

# while 문
i = 1
plus = 0
while i < 10000 + 1:
    if plus > 12345678:
        break
    plus += i
    i += 1
print(plus)

# 구구단 3단 출력하기
dan = 3
result = ''
i = 1
while i < 10:
    result = f'{dan} x {i} = {dan * i}'
    print(result)
    i += 1

# 0 ~ 100까지 정수 중 3과 8의 공배수와 최소공배수 출력
result = ''
mul = 1
minmul = 3 * 8
i = 1
print(f'최소 공배수 : {minmul}')
while True:
    mul = i * minmul
    if mul >= 100:
        break
    result = f'공배수 : {mul}'
    print(result)
    i += 1

# 삼각형 넓이 구하기
limitArea = 150     # 반복 중단 삼각형 넓이
i = 1
while True:
    area = (i * 2) * (i * 3) / 2
    if area > limitArea:
        break
    print(f'삼각형의 넓이 : {i * 2}/{i * 3} = {area}')
    i += 1


# 실전 예제1 - 369게임(while문)
# 값 in str(문자열)
# '3' in str(36)
# '6' in str(36)
# '9' in str(12)
i = 1
while i < 100:
    jjak = ''
    if '3' in str(i):
        jjak += ' 짝!'
    if '6' in str(i):
        jjak += ' 짝!'
    if '9' in str(i):
        jjak += ' 짝!'
    if i == 33 or i == 66 or i == 99:
        jjak += '짝!'
    print(i, jjak)
    i += 1

# 실전 예제2 - 열차 교차로 시간 알아내기(while문)
# 오전 9시 ~ 오후 6시 : 540분
# A, B 교차 : 50분 간격
# A, C 교차 : 30분 간격
# A,B,C 교차 : 150분 간격
trainA = 10
trainB = 25
trainC = 30
min = 1
while min <= 540:
    hour = 9 + min // 60
    minute = min % 60
    if min % trainA == 0 and min % trainB == 0:
        print(f'{hour}시 {minute}분 A-B 교차')
    elif min % trainB == 0 and min % trainC == 0:
        print(f'{hour}시 {minute}분 B-C 교차')
    elif min % trainC == 0 and min % trainA == 0:
        print(f'{hour}시 {minute}분 C-A 교차')
    min += 1

# 실전 예제3 - 로그인 기능 만들기(while문)
passwd = 'hanbitac'
i = 1
while i <= 5:
    login = input('관리자 암호를 입력하세요 : ')
    if login == passwd:
        print('로그인 됐습니다.')
        break
    else:
        i += 1
        if i > 5:
            print('로그인 실패!! 횟수 초과!!')
            break
