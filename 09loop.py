# 반복문
# 특정 문장/코드를 지정한 횟수/조건에 반복 실행하는 문장

# 간단한 메세지 한번 출력
print('Hello Python!')

# 간단한 메세지 여번 출력
print('Hello Python!')
print('Hello Python!')
print('Hello Python!')

# 메세지를 수정한다면? - 번거로움
print('Hello Cloud!')
print('Hello Cloud!')
print('Hello Cloud!')

# 만약, 반복문을 사용한다면?
# 반복의 용이성과 수정의 편리함을 제공

# 파이썬의 반복문
# for   : 지정한 횟수만큼 반복 수행
# while : 지정한 조건에 의해 반복 수행

# 횟수에 따른 반복 - for
# 반복 회수는 range() 함수로 유추 가능 : 종료값-1 - 시작값
# for 카운트변수 in range(시작값, 종료값-1, 간격):
#     반복할 문장

# range 함수
# 시작값과 종료값-1 사이의 연속된 정수 반환
print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(list(range(1, 10 + 1)))
print(list(range(1, 10 + 1, 2)))

# for 사용예
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
for i in range(1, 10 + 1):
    print(i)

for i in range(1, 3 + 1):  # st ~ end-1
    print(f'Hello World! {i}')

for i in range(3):  # 0 ~ end-1
    print(f'Hello World! {i}')

for _ in range(3):  # 카운트 변수 생략
    print(f'Hello World!')

# 1 ~ 100 사이 모든 정수의 합을 구하고 출력
a = 0
for i in range(1, 101):
    a += i
print(f'1 ~ 100 사이 모든 정수의 합 : {a}')

# 1 ~ 100 사이 모든 짝수의 합을 구하고 출력
b = 0
# for i in range(2, 101 ,2):
for i in range(1, 101):
    if i % 2 == 0:
        b += i
print(f'1 ~ 100 사이 모든 짝수의 합 : {b}')

# 메일 발송
count = int(input('메일발송 횟수를 입력하세요 : '))
for _ in range(count):
    print('메일발송')

# 3의 배수 출력하기
result = ''
for i in range(1, 11):
    result += f'num = {i}\n'
    if i % 3 == 0:
        result += '3의 배수!\n'
print(result)

# 구구단 5단 출력
dan = 5
result = ''
for i in range(1, 10):
    result += f'{dan} * {i} = {dan * i}\n'
print(result)

# 줄바꿈 없이 출력하기 (end='')
result = ''
for i in range(1, 11):
    # print(i, end=' ')
    result += f'{i} '
print(result)

# 1 ~ 100까지 정수중 3과 7의 공배수와 최소공배수를 출력
result = ''
for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0:
        result += f'{i} '
print(result, f',{3 * 7}')

# range함수 사용 예
print(list(range(-10, 0, 1)))
print(list(range(10, 0, -1)))

# 문자열에 for문
str = 'Hello, World!!'
for c in str:
    print(c, end='')

# 실전 예제1 - 369게임
# 방법1
for i in range(1, 100):
    num = str(i)
    count = num.count('3') + num.count('6') + num.count('9')
    if count > 0:
        print(i, '짝!' * count)
    else:
        print(i)

# 방법2
# 1 ~ 10 : 3, 6, 9
# 11 ~ 20 : 13, 16, 19
# ...
# 41 ~ 50 : 43, 46, 49
for i in range(1, 100):
    if i < 10:
        if i % 3 == 0:
            print(f'{i} 짝!')
        else:
            print(i)
    else:
        clap = ''
        fnum = i // 10
        lnum = i % 10
        if fnum % 3 == 0:
            clap += '짝!'
        if lnum % 3 == 0 and lnum != 0:
            clap += '짝!'
        print(f'{i} {clap}')

# 실전 예제2 - 열차 교차로 시간 알아내기
# 오전 9시 ~ 오후 6시 : 540분
# A, B 교차 : 50분 간격
# A, C 교차 : 30분 간격
# A,B,C 교차 : 150분 간격
trainA = 10
trainB = 25
trainC = 30
for min in range(1, 540+1):
    hour = 9 + min // 60
    minute = min % 60
    if min % trainA == 0 and min % trainB == 0:
        print(f'{hour}시 {minute}분 A-B 교차')
    elif min % trainB == 0 and min % trainC == 0:
        print(f'{hour}시 {minute}분 B-C 교차')
    elif min % trainC == 0 and min % trainA == 0:
        print(f'{hour}시 {minute}분 C-A 교차')

# 실전 예제3 - 로그인 기능 만들기
passwd = 'hanbitac'
for i in range(5):
    login = input('관리자 암호를 입력하세요 : ')
    if login == passwd:
        print('로그인 됐습니다.')
        break
    if login != passwd:
        i += 1
        if i >= 5:
            print('로그인 실패!! 횟수 초과!!')

isLogin = False
for i in range(5):
    if not isLogin:
        passwd = input('관리자 암호를 입력하세요 : ')
        if passwd == 'hanbitac':
            isLogin = True
            print('로그인 됐습니다.')
        else:
            print('암호를 다시 입력하세요.')
if not isLogin:
    print('로그인 실패!! 횟수 초과!!')

