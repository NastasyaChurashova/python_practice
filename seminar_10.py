'''
Задача №1.
1. Изобразите отношение households к population с
помощью точечного графика
2. Визуализировать longitude по отношения к
median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('california_housing_train.csv')

# 1. Изобразите отношение households к population с помощью точечного графика

scatter_plot = sns.scatterplot(data=df, x='households', y='population')

scatter_plot.set_title('Relationship between Households and Population')
scatter_plot.set_xlabel('Households')
scatter_plot.set_ylabel('Population')

plt.show()

# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график

sns.relplot(data=df, x='longitude', y='median_house_value', kind='line')
plt.show()

# 3. Представить гистограмму по housing_median_age

# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age



# 1. Изобразите отношение households к population с помощью точечного графика
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('california_housing_train.csv')
scatter_plot = sns.scatterplot(data=df, x='households', y='population')
plt.show()

plt.figure(figsize=(10, 6))

scatter_plot = sns.scatterplot(data=df, x='households', y='population')

scatter_plot.set_title('Relationship between Households and Population')
scatter_plot.set_xlabel('Households')
scatter_plot.set_ylabel('Population')

plt.show()

sns.histplot(data=df, x='housing_median_age')
plt.show()

# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график

rel_plot = sns.relplot(x='longitude', y='median_house_value', kind='line', data=df, height=6, aspect=1.5)

rel_plot.set_axis_labels('Longitude', 'Median House Value')
rel_plot.fig.suptitle('Relationship between Longitude and Median House Value', y=1.02)

plt.show()

# 3. Представить гистограмму по housing_median_age

hist_plot = sns.histplot(data=df, x = 'housing_median_age')

hist_plot.set_xlabel('Housing Median Age')
hist_plot.set_ylabel('Frequency')
plt.title('Histogram for Housing Median Age')

plt.show()

# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age

sns.histplot(data=df, x='median_house_value', hue='housing_median_age')
plt.show()

hist_plot = sns.histplot(data=df, x = 'median_house_value', hue = 'housing_median_age')

hist_plot.set_xlabel('Median House Value')
hist_plot.set_ylabel('Frequency')
plt.title('Histogram for Median House Value with Hue based on Housing Median Age')

plt.show()

'''
Задача №2. Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы

Чтобы подключить датасет с пингвинами, воспользуйтесь данным
скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()

'''

penguins = sns.load_dataset("penguins")
print(penguins.head())

print(penguins.describe(include='all'))

print(penguins.isnull().sum())

penguins = penguins.dropna()

# Pair plot
sns.pairplot(penguins, hue='species')
plt.show()

# Correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(penguins.corr(), annot=True, cmap='coolwarm', center=0).set_title('Correlation Matrix')
plt.show()

# # Visualizations

# Histogram for numerical features
plt.figure(figsize=(10, 6))
sns.histplot(data=penguins, x='bill_length_mm', kde=True).set_title('Bill Length Distribution')
plt.show()

# Scatter plots
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species').set_title('Bill Length vs Bill Depth')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species').set_title('Flipper Length vs Body Mass')
plt.show()


'''
Задача №3.
1. Создать новый столбец в таблице с пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)

Чтобы подключить датасет с пингвинами, воспользуйтесь данным
скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()

'''
penguins = sns.load_dataset("penguins")
penguins.head()

penguins.loc[penguins['bill_length_mm'] > 42, 'height_group'] = 'Длинный'
penguins.loc[(penguins['bill_length_mm'] > 35) & (penguins['bill_length_mm'] < 42), 'height_group'] = 'Длинный'
penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'Маленький'
print(penguins.columns)

'''
Задача №4. Решение в группах
1. Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ
'''
penguins = sns.load_dataset("penguins")
penguins.head()

penguins.loc[penguins['bill_length_mm'] >= 42, 'height_group'] = 'длинный'
penguins.loc[(penguins['bill_length_mm'] >= 35) & (penguins['bill_length_mm'] < 42), 'height_group'] = 'средний'
penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'маленький'

plt.figure(figsize=(10, 6))
hist_plot = sns.histplot(data=penguins, x = 'flipper_length_mm', hue = 'height_group', multiple="stack")

hist_plot.set_xlabel('flipper_length_mm')
hist_plot.set_ylabel('Frequency')
plt.title('Histogram for Flipper Length (mm) with Hue based on Height Group')

plt.show()