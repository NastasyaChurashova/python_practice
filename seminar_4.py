'''
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
'''
# def check_duplicate_symbols(str):
#     # Разбиваем строку на список символов
#     symbols = str.split()
    
#     # Словарь для отслеживания количества вхождений каждого символа
#     counts = {}
    
#     # Новый список для хранения результатов
#     result = []
    
#     for symbol in symbols:
#         if symbol in counts:
#             counts[symbol] += 1
#             result.append(f'{symbol}_{counts[symbol]}')
#         else:
#             counts[symbol] = 0
#             result.append(symbol)
    
#     # Объединяем список в строку и выводим результат
#     print(' '.join(result))

# # Пример использования
# my_str = 'a a a b c a a d c d d'
# check_duplicate_symbols(my_str)

input_string = "a a a b c a a d c d d"
words = input_string.split()
counts = {}

for word in words:
    if word not in counts:
        print(word, end=' ')
    else:
        print(f"{word}_{counts[word]}", end=' ')
    counts[word] = counts.get(word, 0) + 1

'''
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore;The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore,I'm sure that the shells are sea
shore shells
Output: 19
'''


input_str = "She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells"

print(len(set(input_str.lower().split())))


'''
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих
слайдах


Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)
Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n) 

'''
# import random
# sequence = random.sample(range(100), 10)
# print(sequence)
# max_number = 1
# for num in sequence:
#     if max_number < num:
#         max_number = num
# print(max_number)