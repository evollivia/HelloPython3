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