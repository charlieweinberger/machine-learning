import sys
sys.path.append('src')
from dataframe import DataFrame

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0],
    [5, 5, [],                0],
    [5, 5, ['mayo'],          0],
    [5, 5, ['jelly'],         0],
    [5, 5, ['mayo', 'jelly'], 0]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)
df = df.create_dummy_variables('condiments')

assert df.columns == ['beef', 'pb', 'mayo', 'jelly', 'rating'], df.columns

assert df.to_array() == [[0, 0, 0, 0, 1],
                         [0, 0, 1, 0, 1],
                         [0, 0, 0, 1, 4],
                         [0, 0, 1, 1, 0],
                         [5, 0, 0, 0, 4],
                         [5, 0, 1, 0, 8],
                         [5, 0, 0, 1, 1],
                         [5, 0, 1, 1, 0],
                         [0, 5, 0, 0, 5],
                         [0, 5, 1, 0, 0],
                         [0, 5, 0, 1, 9],
                         [0, 5, 1, 1, 0],
                         [5, 5, 0, 0, 0],
                         [5, 5, 1, 0, 0],
                         [5, 5, 0, 1, 0],
                         [5, 5, 1, 1, 0]], df.to_array()

print("passed")