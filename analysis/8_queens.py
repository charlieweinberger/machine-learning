from random import random
import math

#  The 8-queens problem is a challenge to place 8 queens on a chess board in a way that none can attack each other. Remember that in chess, queens can attack any piece that is on the same row, column, or diagonal. So, the 8-queens problem is to place 8 queens on a chess board so that none of them are on the same row, column, or diagonal.

"""

Errors:

1. (0, 2)
2. (0, 4)
3. (1, 6)
4. (2, 4)
5. (2, 7)
6. (3, 4)
7. (3, 5)
8. (3, 7)
9. (4, 7)
10. (6, 7)

"""

def show_board(locations):
    board = [['.' for _ in range(8)] for _ in range(8)]
    
    for i in range(8):
        x = locations[i][0]
        y = locations[i][1]
        board[x][y] = str(i)

    for row_array in board:
        row_string = '  '.join(row_array)
        print(row_string)

def calc_cost(locations):
    cost = 0
    visited_errors = []
    for pair1 in locations: 
        for pair2 in locations:
            pair_of_pairs = [pair1, pair2]
            same_row_column_diagonal = same_row(pair1, pair2) or same_column(pair1, pair2) or same_diagonal(pair1, pair2)
            if pair1 != pair2 and same_row_column_diagonal and pair_of_pairs not in visited_errors and pair_of_pairs[::-1] not in visited_errors:
                cost += 1
                visited_errors.append(pair_of_pairs)
    return cost

def same_row(point1, point2):
    return point1[0] == point2[0]

def same_column(point1, point2):
    return point1[1] == point2[1]

def same_diagonal(point1, point2):
    x_diff = point2[0] - point1[0]
    y_diff = point2[1] - point1[1]
    return abs(x_diff) == abs(y_diff)

def random_optimizer(n):
    n_random_locations = []
    for _ in range(n):

        locations = []
        for _ in range(8):
            x = math.floor(8*random())
            y = math.floor(8*random())
            locations.append(tuple([x, y]))
          
        n_random_locations.append(locations)
    
    locations_and_costs = [[locations, calc_cost(locations)] for locations in n_random_locations]
    costs = [pair[1] for pair in locations_and_costs]
    
    for pair in locations_and_costs:
        if pair[1] == min(costs):
            lowest_cost_location = pair[0]
            lowest_cost = pair[1]

    ans = {
      'locations': lowest_cost_location,
      'cost': lowest_cost
    }
    return ans

print("\npart 1")
locations = [(0,0), (6,1), (2,2), (5,3), (4,4), (7,5), (1,6), (2,6)]
show_board(locations)

print("\npart 2")
assert calc_cost(locations) == 10, calc_cost(locations)
print("calc_cost(locations) = 10")

"""

print("\npart 3")
n_list = [10, 50, 100, 500, 1000]
for n in n_list:
    print(random_optimizer(n))

"""