'''
Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
'''
# import pandas as pd

# df = pd.read_csv('california_housing_train.csv')
# avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()
# print(avg)

'''
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" в зоне минимального значения переменной min_population и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.
'''
import pandas as pd

df = pd.read_csv('california_housing_train.csv')

max_households_in_min_population =  df[df['population'] == df['population'].min()]['households'].max()

print(max_households_in_min_population)

# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value

# print(data[data['median_house_value'] == data['median_house_value'].min()]['population'].max())
