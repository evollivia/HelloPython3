# 파일 읽기
# with open(경로, 방식, 'r') as 파일객체변수
#   파일객체변수.read()

# 파일 기록방식
# r(읽기)

# 파일 읽을때 사용 가능한 함수
# read      : 파일의 내용을 모두 읽음
# readline  : 파일의 내용을 한 줄씩 읽음(반복문 필요)
# readlines : 파일의 내용을 한 줄씩 모두 읽음

# 파일에서 간단한 인삿말 읽어오기
with open('c:/java/hello.txt') as f:
    print(f.read())

# 파일에서 회원정보 읽어오기1 - 단순출력
with open('c:/java/member.dat') as f:
    print(f.read())

# 파일에서 회원정보 읽어오기2 - 행단위 처리1
with open('c:/java/member.dat') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

# 파일에서 회원정보 읽어오기3 - 행단위 처리2
with open('c:/java/member.dat') as f:
    while True:
        line = f.readline()     # 먼저 한줄 읽고
        if not line: break      # 읽은 내용이 없으면 중단
        print(line)

# 파일에서 회원정보 읽어오기4 - 행단위 처리3
with open('c:/java/member.dat') as f:
    lines = f.readlines()       # 행 단위로 읽어서 리스트에 저장

for line in lines:      # 이터러블 형식으로 반복 처리
    print(line)

# 회원정보 데이터파일에서 이름과 이메일만 출력
with open('c:/java/member.dat', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

# 문자열변수.split(구분자) : 특정 문자로 문자열을 나눠 리스트에 저장
for line in lines:
    member = line.split('/')
    print(member[2], member[3], end='')

# 앞 예제에서 파일로 저장한 성적데이터를
# 다음과 같은 형태로 화면에 출력
# 이름:abc, 국어:99, 영어:87, 수학:66
with open('c:/java/sungjuk.dat', encoding='UTF-8') as f:
    lines = f.readlines()

for line in lines:
    s = line.split(',')
    row = f'이름:{s[0]}, 국어:{s[1]}, 영어:{s[2]}, 수학:{s[3]}'
    print(row, end='')
