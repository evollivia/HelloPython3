def readUnit():
    mm = float(input('길이(mm)를 입력하세요: '))
    return mm

def convertUnit(mm):
    units = [mm]
    units.append(mm * 0.1)
    units.append(mm * 0.001)
    units.append(mm * 0.03937)
    units.append(mm * 0.003291)
    return units

def printUnits(units):
    print(f'''
    {units[0]} mm --> {units[1]} cm
    {units[0]} mm --> {units[2]} m
    {units[0]} mm --> {units[3]} inch
    {units[0]} mm --> {units[4]} ft
    ''')

######################################################
products = {'쌀' : 9900, '상추' : 1900,'고추' : 2900,'마늘' : 8900,'통닭' : 5600,'햄' : 6900,'치즈' : 3900}
def readDiscount():
    print(f'''
{'-'*39}
-- 한빛마트 오늘의 할인 가격표 출력 시스템 --
{'-'*39}''')
    rate = int(input('오늘의 할인율을 입력하세요. '))
    return rate

def discountPrice(rate):
    dcprice = []
    dc = (1-(rate/100))
    for v in products.values():
        dcprice.append(v*dc)
    return dcprice

def printPrices(dcprice, rate):
    result = ''
    for idx, k in enumerate(products):
        result += f'''{k}\t: {products[k]:,d} 원 {rate} %DC -> {dcprice[idx]:,.0f} 원\n'''
    print(f'{result}'
          f'{"-"*39}')

######################################################

def checkJumin(jumin):
    result = '주민번호가 유효하지 않습니다.'
    sum = 0

    weight = [2,3,4,5,6,7,8,9,2,3,4,5]
    for i in range(12):
        sum += int(jumin[i]) * weight[i]

    checker = (11 - (sum % 11)) % 10
    if checker == int(jumin[12]):
        result = '유효한 주민번호입니다.'
    print(result)
    return result