import sys
sys.path.append('src')
from dataframe import DataFrame

print("Testing Assignment 29-2")

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

columns = ['firstname', 'lastname', 'age']
arr = [['Kevin', 'Fray', 5],
       ['Charles', 'Trapp', 17],
       ['Anna', 'Smith', 13],
       ['Sylvia', 'Mendez', 9]]
df = DataFrame.from_array(arr, columns)

columns = ['firstname', 'lastname', 'age']
problem = df.select_rows_where(lambda row: len(row['firstname']) >= len(row['lastname']) and row['age'] > 10).to_array()
assert problem == [['Charles', 'Trapp', 17]], problem

ans = [['Kevin', 'Fray', 5],
       ['Sylvia', 'Mendez', 9],
       ['Anna', 'Smith', 13],
       ['Charles', 'Trapp', 17]]
assert df.order_by('age', True).to_array() == ans, df.order_by('age', True).to_array()

ans = [['Sylvia', 'Mendez', 9],
       ['Kevin', 'Fray', 5],
       ['Charles', 'Trapp', 17],
       ['Anna', 'Smith', 13]]
assert df.order_by('firstname', False).to_array() == ans, df.order_by('firstname', False).to_array()

print("Passed Assignment 29-2")