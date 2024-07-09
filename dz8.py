'''
Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
'''
from pandas import read_csv

data = read_csv('california_housing_train.csv')

# filtered_data = data[(data['population'] > 0) & (data['population'] < 500)]

# print(filtered_data)

# # avg = filtered_data["median_house_value"].mean()

# # print(avg)

'''
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" в зоне минимального значения переменной min_population и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.
'''
import pandas as pd

# Чтение файла
data = pd.read_csv('california_housing_train.csv')

# Найти минимальное значение переменной population
min_population = data['population'].min()

# Отфильтровать строки, где population равно минимальному значению
min_population_data = data[data['population'] == min_population]

# Найти максимальное значение переменной households среди отфильтрованных строк
max_households_in_min_population = min_population_data['households'].max()

print(max_households_in_min_population)
