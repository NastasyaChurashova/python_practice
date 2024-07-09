''' #1
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values
'''

# transformation = <???>
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')


'''
Задача №2. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
Пример ввода и вывода данных представлены на
следующем слайде

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10 
'''
# from math import pi
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# # lst = [1, 3, 3, 5]
# # print(max(lst, key=lst.count))

# def find_farthest_orbit(orbits):

#     return max([orbit for orbit in orbits if orbit[0] != orbit[1]], key=lambda orbit: pi * orbit[0] * orbit[1])

# print(find_farthest_orbit(orbits))

'''
Задача №3. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

Ввод: 
values = [0, 2, 10, 6] 
    if same_by(lambda x: x % 2, values):
        print('same')
    else:
        print('different')

Вывод:same
'''
values = [0, 2, 10, 6]
characteristic = lambda x: x % 2

# def same_by(characteristic, objects):
#     if not objects:
#         return True
    
#     first_value = characteristic(objects[0])
#     filtered_objects = filter(lambda x: characteristic(x) == first_value, objects)
#     return len(list(filtered_objects)) == len(objects)
#     # return all(characteristic(obj) == first_value for obj in objects)

# if same_by(characteristic, values):
#     print('same')
# else:
#     print('different')

# same_by(characteristic, values)
# __________________________

def same_by(characteristic, objects):
    my_set = set(map(characteristic, objects))  # из результата вызова функции lambda формируем список
      # уже из списка делаем множество, set - набор элементов без дубликатов
    # таким образом, если длина множества =1,
    # то элементы в заданном списке имеют одинаковые характеристики
    # если длина множества =0, значит заданный список был пустым
    # в этом случае по условию, мы также должны вернуть True
    return True if len(my_set) == 1 or len(my_set) == 0 else False


def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) < 2


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')