# 성적처리 프로그램 v
# 이름, 국어, 영어, 수학을 입력받으면
# 총점, 평균, 학점을 계산하고 출력함
# 단, 학생 3명에 대해서 성적 처리를 진행함
# 학점 : 수우미양가

# 이름 : 민지, 국어 : 99, 영어 : 98, 수학 : 99
# 총점 : 296, 평군 : 98.7, 학점 : 수

# 이름 : 혜린, 국어 : 88, 영어 : 77, 수학 : 66
# 총점 : 231, 평군 : 77.0, 학점 : 미

# 이름 : 다니엘, 국어 : 55, 영어 : 77, 수학 : 99
# 총점 : 231, 평군 : 77.0, 학점 : 미

# 성적 데이터 입력받은
name1 = input('1번학생 이름 : ')
korean1 = int(input('1번학생 국어 성적 : '))
english1 = int(input('1번학생 성적 : '))
math1 = int(input('1번학생 수학 성적 : '))

name2 = input('2번학생 이름 : ')
korean2 = int(input('2번학생 국어 성적 : '))
english2 = int(input('2번학생 성적 : '))
math2 = int(input('2번학생 수학 성적 : '))

name3 = input('3번학생 이름 : ')
korean3 = int(input('3번학생 국어 성적 : '))
english3 = int(input('3번학생 성적 : '))
math3 = int(input('3번학생 수학 성적 : '))

# 성적 처리
# 100~90 수, 89~ 80 우, 79~ 70 미, 69~ 60 양, 59~ 0 가
total1 = korean1 + english1 + math1
average1 = (korean1 + english1 + math1) / 3
agrades1 = '수' if average1 >= 90 else ('우' if average1 >= 80 else ('미' if average1 >= 70 else ('양' if average1 >= 60 else '가')))

total2 = korean2 + english2 + math2
average2 = (korean2 + english2 + math2) / 3
agrades2 = '수' if average2 >= 90 else ('우' if average2 >= 80 else ('미' if average2 >= 70 else ('양' if average2 >= 60 else '가')))

total3 = korean3 + english3 + math3
average3 = (korean3 + english3 + math3) / 3
agrades3 = '수' if average3 >= 90 else ('우' if average3 >= 80 else ('미' if average3 >= 70 else ('양' if average3 >= 60 else '가')))

# 결과 출력
print(f'''
이름 : {name1}, 국어 : {korean1}, 영어 : {english1} ,수학 : {math1}
총점 : {total1}, 평군 : {average1:.1f}, 학점 : {agrades1}
-----------------------------------------------------------------
이름 : {name2}, 국어 : {korean2}, 영어 : {english2} ,수학 : {math2}
총점 : {total2}, 평군 : {average2:.1f}, 학점 : {agrades2}
-----------------------------------------------------------------
이름 : {name3}, 국어 : {korean3}, 영어 : {english3} ,수학 : {math3}
총점 : {total3}, 평군 : {average3:.1f}, 학점 : {agrades3}
''')

