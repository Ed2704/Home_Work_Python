# # Задача 6.
# # Напишите программу, которая принимает на вход цифру, обозначающую
# # день недели и проверяет, является ли этот день выходным.

# n = int(input('Введите число от 1 до 7, обозначающее день недели: '))
# if n == 6 or n == 7:
#     print('Да! Это выходной!')
# else:
#     print('Нет:( Это будни')

# Задача 8.
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату X, отличную от 0: '))
y = int(input('Введите координату Y, отличную от 0: '))

if x !=0 and y !=0:
    if x > 0 and y > 0:
        print('1 плоскость')
    elif x < 0 and y > 0:
        print('2 плоскость')
    elif x < 0 and y < 0:
        print('3 плоскость')
    else:
        print('4 плоскость')
else:
    print('Вы ввели координату равную 0')

