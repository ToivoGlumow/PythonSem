# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

import math 

SumNumbers = int(input("Введите сумму задуманных двух чисел: "))
ProdNumbers = int(input("ВВедите произведение задуманных двух чисел: "))
fistNumber = 0
secondNumber = 0

D = (SumNumbers * SumNumbers) - 4 * 1 * ProdNumbers
if D == 0:
    fistNumber = (-1 * -SumNumbers) / (2 * 1)
    secondNumber = SumNumbers - fistNumber
    print(f"Исходные числа {secondNumber}, {fistNumber}")
elif D > 0:
    time1 = ((-1 * -SumNumbers) + math.sqrt(D)) / 2
    time2 = ((-1 * -SumNumbers) - math.sqrt(D)) / 2
    secondNumber = SumNumbers - time1
    print(f"Исходные числа {secondNumber}, {time1}")
    secondNumber = SumNumbers - time2
    print(f"Исходные числа {secondNumber}, {time2}")
else:
    print("Нет таких чисел")
