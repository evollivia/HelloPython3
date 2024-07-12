# 26
isMarried = int(input('결혼여부 0:미혼, 1:기혼'))
salary = int(input('연봉 : '))
tax = 0
if isMarried == 0:
    tax = salary * 0.1
    if salary >= 3000:
        tax = salary * 0.25
elif isMarried == 1:
    tax = salary * 0.15
    if salary >= 6000:
        tax = salary * 0.35

print(f'''
결혼여부 : {isMarried}
연봉 : {salary}
세금 : {tax:,}''')

# 27
# 1992, 2000, 2020 (윤O)
# 1900, 2100 (윤X)
year = int(input('연도 : '))
con1 = year % 4 == 0 and year % 100 != 0
con2 = year % 400 == 0
isLeap = '윤년아님'
if con1 or con2:
    isLeap = '윤년맞음'
print(f'{year}년은 {isLeap}')

# 28
# GuGuDan = int(input('원하는 단수를 입력하시오 : '))
GuGuDan = input('원하는 단수를 입력하시오 : ')
result = '잘못 입력하셨습니다'
# if GuGuDan > 0 and GuGuDan <= 9:
if (GuGuDan.isdigit()) and (0 < int(GuGuDan) <= 9):
    result = f'{GuGuDan} X 1 = {GuGuDan * 1}\n'
    result += f'{GuGuDan} X 2 = {GuGuDan * 2}\n'
    result += f'{GuGuDan} X 3 = {GuGuDan * 3}\n'
    result += f'{GuGuDan} X 4 = {GuGuDan * 4}\n'
    result += f'{GuGuDan} X 5 = {GuGuDan * 5}\n'
    result += f'{GuGuDan} X 6 = {GuGuDan * 6}\n'
    result += f'{GuGuDan} X 7 = {GuGuDan * 7}\n'
    result += f'{GuGuDan} X 8 = {GuGuDan * 8}\n'
    result += f'{GuGuDan} X 9 = {GuGuDan * 9}'
print(result)

# 33
cardno = int(input('카드번호 : '))
result = '잘못된 카드번호입니다'
if cardno == 356317: result = 'JCB카드 NH농협카드'
elif cardno == 356901: result = 'JCB카드 신한카드'
elif cardno == 356912: result = 'JCB카드 KB국민카드'
elif cardno == 404825: result = '비자카드 비씨카드'
elif cardno == 438676: result = '비자카드 신한카드'
elif cardno == 457973: result = '비자카드 국민은행'
elif cardno == 515594: result = '마스터카드 신한카드'
elif cardno == 524353: result = '마스터카드 외환카드'
elif cardno == 5540926: result = '마스터카드 국민은행'
print(f'{cardno} / {result}')

# 35
daytime = input('시간대 :')
result = '잘못 입력하셨습니다.'
if daytime == 'morning hour': result = '아침시간 (7-12)'
elif daytime == 'midday' or daytime == 'noon': result = '점심시간 (12-1 )'
elif daytime == 'midday' or daytime == 'noon': result = '점심시간'