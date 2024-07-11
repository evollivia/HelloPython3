# 4
x = 1
y = 2
z = 3
s0 = 9
v0 = 10
t = 11
g = 9.81

a = 3 * x
b = 3 * x + y
c = (x + y) / 7
d = (3 * x + y) / (z + 2)
e = s0 + v0 * t + (1 / 2 * g * t ** 2)

# 5 ~ 10

# 12
# 만나이 : 현재년도 - 출생년도, 생일 안지남 (-1) (민법상, 2023-06부터)
currentYear = int(input('현재 년도를 입력하시오 : '))
bitrhyear = int(input('태어난 년도를 입력하시오 : '))
isPass = bool(input('생일이 지났는가 (True/False)'))
myage = currentYear - bitrhyear
# myage = myage if (isPass == True) else (myage - 1)
myage = myage if isPass else (myage - 1)
print(f'''현재 년도는 {currentYear}이고, 생일의 년도가 {bitrhyear}일때, 나이는 {myage}입니다.''')

# 14
day = int(input('초를 입력하시오 : '))
hour = int(input('초를 입력하시오 : '))
minute = int(input('초를 입력하시오 : '))
days = round(day / 86400, 2)
hours = round(hour / 3600, 2)
minutes = round(minute / 60, 2)
print(f'''
{day}초 = {days}일
{hour}초 = {hours}시간
{minute}초 = {minutes}분
''')

# 16
received = int(input('받은금액을 입력하시오 : '))
price = int(input('제품금액을 입력하시오 : '))
change = received - price
change1 = change // 50000
change %= 50000
change2 = change // 10000
change %= 10000
change3 = change // 5000
change %= 5000
change4 = change // 1000
change %= 1000
change5 = change // 500
change %= 500
change6 = change // 100
change %= 100
change7 = change // 50
change %= 50
change8 = change // 10
change %= 10

print(f'''
잔돈은 50000원 {change1}개, 10000원 {change2}개, 5000원 {change3}개, 1000원 {change4}개, 
500원 {change5}개, 100원 {change6}개, 50원 {change7}개, 10원 {change8}개,
''')

price = 34_560
paid = 50_000
charge = paid - price

# w50000 = change / 50000      # 결과는 float
# w50000 = int(change / 50000) # 결과는 정수형으로 변환
w50000 = charge // 50000  # 파이썬 몫 연산자

w10000 = charge // 10000
charge = charge - (10000 * w10000)

w5000 = charge // 5000
charge = charge - (5000 * w5000)

w1000 = charge // 1000
charge = charge - (5000 * w1000)

w500 = charge // 5000
charge = charge - (5000 * w500)

w100 = charge // 5000
charge = charge - (5000 * w100)

w50 = charge // 5000
charge = charge - (5000 * w50)

w10 = charge // 5000
charge = charge - (5000 * w10)

print(f'''
금액 : {price}원
지불금액 : {paid}원
잔돈 : {paid - price}원
-------------------------
50000원  : {w50000}장
10000원  : {w10000}장
5000원   : {w5000}장
1000원   : {w1000}장
500원    : {w500}개
100원    : {w100}개
50원     : {w50}개
10원     : {w10}개
''')
