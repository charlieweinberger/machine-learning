import sys
sys.path.append('src')
from dataframe import DataFrame
sys.path.append('kaggle/titanic')
from parse_line import parse_line

data = [
  ['Kevin Fray', 52, 100],
  ['Charles Trapp', 52, 75],
  ['Anna Smith', 52, 50],
  ['Sylvia Mendez', 52, 100],
  ['Kevin Fray', 53, 80],
  ['Charles Trapp', 53, 95],
  ['Anna Smith', 53, 70],
  ['Sylvia Mendez', 53, 90],
  ['Anna Smith', 54, 90],
  ['Sylvia Mendez', 54, 80],
]
columns = ['name', 'assignmentId', 'score']
df = DataFrame.from_array(data, columns)

assert df.group_by('name').aggregate('score', 'count').to_array() == [
    ['Kevin Fray', [52, 53], 2],
    ['Charles Trapp', [52, 53], 2],
    ['Anna Smith', [52, 53, 54], 3],
    ['Sylvia Mendez', [52, 53, 54], 3],
]

assert df.group_by('name').aggregate('score', 'max').to_array() == [
    ['Kevin Fray', [52, 53], 100],
    ['Charles Trapp', [52, 53], 95],
    ['Anna Smith', [52, 53, 54], 90],
    ['Sylvia Mendez', [52, 53, 54], 100],
]

assert df.group_by('name').aggregate('score', 'min').to_array() == [
    ['Kevin Fray', [52, 53], 80],
    ['Charles Trapp', [52, 53], 75],
    ['Anna Smith', [52, 53, 54], 50],
    ['Sylvia Mendez', [52, 53, 54], 80],
]

assert df.group_by('name').aggregate('score', 'sum').to_array() == [
    ['Kevin Fray', [52, 53], 180],
    ['Charles Trapp', [52, 53], 170],
    ['Anna Smith', [52, 53, 54], 210],
    ['Sylvia Mendez', [52, 53, 54], 270],
]

assert df.group_by('name').aggregate('score', 'avg').to_array() == [
    ['Kevin Fray', [52, 53], 90],
    ['Charles Trapp', [52, 53], 85],
    ['Anna Smith', [52, 53, 54], 70],
    ['Sylvia Mendez', [52, 53, 54], 90],
]

print("passed all tests")