# list_1 = [1, 2, 3, 4, 5]
# k = 6

# if k in list_1:
#     print(k)
# else:
#     for el in list_1:
#         if el == k + 1 or el == k - 1:
#             print(el)

'''
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:

A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:

А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
'''
k = 'ноутбук'
score = 0
my_dict_en = {
    1 : ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
    2 : ["D", "G"], 
    3 : ["B", "C", "M", "P"],
    4 : ["F", "H", "V", "W", "Y"],
    5 : ["K"],
    8 : ["J", "X"],
    10 :["Q", "Z"],
    }

my_dict_ru = {
    1 : ["А", "В", "Е", "И","Н", "О", "Р", "С", "Т"],
    2 : ["Д", "К", "Л", "М", "П", "У"], 
    3 : ["Б", "Г", "Ё", "Ь", "Я"],
    4 : ["Й", "Ы"],
    5 : ["Ж", "З", "Х", "Ц", "Ч"],
    8 : ["Ш", "Э", "Ю"],
    10 :["Ф", "Щ", "Ъ"],
    }

def is_russian(k, my_dict_ru):
    # Объединяем все значения из словаря в одно множество
    russian_letters = set()
    for values in my_dict_ru.values():
        russian_letters.update(values)
    # Проверяем, все ли символы слова находятся в этом множестве
    return all(char.upper() in russian_letters for char in k)

def is_english(k, my_dict_en):
    english_letters = set()
    for values in my_dict_en.values():
        english_letters.update(values)
    return all(char.upper() in english_letters for char in k)

def get_key_by_value(value, dictionary):
    for key, values in dictionary.items():
        if value.upper() in values:
            return key
    return None

def count_scrabble_score(word):
    score = 0
    if is_russian(word, my_dict_ru):
        for el in word:
            score += get_key_by_value(el, my_dict_ru)
    elif is_english(word, my_dict_en):
        for el in word:
            score += get_key_by_value(el, my_dict_en)
    return score

score = count_scrabble_score(k)
print(score) 


