'''
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''
# my_list = [1, 1, 2, 0, -1, 3, 4, 4]

# print(len(list(set(my_list))))

# res = []
# for el in my_list:
#     if el not in res:
#         res.append(el)
# print(len(res))

'''
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3] 
'''

# my_list = [1, 2, 3, 4, 5] 
# k = 3

# # print(my_list[k:])
# # print(my_list[:k])
# print(my_list[k:] + my_list[:k])
# ____________________
# for _ in range(k-1):
#     last = my_list.pop()
#     my_list.insert(0, last)
# print(my_list)

'''
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# традиционный итератор с методом add()
unique_values = set()
for item in my_list:
    for value in item.values():
        unique_values.add(value)
print(unique_values)


# set comprehension
print(set(value for item in my_list for value in item.values()))

'''
Задача №23. Решение в группах Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''
# my_list = [0, -1, 5, 2, 3]
# counter = 0

# for i in range(1, len(my_list)):
#     if my_list[i] > my_list[i -1]:
#         counter +=1
# print(counter)

'''
my_list = [10, 11, 20, 30, 55, 60]
Найти четные элементы на нечетных позициях.
'''
my_list = [10, 11, 20, 30, 55, 60]
for i in range(0, len(my_list), 2):
    if my_list[i]% 2 == 0:
        print(my_list[i])