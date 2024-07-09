import math
# list = [1, 2,3, 5, 8, 15, 23, 38]

# def even (list):
#     for i in list:
#         if i % 2 == 0:
#             print(i, i ** 2)


# even(list)

# ************1*********
# n= int(input())
# m = int(input())
# print(math.ceil(m/n))

# ************2*********
# x= int(input())
# y = int(input())
# z = int(input())

# print(math.ceil((x+y+z)/2))

# ************3*********
"""
Задача №5. Решение в группах
Вагоны в электричке пронумерованы натуральными
числами, начиная с 1 (при этом иногда вагоны
нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить,
сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать
невозможно.
Input: 3 4(ввод на разных строках)
Output: 6
"""

# i, j = 3, 4
# if i == j:
#     print('нужна дополнительная информация')
# else:
#     print(i + j - 1)


# ************5*********
# year = int(input())
# if (year%4==0 or year%400==0 and year%100 != 0):
#     print('YES')
# else:
#     print('NO')

# print("Yes" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "No")

# ************HOMETASK*********
# ********2***
# n=123
# res=0

# while n>0:
#     x= n %10
#     res = res + x
#     n = n 

# ********4***
n = 123456

# digits = [int(digit) for digit in str(n)]
     
# if digits[0] + digits[1] + digits[2] == digits[3] + digits[4] + digits[5]:
#     print('yes')
# else :
#     print('no')
    
print('yes' if sum(map(int, str(n)[:3])) == sum(map(int, str(n)[3:])) else 'no') 
 