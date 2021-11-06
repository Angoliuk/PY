from random import randint
import statistics
import winsound

def work5():
    #
    # print('Task 1 -----------------------------------------------')
    #
    # array = []
    # arrayLength = int(input('Довжина списку: '))
    # if arrayLength > 6 :
    #     for i in range (arrayLength):
    #         array.append(randint(0, 10))
    #     array.sort()
    #     print(array[3:(arrayLength-3)])
    # else:
    #     print('Треба більше інформації для короля інформації')
    #
    #
    # print('Task 5 -----------------------------------------------')
    #
    # article = ['the', 'a', 'one', 'some', 'any']
    # noun = ['boy', 'girl', 'dog', 'town', 'car']
    # verb = ['drove', 'jumped', 'ran', 'walked', 'skipped']
    # preposition = ['to', 'from', 'over', 'under', 'on']
    #
    # for i in range (10):
    #     print('{} {} {} {}.'
    #           .format(
    #                 article[randint(0, 4)].title(),
    #                 noun[randint(0, 4)],
    #                 verb[randint(0, 4)],
    #                 preposition[randint(0, 4)]
    #           ))
    #
    # print('Task 7 -----------------------------------------------')
    #
    # number = int(input('ваше число: '))
    # strNumber = str(number)
    # numberName = ''
    # thousands = ['тисяча ', 'тисячі ', 'тисяч ']
    # hundreds = ['', 'сто ', 'двісті ',
    #             'триста ', ' чотириста ', 'п`ятсот ',
    #             'шістсот ', 'сімсот ', 'вісімсот ',
    #             'дев`тсот ']
    # decades = ['', 'десять ', 'двідцять ',
    #            'тридцять ', 'сорок ',
    #            'п`ятдесят ', 'шістдесят ',
    #            'сімдесят ', 'вісімдесят ',
    #            'дев`яносто ']
    # numbers = ['', 'один ', 'два ', 'три ', 'чотири ',
    #            'п`ять ', 'шість ', 'сім ',
    #            'вісім ', 'дев`ять ']
    #
    # if number > 999:
    #     numberName += numbers[int(strNumber[0])]
    #     if number // 1000 == 1:
    #         numberName += thousands[0]
    #     elif 1 < number // 1000 < 5:
    #         numberName += thousands[1]
    #     else:
    #         numberName += thousands[2]
    #     numberName += hundreds[int(strNumber[1])]
    #     numberName += decades[int(strNumber[2])]
    #     numberName += numbers[int(strNumber[3])]
    #
    # elif number > 99:
    #     numberName += hundreds[int(strNumber[0])]
    #     numberName += decades[int(strNumber[1])]
    #     numberName += numbers[int(strNumber[2])]
    #     print(numberName)
    # elif number > 9:
    #     numberName += decades[int(strNumber[0])]
    #     numberName += numbers[int(strNumber[1])]
    #     print(numberName)
    # elif number > 0:
    #     numberName += numbers[int(strNumber[0])]
    #     print(numberName)
    # else:
    #     print('У вас проблеми з грошима')

    # print('Task 10 -----------------------------------------------')
    #
    # variants = [u"\U0001F352", u"\U0001F514", u"\U0001F34B",
    #             u"\U0001F34A", u"\u2606", u"\U0001F480"]
    #
    # playing = True
    # money = 100
    # payment = 5
    #
    # while playing:
    #
    #     startGame = int(input('Почати гру - 1, Забрати виграш - 2: '))
    #     if startGame == 1:
    #
    #         result = []
    #         money -= payment
    #
    #         for i in range(3):
    #             result.append(variants[randint(0, 5)])
    #         print(result)
    #
    #         if result[0] == result[1] == result[2]:
    #             if result[0] == u"\U0001F514":
    #                 money += 100
    #                 print('Ви вийграли 100')
    #             elif result[0] == u"\U0001F480":
    #                 money = 0
    #                 playing = False
    #             else:
    #                 money += 25
    #                 print('Ви вийграли 25')
    #
    #         elif result[0] == result[1] or result[0] == result[2] or result[1] == result[2]:
    #             if result[0] == result[1] == u"\U0001F480" \
    #                     or result[0] == result[2] == u"\U0001F480" \
    #                     or result[1] == result[2] == u"\U0001F480":
    #                 money -= 5
    #                 print('Ви програли 5')
    #             else:
    #                 money += 10
    #                 print('Ви вийграли 10')
    #         else:
    #             print('спробуйте ще раз')
    #
    #         if money <= 0:
    #             playing = False
    #             print('Ви програли всі гроші \U0001F480 \U0001F480 \U0001F480')
    #         else:
    #             print('Ваш баланс {}'.format(money))
    #
    #     elif startGame == 2:
    #         print('Ви отримали {}'.format(money))
    #         playing = False
    #     else:
    #         print('bzzzzzzzzzzzzzzzzz')
    #         playing = False
    #
    #
    #
    # print('Task 13 -----------------------------------------------')
    #
    # passwords = ['never', 'gonna', 'give', 'you', 'up', 'never', 'gonna', 'let', 'you', 'down']
    # password = '0'
    #
    # while len(password) > 11 or len(password) < 7:
    #     numOfWords = 0
    #     password = ''
    #     while numOfWords < 2:
    #         candidate = passwords[randint(0, 9)]
    #         if len(candidate) > 2:
    #             password += candidate.title()
    #             numOfWords += 1
    # print(password)


    # print('Task 14 -----------------------------------------------')
    #
    # numArray = []
    # for j in range(10000):
    #     rightNumbers = []
    #     for i in range(j-1):
    #         if (j+1) % (i+1) == 0:
    #             rightNumbers.append((i+1))
    #     if sum(rightNumbers) == j+1:
    #         numArray.append(j+1)
    # print(numArray)

    # print('Task 18 -----------------------------------------------')
    #
    # printing = True
    # numArray = []
    # numArrayMin = []
    # numArrayMax = []
    #
    # while printing:
    #     newNum = input('Число: ')
    #     if newNum == '' or newNum == ' ':
    #         printing = False
    #     else:
    #         numArray.append(float(newNum))
    # average = statistics.mean(numArray)
    # for i in range(len(numArray)):
    #     if numArray[i] >= average:
    #         numArrayMax.append(numArray[i])
    #     else:
    #         numArrayMin.append(numArray[i])
    # print('Весь масив: ', numArray)
    # print('Більше середнього: ', numArrayMax)
    # print('Менше середнього: ', numArrayMin)
    # print('Середнє: ', average)

    # print('Task 19 -----------------------------------------------')
    #
    # sound = ['659', '659', '659', '523', '659', '784',
    #          '392', '523', '392', '330', '440', '494',
    #          '466', '440', '392', '659', '784', '880',
    #          '698', '784', '659', '523', '587', '494',
    #          ]
    #
    # time = ['250', '250', '300', '250', '250', '300',
    #         '300', '275', '275', '275', '250', '250',
    #         '275', '275', '275', '250', '250', '275',
    #         '275', '225', '250', '250', '225', '225',
    #         ]
    #
    # for i in range(len(sound)):
    #     winsound.Beep(int(sound[i]), int(time[i]))
    #
    # print('Task 20 -----------------------------------------------')
    #
    # music = [['659', '659', '659', '523', '659', '784',
    #          '392', '523', '392', '330', '440', '494',
    #          '466', '440', '392', '659', '784', '880',
    #          '698', '784', '659', '523', '587', '494'],
    #          ['659', '659', '659', '523', '659', '784',
    #           '392', '523', '392', '330', '440', '494',
    #           '466', '440', '392', '659', '784', '880',
    #           '698', '784', '659', '523', '587', '494',]
    #          ]
    #
    # for i in range(len(sound)):
    #     winsound.Beep(int(music[0][i]), int(music[1][i]))

    print('Task 23 -----------------------------------------------')

    numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for j in range(1000):
        totalResult = 0
        for i in range(2):
            totalResult += randint(1, 6)
        numbers[totalResult-1] += 1
    print(numbers)
    for i in range(12):
        print('''Число: {}
Частота: {}%
'''.format((i+1), numbers[i]/10))



    print('Task 25 -----------------------------------------------')



    print('Task 27 -----------------------------------------------')

work5()
