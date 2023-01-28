# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input('введите количество долек по вертикали: '))
n = int(input('введите количество долек по горизонтали: '))
k = int(input('введите количество отделяемых долек: '))

if m * n > k:
    if k // m or k // n:
        print('YES')
    else:
        print('NO')
else:
    print('Количество отделяемых долек больше всей шоколадки')

