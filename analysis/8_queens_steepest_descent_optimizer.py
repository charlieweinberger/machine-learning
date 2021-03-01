from random import random

# python analysis/8_queens_steepest_descent_optimizer.py

"""

The function steepest_descent_optimizer(n) starts with the best of 100 random locations arrays, and on each iteration, repeatedly compares all possible next location arrays that result from moving one queen by one space, and chooses the one that results in the minimum cost. The algorithm will run for n iterations.

- By "starts with the best of 100 random locations arrays", I mean that you should start by generating 100 random locations arrays and selecting the lowest-cost array to be your initial locations array.

- There are 8 queens, and each queen can move in one of 8 directions unless one of those directions is blocked by another queen or invalid due to being off the board.

- The number of possible "next location arrays" resulting from moving one queen by one space will be around 8×8 = 64, though probably a little bit less. This means that on each iteration, you'll have to check about 64 possible next location arrays and choose the one that minimizes the cost function.

- If multiple configurations minimize the cost, randomly select one of them. If every next configuration increases the cost, then terminate the algorithm and return the current locations.

"""

def random_locations(n):
    # n = 100
    boards_list = []
    for _ in range(n):
        
        location = []
        for _ in range(8):
            x = round(8*random() - 0.5)
            y = round(8*random() - 0.5)
            location.append((x, y))
        
        board = [['.' for _ in range(8)] for _ in range(8)]
    
        for i in range(8):
            x = location[i][0]
            y = location[i][1]
            board[x][y] = str(i)
        
        boards_list.append(board)
    
    return boards_list

def steepest_descent_optimizer(n):
    for _ in range(n):
        100_random_locations = random_locations(100)