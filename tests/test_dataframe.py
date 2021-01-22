import sys
sys.path.append('src')
from dataframe import DataFrame

df = DataFrame.from_array(
    [[0, 0, 1], 
    [1, 0, 2], 
    [2, 0, 4], 
    [4, 0, 8], 
    [6, 0, 9], 
    [0, 2, 2], 
    [0, 4, 5], 
    [0, 6, 7], 
    [0, 8, 6],
    [2, 2, 0],
    [3, 4, 0]],
    columns = ['beef', 'pb', 'rating']
)

df = df.create_interaction_terms('beef', 'pb')

assert df.columns == ['beef', 'pb', 'rating', 'beef * pb'], df.columns
assert df.to_array() == [[0, 0, 1, 0], 
                        [1, 0, 2, 0], 
                        [2, 0, 4, 0], 
                        [4, 0, 8, 0], 
                        [6, 0, 9, 0], 
                        [0, 2, 2, 0], 
                        [0, 4, 5, 0], 
                        [0, 6, 7, 0], 
                        [0, 8, 6, 0],
                        [2, 2, 0, 4],
                        [3, 4, 0, 12]], df.to_array()

print("passed")