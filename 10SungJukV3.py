# 성적처리 프로그램 v3
# 이름, 국어, 영어, 수학을 입력받으면
# 총점, 평균, 학점을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해서 성적 처리를 진행함
# 학점 : 수우미양가

# 이름 : 민지, 국어 : 99, 영어 : 98, 수학 : 99
# 총점 : 296, 평군 : 98.7, 학점 : 수

# 이름 : 혜린, 국어 : 88, 영어 : 77, 수학 : 66
# 총점 : 231, 평군 : 77.0, 학점 : 미

# 이름 : 다니엘, 국어 : 55, 영어 : 77, 수학 : 99
# 총점 : 231, 평군 : 77.0, 학점 : 미

# 성적 데이터 관련변수
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []

# 성적 데이터 입력받음
for i in range(1, 4):
    names.append(input(f'{i}번학생 이름 : '))
    kors.append(int(input(f'{i}번학생 국어 성적 : ')))
    engs.append(int(input(f'{i}번학생 영어 성적 : ')))
    mats.append(int(input(f'{i}번학생 수학 성적 : ')))

# 성적 처리
# 100~90 수, 89~ 80 우, 79~ 70 미, 69~ 60 양, 59~ 0 가
for i in range(3):
    tot = kors[i] + engs[i] + mats[i]
    tots.append(tot)
    avg = tot[i] / 3
    avgs.append(avg)
    grd = '수' if avg >= 90 else ('우' if avg >= 80 else ('미' if avg >= 70 else ('양' if avg >= 60 else '가')))
    grds.append(grd)

# 결과 출력
result = ''
for i in range(3):
    result += f'''
    이름 : {names[i]}, 국어 : {kors[i]}, 영어 : {engs[i]} ,수학 : {mats[i]}
    총점 : {tots[i]}, 평군 : {avgs[i]:.1f}, 학점 : {grds[i]}\n
    '''
print(result)
