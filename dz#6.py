# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#было

lst = [2, 3, 5, 9, 3]
lst = list(input("Введите числа через пробел:\n"))


sum = 0
for i in range(len(lst)):
    if i % 2 != 0:
       sum += lst[i]
print(f"Сумма равна: {sum}")

# стало

def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = [2, 3, 5, 9, 3]
sum_odd_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# было

n = int(input("Vvedite N: "))
list = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f"Posledovatel'nost': {list}\nSumma: {round(sum(list), 3)}")

# стало
lst = [(1+1/i)**i for i in range(1,n+1)]
print(f"Полученная сумма последовательности (1+1/n)^n равнна {round(sum(lst),2)}")