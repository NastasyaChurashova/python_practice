'''
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0= 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
'''

# def find_fibonacci_num(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return find_fibonacci_num(n - 1) + find_fibonacci_num(n - 2)

# print(find_fibonacci_num(7)) 

'''
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''


# def substitute_grades_to_min(n, grades, max_grade, min_grade, index=0):
#     if index == n:
#         return grades
#     if grades[index] == max_grade:
#         grades[index] = min_grade
#     return substitute_grades_to_min(n, grades, max_grade, min_grade, index + 1)

# def main(n, grades):
#     if n == 0:
#         return grades
#     max_grade = max(grades)
#     min_grade = min(grades)
#     return substitute_grades_to_min(n, grades, max_grade, min_grade)

# n = 5
# grades = [1, 3, 3, 3, 4]
# result = main(n, grades)
# print(result) 
# _______________

# lst1  = [1, 3, 3, 3, 4]
# max_grade = max(lst1)
# min_grade = min(lst1)
# lst2 = []
# for grade in lst1:
#     if grade == max_grade:
#         lst2.append(min_grade)
#     else:
#         lst2.append(grade)

# print(lst2)

# print([min_grade if grade == max_grade else grade for grade in lst1])

# _______________

# def func(lst1, lst2=[], min_grade=min(lst1), max_grade=max(lst1)):
#     if len(lst1) == 0:
#         return lst2
#     if lst1[0] == max_grade:
#         lst2.append(min_grade)
#     else:
#         lst2.append(lst1[0])
#     return func(lst1[1:], lst2)

# print(func(lst1))
'''
Задача №35. Общее обсуждение
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
'''
# def if_num_is_prime1(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return "no"
#     return "yes"
# print(if_num_is_prime1(7))

# def if_num_is_prime2(n, i=2):
#     if i < n:
#         if n % i == 0:
#             return "no"
#         return if_num_is_prime2(n, i+1)
#     return "yes"

# print(if_num_is_prime2(4))
      

'''
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''

number = "3 4"


def func1(data):
    new_data = ""
    for s in reversed(data):
        new_data += s
    return new_data


print(func1(number))


def func2(data, new_data=""):
    if len(data) == 0:
        return new_data
    return func2(data[:-1], new_data+data[-1])


print(func2(number))