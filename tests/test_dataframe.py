import sys
sys.path.append('src')
from dataframe import DataFrame
sys.path.append('kaggle/titanic')
from parse_line import parse_line

df = DataFrame.from_array(
    [
        ['Kevin', 'Fray', 5],
        ['Charles', 'Trapp', 17],
        ['Anna', 'Smith', 13],
        ['Sylvia', 'Mendez', 9]
    ],
    columns = ['firstname', 'lastname', 'age']
)

assert df.query('SELECT firstname, age').to_array() == [
    ['Kevin', 5],
    ['Charles', 17],
    ['Anna', 13],
    ['Sylvia', 9]
]

print("passed test")