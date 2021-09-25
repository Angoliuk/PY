import datetime
import random
import string
from random import randint

constName = 'Анголюк Стас'


def cipherCreate():

    print('Task 21-------------------------------------')


    print('Task 33-------------------------------------')
    y1 = int(input('Введіть рік: '))
    if y1 % 400 == 0: print('Високосний')
    elif y1 % 100 == 0: print('Невисокосний')
    elif y1 % 4 == 0: print('Високосний')
    else: print('Невисокосний')
    print('Task 13-------------------------------------')
    m2 = float(input('Введіть силу: '))
    if m2 >= 10: print('meteoric')
    elif m2 > 8: print('great')
    elif m2 > 7: print('major')
    elif m2 > 6: print('strong')
    elif m2 > 5: print('moderate')
    elif m2 > 4: print('light')
    elif m2 > 3: print('minor')
    elif m2 >= 2: print('very minor')
    else: print('micro')
    print('Task 3-------------------------------------')
    chr = str(input())
    if len(chr)==1:
        if chr == 'a' or chr == 'o' or chr == 'u' or chr == 'e' or chr == 'i': print('Голосна')
        elif chr == 'y': print('Може бути і голосною і приголосною')
        else: print('Приголосна або не буква')
    else: print('Треба лише один символ вводити...')



def printTimeStamp(myName):
  print('Автор програми: ' + myName)
  print('Час компіляції: ' + str(datetime.datetime.now()))


cipherCreate()
printTimeStamp(constName)

# print('Task 2 ----------------------------------')
# print('{:>70}'.format('Рахунок-фактура № _ від ___201_р.'))
# print('{}, {:^10} , {}'.format(
# 'Постачальник: Управління'
# 'Платник: ЧП Іванов Іван'
# '''
# інженерного захисту території міста та
# розвитку узбереження ОМР Код ЄДРПОУ
# 7812638 Р/рахунок № 39120382193044
# МФО 863248 в ГУДКУ в одеській області
# '''))
# print('Task 4 ----------------------------------')
# a = int(input('Вводьте тільки цілі числа : '))
# b = int(input('Вводьте тільки цілі числа : '))
# print('a = ', a, '; b = ', b)
# print('+', a+b, '; -', a-b, '; *', a*b, '; /', a/b, '; //', a//b, '; **', a**b, '; %', a%b)
# print('exercise 1 ----------------------------------')
# a = int(input('Штучки : '))
# b = int(input('Штукенції : '))
# print('Всього : ', a*0.075+b*0.112)
# print('exercise 2 ----------------------------------')
# c = int(input('Скільки хліба ви хочете взяти : '))
# print(c*(0.6*8.5))
# print('exercise 3 ----------------------------------')
# p = int(input('Р : '))
# v = int(input('V : '))
# t = int(input('T : '))
# n = (p*v)/8.314*(t+271.15)
# print(n)
# print('exercise 4 ----------------------------------')
# print(time.asctime())
# print('exercise 5 ----------------------------------')
# t2 = int(input('Tемпература : '))
# f2 = (t2 * (9/5)) + 32
# k2 = t2 + 271.15
# print('Фаренгейти: ', f2, '; Кельвіни: ', k2)
# print('exercise 6 ----------------------------------')
# h = int(input('Зріст : '))
# d3 = int(h/2.54)
# f3 = d3//12
# d3 = d3%12
# print('Фути: ', f3, '; Дюйми: ', d3)
# print('exercise 7 ----------------------------------')
# d4 = int(input('Днів : '))
# g4 = int(input('Годин : '))
# h4 = int(input('Хвилин : '))
# s4 = int(input('Секунд : '))
# ts = d4*86400+g4*3600+h4*60+s4
# print('Всього секунд: ', ts)
#  i = 0
#   j = 0
# for i in range(3):
#   line = ''
#   s = 0
#   for j in range(3):
#     s += 1
#     line += str(s+i*3) + '     '
#   print(line, '\n')
# print('Час початку  алгоритму: ' + str(datetime.datetime.now()))
# A = []
# for i in range(1000):
#     A.append(randint(0, 1000))
# print(A)
# print('Час початку сортування: ' + str(datetime.datetime.now()))
# for j in range(len(A)):
#     i = j - 1
#     currElem = A[j]
#     while i > -1 and A[i] > currElem:
#         A[i + 1] = A[i]
#         i = i - 1
#     A[i + 1] = currElem
#
# print(A)
# print('Час кінця: ' + str(datetime.datetime.now()))
# word = (input('Слово : '))
# diam = int(input('Діаметер палиці : '))
# cipher = []
# cipherLengh = diam*len(word)
# letters = string.ascii_letters
# for i in range(len(word)):
#     cipher.append(word[i])
#     for j in range (diam-1):
#         letter = ''.join(random.choice(letters))
#         cipher.append(letter)
# print(cipher)
#
# newWord = ''
# for i in range(len(word)):
#     newWord += cipher[i*diam]
#     print(i*diam)
# print ('Розшифровано : ', newWord)
# print('Task 29-------------------------------------')
# a = int(input('Сьогодні вихідний? '))
# b = int(input('Ви в відпустці?  '))
# if (a == 1 or b == 1): print('Будильник відключено')
# else: print('Будильник працює')
#
# print('Task 31-------------------------------------')
# a1 = 45
# b1 = int(input('Всього хвилин: '))
# c1 = int(input('Всього СМС: '))
# if (b1 >= 0 and c1 >= 0) :
#     d1 = 0
#     e1 = 0
#     if (b1 - 200 > 0): d1 = b1 - 200
#     if (c1 - 50 > 0): e1 = c1 - 50
#     tM1 = a1 + (d1 * 0.21) + (e1 * 0.18)
#     tK1 = 1.05*tM1+0.48
#     print('Базова плата: ', format(tM1, ".2f"), 'Рахунок: ', format(tK1, ".2f"))
# else: print('Error')
#
# print('Task 12-------------------------------------')
# num = input('Ваше число: ')
# sum = 0
# for i in range(len(num)):
#     sum += int(num[i])
# print(sum)
#
# print('Task 34-------------------------------------')
# a4 = int(input('Число перше: '))
# b4 = int(input('Число друге: '))
# d4 = a4
# if d4 > b4:
#     d4 = b4
# while (a4%d4 > 0) or (b4%d4 > 0):
#     d4 -= 1
# print(d4)
#
# print('Task 25-------------------------------------')
# array5 = [[0] * 21 for i in range (21)]
# for i in range(21):
#     for j in range(21):
#         array5[i][j] = f'{i} * {j} = {i*j}'
#     print(array5[i])
# print('Task 36-------------------------------------')
# t6 = int(input('Ведіть ваш тариф: '))
# mb6 = int(input('Скільки ви витратили мегабайт цього місяця: '))
# extraMb6 = 0
# p6 = 0
# if (t6 == 1000):
#     p6 = 20
#     if mb6 > 1000:
#         extraMb6 = mb6 - 1000
#         p6 += extraMb6 * 0.05
#     if p6 > 85:
#         print(f'Зараз ви платите {p6} грн, а могли б платити 85 із тарифом 5000')
#     elif p6 > 35:
#         print(f'Зараз ви платите {p6} грн, а могли б платити 35 із тарифом 2000')
#     else: print(f'Ви платите {p6} грн, все в нормі, кращого тарифу немає')
# elif (t6 == 2000):
#     p6 = 35
#     if mb6 > 2000:
#         extraMb6 = mb6 - 2000
#         p6 += extraMb6 * 0.04
#     if p6 > 85:
#         print(f'Зараз ви платите {p6} грн, а могли б платити 85 із тарифом 2000')
#     else:
#         print(f'Ви платите {p6} грн, все в нормі, кращого тарифу немає')
# elif (t6 == 5000):
#     p6 = 85
#     if mb6 > 5000:
#         extraMb6 = mb6 - 5000
#     p6 += extraMb6 * 0.02
#     print(f'Ви платите {p6} грн, все в нормі, кращого тарифу немає')
# else: print('Такого тарифу не існує')
#
# print('Task 7-------------------------------------')
# M37 = int(input('Скільки води ви використали? '))
# p7 = 20
# if M37 > 60:
#     p7 += 30 * 9.86 + 20 * 11.22 + 10 * 13.06 + (M37 - 60) * 17.89
# elif M37 > 50:
#     p7 += 30 * 9.86 + 20 * 11.22 + (M37 - 50) * 13.06
# elif M37 > 30:
#     p7 += 30 * 9.86 + (M37 - 30) * 11.22
# else: p7 += M37 * 9.86
# print('Ваш рахунок: ', format(p7, '.2f'))