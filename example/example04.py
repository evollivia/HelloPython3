# 51. 구구단
print(f'''
             Multiplication Table
        1    2    3    4    5    6    7    8    9
-------------------------------------------------''')

for i in range(1, 10):
    print(f'{i} |', end='  ')
    for j in range(1, 10):
        print(f'  {j * i:2d}', end=' ')
    print()

# 33
cardno = input('카드번호 : ')
result = '잘못된 카드번호입니다'
if cardno[:2] == '35':
    if cardno == '356317': result = 'JCB카드 NH농협카드'
    elif cardno == '356901': result = 'JCB카드 신한카드'
    elif cardno == '356912': result = 'JCB카드 KB국민카드'
elif cardno[:1] == '4':
    if cardno == '404825': result = '비자카드 비씨카드'
    elif cardno == '438676': result = '비자카드 신한카드'
    elif cardno == '457973': result = '비자카드 국민은행'
elif cardno[:1] == '5':
    if cardno == '515594': result = '마스터카드 신한카드'
    elif cardno == '524353': result = '마스터카드 외환카드'
    elif cardno == '5540926': result = '마스터카드 국민은행'
print(f'{cardno} / {result}')