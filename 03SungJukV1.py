# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 입력받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가

# 이름 : 홍길동, 국어 : 99, 영어 : 98, 수학 : 99
# 총점 : 296, 평군 : 98.6 학점 : 수

# 성적 데이터 입력받은
name = input('이름 : ')
korean = int(input('국어 성적 : '))
english = int(input('영어 성적 : '))
math = int(input('수학 성적'))

# 성적 처리
# 100~90 수, 89~ 80 우, 79~ 70 미, 69~ 60 양, 59~ 0 가
total = korean + english + math
average = (korean + english + math) / 3
agrades = '수' if average >= 90 else ('우' if average >= 80 else ('미' if average >= 70 else ('양' if average >= 60 else '가')))

# 결과 출력
print(f'''
이름 : {name}
국어 : {korean}
영어 : {english}
수학 : {math}
-------------------
총점 : {total}
평군 : {average:.1f} 
-------------------
학점 : {agrades}
''')

