'''
Задача: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

print(pd.get_dummies(data['whoAmI']))

# перевести указанный код в 'one hot' вид без get_dummies возможно следующим образом:

# создать вручную колонки с кодировкой с помощью метода .astype(int):
data['robot'] = (data['whoAmI'] == 'robot').astype(int)
data['human'] = (data['whoAmI'] == 'human').astype(int)

print("One-hot Encoded Data:")
print(data.head())

