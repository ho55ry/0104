# ==================================================================
# 2 장
# ==================================================================
# 2-1 ---------------------------------------------------------------
import pandas as pd

FILE=r'D:\EXAM_python\textbook\data\gapminder.tsv'
df = pd.read_csv(FILE,sep='\t')

print(df)
print(df.head())
print(type(df))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

# 2-2 ----------------------------------------------------------------
country_df = df['country']

print(type(country_df))
print(country_df.head())
print(country_df.tail())

subset = df[['country', 'continent', 'year']]

print(type(subset))
print(subset.head())
print(subset.tail())

print(df.loc[0])
print(df.loc[99])
# print(df.loc[-1]) # loc는 인덱스명 불러옴

number_of_rows = df.shape[0] # df.shape = [rows,columns]
last_row_index = number_of_rows - 1
print(df.loc[last_row_index])

print(df.tail(n=1))
print(df.tail(n=2))

print(df.loc[[0, 99, 999]])

# ---------------------------------------------
subset_loc = df.loc[0] 
subset_head = df.head(1)
print(type(subset_loc))
print(type(subset_head))
# ----------------------------------------------
# head(tail)메서드, loc속성이 반환하는 자료형 다름
# loc : series , head(tail) : dataframe 

print(df.iloc[1])
print(df.iloc[99])
print(df.iloc[-1]) # iloc는 인덱스(위치) 이므로 -1=마지막값 가능
print(df.iloc[[0, 99, 999]])

subset = df.loc[:, ['year', 'pop']] 
print(subset.head())

subset = df.iloc[:, [2, 4, -1]] 
print(subset.head())

small_range = list(range(5)) 
print(small_range)

print(type(small_range))

subset = df.iloc[:, small_range] 
print(subset.head())

small_range = list(range(3, 6)) 
print(small_range)

subset = df.iloc[:, small_range] 
print(subset.head())

small_range = list(range(0, 6, 2)) 
subset = df.iloc[:, small_range] 
print(subset.head())

subset = df.iloc[:, :3] 
print(subset.head())

subset = df.iloc[:, 0:6:2] 
print(subset.head())

print(df.iloc[[0, 99, 999], [0, 3, 5]])
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])
print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])


# ==================================================================
# 3 장
# ==================================================================
# 3-1 --------------------------------------------------------------
s = pd.Series(['banana', 42])
print(s)

s = pd.Series(['Wes McKinney', 'Creator of Pandas'])
print(s)

s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)

scientists = pd.DataFrame({ 
    'Name': ['Rosaline Franklin', 'William Gosset'], 
    'Occupation': ['Chemist', 'Statistician'], 
    'Born': ['1920-07-25', '1876-06-13'], 
    'Died': ['1958-04-16', '1937-10-16'], 
    'Age': [37, 61]}) 
print(scientists)

scientists = pd.DataFrame( 
    data={'Occupation': ['Chemist', 'Statistician'], 
          'Born': ['1920-07-25', '1876-06-13'], 
          'Died': ['1958-04-16', '1937-10-16'],
          'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Age', 'Died']) 
print(scientists)

# OrderedDict 모듈 사용 방법 -----------------------------
# from collections import OrderedDict
# scientists = pd.DataFrame(OrderedDict([ 
#     ('Name', ['Rosaline Franklin', 'William Gosset']),
#     ('Occupation', ['Chemist', 'Statistician']), 
#     ('Born', ['1920-07-25', '1876-06-13']), 
#     ('Died', ['1958-04-16', '1937-10-16']), 
#     ('Age', [37, 61])])) 
# print(scientists)
# -------------------------------------------------------

# 3-2 ----------------------------------------------------------------
scientists = pd.DataFrame(
    data={'Occupation': ['Chemist', 'Statistician'], 
          'Born': ['1920-07-25', '1876-06-13'], 
          'Died': ['1958-04-16', '1937-10-16'],
          'Age': [37, 61]},
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Died', 'Age']) 

first_row = scientists.loc['William Gosset'] 
print(type(first_row))

print(first_row)

print(first_row.index)

print(first_row.values)

print(first_row.keys())

print(first_row.index[0])

print(first_row.keys()[0])

ages = scientists['Age'] 
print(ages)

print(ages.mean())

print(ages.min())

print(ages.max())

print(ages.std())

# 3-3 ----------------------------------------------------------------------------
scientists = pd.read_csv(r'D:\EXAM_python\textbook\data\scientists.csv')

ages = scientists['Age'] 

print(ages.max())
print(ages.mean())

print(ages[ages > ages.mean()])
print(ages > ages.mean())
print(type(ages > ages.mean()))
manual_bool_values = [True, True, False, False, True, True, False, True] 
print(ages[manual_bool_values])
print(ages + ages)
print(ages * ages)
print(ages + 100)
print(ages * 2)

print(pd.Series([1, 100]))
print(ages + pd.Series([1, 100]))
rev_ages = ages.sort_index(ascending=False) 
print(rev_ages)

print(ages * 2)
print(ages + rev_ages)

# 3-4 ----------------------------------------------------------------------------
print(scientists[scientists['Age'] > scientists['Age'].mean()])
# print(scientists.loc[[True, True, False, True]])
print(scientists.loc[[True, True, False, True,True, True, False, True]])
print(scientists * 2)


# 3-5 ----------------------------------------------------------------------------
print(scientists['Born'].dtype)
print(scientists['Died'].dtype)

born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d') 
print(born_datetime)

died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(died_datetime)

scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
print(scientists.head())

print(scientists.shape)

scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
print(scientists)

print(scientists['Age'])

import random

random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])

print(scientists.columns)

scientists_dropped = scientists.drop(['Age'], axis=1)

print(scientists_dropped.columns)