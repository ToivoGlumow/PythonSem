# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.



number = int(input("Введите произвольное число n: "))
print("Введите 0 или 1:")

sum_0 = 0
sum_1 = 0


while number > 0:
    num = int(input())
    if num == 0:
        sum_0 += 1
        number -= 1
    elif num == 1:
        sum_1 +=1
        number -= 1
    else:
        print("Введите 0 или 1")
if sum_1 < sum_0:
    print(f"Наименее встречающиеся чмсла 1, сумма которых равна {sum_1}")
elif sum_0 < sum_1:
    print(f"Наименее встречающиеся чмсла 0, сумма которых равна {sum_0}")
else:
    print(f"Числа 0 и 1 повторяются одинаковое количесво раз, сумма каждых в отдельности равна {sum_0}")
