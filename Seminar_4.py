# Задача 30. Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
p = math.pi
d = float(input('ВВедите число в диапазоне 10^-1 ≤ d ≤ 10^-10: '))
n = 0
if ((10**-1) >= d >= (10**-10)):
    while d < 1:
        d *=10
        n +=1
    print(round(p,n))
else:
    print('Вы ввели некорректное число !!!')


# Задача 31. Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

a = int(input())
res = []
i = 2
while i * i < a + 1:
    if a % i == 0:
        res.append(i)
    while a % i == 0:
        a //= i
    i += 1
if a != 1:
    res.append(a)
print(res)

# Задача 32. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

some_str = input('Введите числа через пробел \n')
arr = [int(n) for n in some_str.split()]
res = []
for i in range(0, len(arr)):
    for j in range(0, len(arr)):
        if i != j and arr[i] == arr[j]:
            break
    else:
        res.append(arr[i])
print(res)