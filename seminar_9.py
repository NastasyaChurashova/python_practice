from pandas import read_csv

'''
Задача №1. Решение в группах
1. Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
'''

file_path = 'california_housing_test.csv'
data = read_csv(file_path)

# print(type(data))

# print(data.shape)

# print(data.dtypes)

# print(data.info())

# print(data.describe())

'''
Задача №2. Решение в группах
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000

'''
# print(data.isnull())

# print(data[data['median_income'] < 2]['median_house_value'])

# print(data[['longitude', 'latitude']])

# print(data.iloc[:, :2])

print(data[(data['housing_median_age'] < 20) & (data['median_house_value'] > 70000)])

'''
Задача №3. Решение в группах
1. Определить какое максимальное и минимальное
значение median_house_value
1. Показать максимальное median_house_value, где
median_income = 3.1250
1. Узнать какая максимальная population в зоне
минимального значения median_house_value
'''

# 1. Определить какое максимальное и минимальное
# значение median_house_value
print(f'Минимальное - {data["median_house_value"].min()}, максимальное - {data["median_house_value"].max()}')
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
print((data[data['median_income']] == ["median_house_value"].max()))

# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value

print(data[data['median_house_value'] == data['median_house_value'].min()]['population'].max())