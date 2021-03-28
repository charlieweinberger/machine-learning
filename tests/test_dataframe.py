import sys
sys.path.append('src')
from dataframe import DataFrame
sys.path.append('kaggle/titanic')
from parse_line import parse_line

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Sylvia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)

assert df.query("SELECT lastname, firstname, age ORDER BY age DESC").to_array() == [
  ['Trapp', 'Charles', 17],
  ['Smith', 'Anna', 13],
  ['Mendez', 'Sylvia', 9],
  ['Fray', 'Kevin', 5]
]

print("\npassed test 1")

assert df.query("SELECT firstname ORDER BY lastname ASC").to_array() == [
  ['Kevin'],
  ['Sylvia'],
  ['Anna'],
  ['Charles']
]

print("\npassed test 2")

df = DataFrame.from_array(
    [['Kevin', 'Fray', 5],
    ['Melvin', 'Fray', 5],
    ['Charles', 'Trapp', 17],
    ['Carl', 'Trapp', 17],
    ['Anna', 'Smith', 13],
    ['Hannah', 'Smith', 13],
    ['Sylvia', 'Mendez', 9],
    ['Cynthia', 'Mendez', 9]],
    columns = ['firstname', 'lastname', 'age']
)

assert df.query("SELECT lastname, firstname, age ORDER BY age ASC, firstname DESC").to_array() == [
  ['Fray', 'Melvin', 5],
  ['Fray', 'Kevin', 5],
  ['Mendez', 'Sylvia', 9],
  ['Mendez', 'Cynthia', 9],
  ['Smith', 'Hannah', 13],
  ['Smith', 'Anna', 13],
  ['Trapp', 'Charles', 17],
  ['Trapp', 'Carl', 17]
]

print("\npassed test 3")