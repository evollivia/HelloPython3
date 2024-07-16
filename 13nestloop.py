# 중첩 반복문
# 2개 이상의 반복문을 이용해서 반복실행 할 수도 있음
# 하나의 반복문 안에 다른 반복문을 포함시킨 것을 의미
# 이 것을 통해 좀 더 복잡힌 반복 패턴을 구현할 수 있음
# 2차원 배열처리나 달력 출력, 복잡한 패턴 생성시 주로 이용

# *
# **
# ***
# ****
# *****
# 5 x 5 반복출력
for i in range(5):         # 행
    for j in range(5):     # 열
        print('*', end='')
    print()                     # 줄바꿈

# 각 반복마다 1, 2, 3, 4, 5회 출력
for i in range(1, 5+1):    # 행
    for j in range(i):     # 열
        print('*', end='')
    print()                # 줄바꿈

# *****
# ****
# ***
# **
# *
for i in range(5, 0, -1):    # 행
    for j in range(i):       # 열
        print('*', end='')
    print()                  # 줄바꿈

# 구구단 전체 출력
for i in range(1, 10):      # 행/큰바늘
    for j in range(1,10):   # 열/작은바늘
        print(f'{j} x {i} = {i * j:2d}', end='   ')
    print()

# 19단 전체 출력
for i in range(1, 20):      # 행/큰바늘
    for j in range(1,20):   # 열/작은바늘
        print(f'{j:2d} x {i:2d} = {i * j:3d}', end='   ')
    print()
