import random

# *****************1*************
# n = 5
# f = 1

# while n > 1:
#     f *= n
#     n -= 1
# print(f)

# def func(n, f=1):
#     if n == 1:
#         return f
#     return func(n-1, f * n)
# print(func(5))

# a = 5
# fibo_p, fibo_n = 0, 1
# position = 2
# while fibo_n < a:
#     fibo_p, fibo_n  = fibo_n, fibo_p + fibo_n
#     position += 1
#     if fibo_n == a:
#         print (position)
#     else: print(-1)
# _____________________________________
# def func(a = 5, fibo_p = 1, fibo_n = 1, position= 2):
#     if fibo_n == a:
#         return position
#     elif fibo_n < a:
#         return func(a, fibo_n, fibo_p + fibo_n, position + 1)
#     else: 
#         return -1
    
# print(func())
# ________________________
# list_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# def if_number_is_fibonacci(list_fib, number):
#     return number in list_fib

# print(if_number_is_fibonacci(list_fib, 13))
# print(list_fib.index(13))


# ***********************15***************
"""
Задача №13. Решение в группах
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2
"""
# n = 6   
# range_start = -50
# range_end = 50

# random_numbers = [random.randint(range_start, range_end) for _ in range(n)]
# print(random_numbers)

numbers = "-20 30 -40 50 10 -10".split() #список разб строк
length = 0
max_length = 0

for elem in numbers:
    num = int(elem)
    if num > 0:
        length += 1
    else:
        length = 0
    if length > max_length:
        max_length = length
print(max_length)

# ******************#19******************
"""
Задача №15. Решение в группах
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""
data  =  [5, 1, 6, 5, 9]
max_elem = data[0]
min_elem = data[0]
for elem in data: 
    if elem > max_elem:
        max_elem = elem
    if elem < min_elem:
        min_elem = elem

print(min_elem, max_elem)

# через рекурсию:

def func(data, max_elem=data[1], min_elem=data[1]):
    if len(data) == 0:
        return max_elem, min_elem
    if data[0] > max_elem:
        max_elem = data[0]
    if data[0] < min_elem:
        min_elem = data[0]
    return func(data[1:], max_elem, min_elem)
print(func(data))