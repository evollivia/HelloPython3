# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장, 조회, 삭제하기위해 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리
# 대량의 데이터를 처리할 때 속도를 높이고, 메모리를 절약할 수 있음

# 리스트
# 다른 프로그래밍 언어에서는 배열(array)과 유사 동일한 유형의 데이터를 1차원 형태로 순차적으로 저장하는 자료구조
# 선언방법은 []에 값들을 하나씩 정의
# 리스트의 각 요소를 참조하려면 변수명 [위치값] 형식을 사용

# 과일 데이터 저장
fruits = ['사과', '포도', '수박', '참외', '복숭아']
print(fruits)

# 점심 메뉴를 리스트로 선언
menus = ['라면', '돈까스', '냉면', '햄버거', '정식']
print(menus)

# 리스트에서 요소(elements, item)별로 출력
# 첫번째 요소의 위치값(index)은 0부터 시작
print(menus[0], menus[1], menus[4])
print(menus[5])  # index 범위 벗어남 - 오류발생!

# 동적으로 리스트 추가하기
menus = []

# 리스트에 요소를 추가하려면 append(값) 함수 사용
# 추가된 요소는 리스트의 맨 뒤에 부착 - LIFO
menus.append('라면')
menus.append('돈까스')
menus.append('우동')
menus.append('햄버거')
menus.append('정식')
print(menus)

# 리스트에는 다른 유형의 데이터도 저장 가능 (비추)
complex = [1, 10.1, 'a', 'abc123', True]
print(complex)

# 리스트 요소 수정 : 변수명[위치] = 새로운값
menus[2] = '탕수육'
print(menus)

# 리스트 요소 삭제 : remove(값) - 값으로 삭제
menus.remove('탕수육')
print(menus)

# 리스트 요소 삭제 : pop(위치) - 위치으로 삭제
menus.pop(1)
print(menus)

# len() 함수 - 리스트 요소의 갯수 또는 문자열 길이 출력
print(len(menus))
print(len('Hello, Worled!'))

# 입력받은 글자 수 확인
msg = input('메세지를 입력하세요 : ')
print(f'입력받은 메세지 길이 : {len(msg)}')

# 이터러블
balls = ['야구공', '축구공', '농구공', '탁구공', '골프공']
for b in balls:
    print('ball :', b)

for idx, b in enumerate(balls):
    print('indx : ', idx, 'ball :', b)

i = 0
while i < len(balls):
    print(balls[i])
    i += 1

# 인덱스 조회
num = [1, 2, 3, 4, 5]
print(num.index(1))
print(num.index(5))

str = 'python'
print(str.index('th'))

# 삽입
num = [1, 2, 3, 4, 5]
num.insert(2,10)
print(num)

# 리스트 연결
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)

# 합격 여부 판정하기
exam = [55, 35, 40, 70, 65, 30]

## 과락여부
cntFail = 0
for i in range(6):
    if exam[i] < 40:
        cntFail += 1
## 평균
sum = 0
for i in range(6):
    sum += exam[i]
avg = sum / 6

## 합격 여부
result = '아쉽습니다. 불합격하셨습니다.'
if cntFail == 0 and avg >= 60:
    result = '축하드립니다. 합격하셨습니다'

## 평가
print(f'''
40점 미만 과목수 : {cntFail}
평균점수 : {avg}
결과 : {result}''')

# 실습 예제2 - 혈액 보관 시스템
bloods = []
cntBlood = [0, 0, 0, 0]
msg = '''헌혈해 주셔서 감사합니다. 혈액형을 선택하세요
A, B, AB, O : '''

for i in range(10):
    bloods.append(input(msg))

for i in range(10):
    if bloods[i] == 'A':
        cntBlood[0] += 1
    elif bloods[i] == 'B':
        cntBlood[1] += 1
    elif bloods[i] == 'AB':
        cntBlood[2] += 1
    elif bloods[i] == 'O':
        cntBlood[3] += 1

line = '-' * 20
# result = f'''
# {line}
# 혈액형 : 개수
# {line}
# A형 : {cntBlood[0]}
# B형 : {cntBlood[1]}
# AB형 : {cntBlood[2]}
# O형 : {cntBlood[3]}
# {line}
# '''

result = f'''
{line}
혈액형 : 개수
{line}
A형 : {bloods.count('A')}
B형 : {bloods.count('B')}
AB형 : {bloods.count('AB')}
O형 : {bloods.count('O')}
{line}
'''
print(result)
