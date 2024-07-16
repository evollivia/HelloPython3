# 슬라이싱
# 연속적인 객체들(리스느, 튜플, 문자열)에 범위를 지정하고
# 선택해서 부분적으로 객체를 가져오는 방법 및 표기법
# 리스트 객체에서 필요한 부분의 항목만 뽑아 사용하는 것
# 시퀀스 지료형에 지원되는 기능(순서를 기억함) 중에 하나
# 객체명[시작 : 끝-1 : 스텝]

# 리스트 슬라이싱 예제
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(alphabet[2:6])
print(alphabet[0:5], alphabet[:5])
print(alphabet[3:8])
print(alphabet[5:10], alphabet[5:])
print(alphabet[3:9])
print(alphabet[:])
print(alphabet[::2])
print(alphabet[::-1])   # 역방향

# 문자열 슬라이스 : 문자열의 일부 추출 가능
# 주민번호에서 생년월일과 성별코드 추출
jumin = '123456-1234567'
birth = jumin[:6]
gender = jumin[7:8]
print(birth)
print(gender)
