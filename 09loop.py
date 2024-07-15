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