# 실전예제 1
email = 'gildong@abc.com'
name = '홍길동'
id = 'gildong'
pw = '1234'
print(f'To. {email}\n '
      f'▶ 아이디 및 비밀번호 확인\n '
      f'  {name} 고객님 안녕하세요\n'
      f'   {name}고객님의 아이디와 비밀번호는 아래와 같습니다\n'
      f'   아이디 : {id}\n'
      f'   비밀번호 : {pw}')

# 실전예제 2
# date = input('요일 : ')
# datem = input('날짜 : ')
# ltemp = input('최저기온 : ')
# htemp = input('최고기온 : ')
# prob = input('비올확률 : ')
# micro = input('미세먼지 : ')
# sunrise = input('일출시간 : ')
# sunset = input('일몰시간 : ')
# souths = input('남해파도 : ')
# easts = input('동해파도 : ')
# wests = input('서해파도 : ')
#
# print(f'내일 날씨 예보 입니다.\n'
#       f'{date}요일인 {datem}의 아침 최저 기온은 {ltemp}도, 낮 최고 기온은 {htemp}도로 예보됐습니다.\n'
#       f'비올 확률은 {prob}%이고, 미세먼지는 {micro}수준일 것으로 예상됩니다.\n'
#       f'일출 시간은 {sunrise} 이고, 일몰 시간은 {sunset} 입니다.\n'
#       f'바다의 물결은 남해 앞바다 {souths}m, 동해 앞바다 {easts}m, 서해 앞바다 {wests}m 높이로 일겠습니다.\n'
#       f'지금까지 {datem} {date}요일 날씨 예보였습니다.')

# 영수증 예제
date = '2014. 07. 07 14:35:24'
soju = 2
chiken = 1

total = (soju * 3000) + (chiken * 12000)
supply = int(total * 100 / 110)
vat = int(total * 10 / 110)
paid = 50000
change = paid - total

print(f'''
[음식나라]
---------------------
소주\t\t{soju}\t\t{soju * 3000} 
너나치킨\t{chiken}\t\t{chiken * 12000}
---------------------
과세합계\t\t\t{supply}
부가세\t\t\t{vat} 
---------------------
총합계\t\t\t{total}
받은금액\t\t\t{paid}
잔돈\t\t\t\t{change}
---------------------
{date}
''')

#3
rate1 = 646
# 1stPlayer = 6513
long = 51651
# myprogram.java = 5216
# except = 6546
TimeLimit = 16355
numberOfWindowa = 6516

#11
# Name = input('이름 : ')
# Weight = input('몸무게 : ')
# Age = input('나이 : ')
# print(Name, Weight, Age)

#12 - 생년월일 계산
# 연나이 계산 : 현재년도 - 출생년도 (병역법, 교육법, 민방위)
# 만나이 : 현재년도 - 출생년도, 생일 안지남 (-1) (민법상, 2023-06부터)
# 한국식 나이 : 현재년도 - 출생년도 + 1
# currentYear = int(input('현재 년도를 입력하시오 : '))
# bitrhyear = int(input('태어난 년도를 입력하시오 : '))
# myage = currentYear - bitrhyear
# print(f'''현재 년도는 {currentYear}이고, 생일의 년도가 {bitrhyear}일때, 나이는 {myage}입니다.''')

#13
dan = 7
# print(f'{dan} x 1 = {dan * 1}')
# print(f'{dan} x 2 = {dan * 2}')
# print(f'{dan} x 3 = {dan * 3}')
# print(f'{dan} x 4 = {dan * 4}')
# print(f'{dan} x 5 = {dan * 5}')
# print(f'{dan} x 6 = {dan * 6}')
# print(f'{dan} x 7 = {dan * 7}')
# print(f'{dan} x 8 = {dan * 8}')
# print(f'{dan} x 9 = {dan * 9}')

print(f'''
{dan} x 1 = {dan * 1}
{dan} x 2 = {dan * 2}
{dan} x 3 = {dan * 3}
{dan} x 4 = {dan * 4}
{dan} x 5 = {dan * 5}
{dan} x 6 = {dan * 6}
{dan} x 7 = {dan * 7}
{dan} x 8 = {dan * 8}
{dan} x 9 = {dan * 9}
''')

GuGuDan = input('원하는 단수를 입력하시오 : ')
i = 1
while i < 10:
    print(int(GuGuDan) * i)
    i += 1