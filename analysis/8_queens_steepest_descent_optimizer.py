from random import random
import math

# python analysis/8_queens_steepest_descent_optimizer.py

"""

The function steepest_descent_optimizer(n) starts with the best of 100 random locations arrays, and on each iteration, repeatedly compares all possible next location arrays that result from moving one queen by one space, and chooses the one that results in the minimum cost. The algorithm will run for n iterations.

- By "starts with the best of 100 random locations arrays", I mean that you should start by generating 100 random locations arrays and selecting the lowest-cost array to be your initial locations array.

- There are 8 queens, and each queen can move in one of 8 directions unless one of those directions is blocked by another queen or invalid due to being off the board.

- The number of possible "next location arrays" resulting from moving one queen by one space will be around 8×8 = 64, though probably a little bit less. This means that on each iteration, you'll have to check about 64 possible next location arrays and choose the one that minimizes the cost function.

- If multiple configurations minimize the cost, randomly select one of them. If every next configuration increases the cost, then terminate the algorithm and return the current locations.

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
            locations.append([x, y])
          
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

def steepest_descent_optimizer(n):
    
    best_of_100_random_locations = random_optimizer(100)
    all_random_locations = []
    
    for _ in range(n):

        all_elems = [elem for pair in best_of_100_random_locations['locations'] for elem in pair]
        all_ways_to_move_1 = []
        for i in range(len(all_elems)):
            
            new_locations = all_elems.copy()
            
            if i < len(all_elems) + 1 and new_locations[i] != 8:
                new_locations[i] += 1
            
            nested_new_locations = [[new_locations[2*j], new_locations[2*j + 1]] for j in range(8)]

            all_ways_to_move_1.append(nested_new_locations)
        
        locations_and_costs = [[locations, calc_cost(locations)] for locations in all_ways_to_move_1]
        costs = [calc_cost(locations) for locations in all_ways_to_move_1]
        lowest_cost = min(costs)

        for pair in locations_and_costs:
            if pair[1] == lowest_cost:
                lowest_cost_locations = pair[0]
        
        best_of_100_random_locations = {
                                          'locations': lowest_cost_locations,
                                          'cost': lowest_cost
        }
        all_random_locations.append(best_of_100_random_locations)
        
        if len(all_random_locations) > 3:
            
            most_recent_random_locations_set = all_random_locations[-1]
            trending_up = True
            for random_locations_set in all_random_locations[-4:]:
                if most_recent_random_locations_set['cost'] <= random_locations_set['cost']:
                    trending_up = False

            if trending_up:
                return all_random_locations[-4]

        if lowest_cost == 0:
            return best_of_100_random_locations
        
            
    return best_of_100_random_locations

print('')
ns = [10,50,100,500,1000]
for n in ns:
    print("steepest_descent_optimizer({}):".format(n), steepest_descent_optimizer(n))

# python analysis/8_queens_steepest_descent_optimizer.py