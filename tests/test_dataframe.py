import sys
sys.path.append('src')
from dataframe import DataFrame

print("Testing Assignment 28-2")

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sarah'])

assert df1.data_dict == {
                          'Pete': [1, 0, 1, 0],
                          'John': [2, 1, 0, 2],
                          'Sarah': [3, 1, 4, 0]
                        }, df1.data_dict

assert df1.columns == ['Pete', 'John', 'Sarah'], df1.columns

assert df1.to_array() == [
                           [1, 2, 3],
                           [0, 1, 1],
                           [1, 0, 4],
                           [0, 2, 0]
                         ], df1.to_array()

df2 = df1.select_columns(['Sarah', 'Pete'])

assert df2.to_array() == [
                           [3, 1],
                           [1, 0],
                           [4, 1],
                           [0, 0]
                         ], df2.to_array()

assert df2.columns == ['Sarah', 'Pete'], df2.columns

df3 = df1.select_rows([1, 3])

assert df3.to_array() == [
                           [0, 1, 1],
                           [0, 2, 0]
                         ], df3.to_array()

data_dict = {
  'Pete': [1, 0, 1, 0],
  'John': [2, 1, 0, 2],
  'Sarah': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sarah'])
df2 = df1.apply('John', lambda x: 7 * x)

ans = {
        'Pete': [1, 0, 1, 0],
        'John': [14, 7, 0, 14],
        'Sarah': [3, 1, 4, 0]
      }
assert df2.data_dict == ans, df2.data_dict

print("Passed Assignment 28-2")