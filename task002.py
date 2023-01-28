# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Введите трехзначное число: '))
summa = 0
if num // 1000 == 0:
    while num != 0:
        ost = num % 10
        summa = summa + ost
        num = num // 10
    print(summa)
else:
    print('Число не трехзначное')

