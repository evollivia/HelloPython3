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
sum = 0
for i in range(1, 10000+1):
    if sum > 12345678:
        break
    sum += i
print(sum)

# while 문
i =1
sum = 0
while i < 10000 + 1:
    if sum > 12345678:
        break
    sum += i
    i += 1
print(sum)

# 구구단 3단 출력하기
# 0 ~ 100까지 정수 중 3과 8의 공배수와 최소공배수 출력
# 삼각형 넓이 구하기

# 실전 예제1 - 369게임(while문)
# 값 in str(문자열)
# '3' in str(36)
# '6' in str(36)
# '9' in str(12)
i = 1
while i < 100:
    jjak = ''
    if '3' in str(i): jjak += ' 짝!'
    if '6' in str(i): jjak += ' 짝!'
    if '9' in str(i): jjak += ' 짝!'
    if i == 33 or i == 66 or i == 99: jjak += '짝!'
    print(i, jjak)
    i += 1

# 실전 예제2 - 열차 교차로 시간 알아내기(while문)

# 실전 예제3 - 로그인 기능 만들기(while문)
