from decision_tree import *

def draw_points(points): # doesnt work

    x_vals = [point['x'] for point in points]
    y_vals = [point['y'] for point in points]

    map_to = {(x, y): '' for x in range(-5, 5) for y in range(5, max_y)}

    for point in points:
        point_list = (point['x'], point['y'])
        map_to[point_list] += str(point['class'])

    for y in range(max_y, min_y):
        string = f'y={y}  '
        for x in range(min_x, max_x):
            string += map_to[(x, y)] + '   '
        print(string[0:-3])
    
    string = '    '
    for x in range(min_x, max_x):
        string += f'x={x} '
    print(string[0:-1], '\n')

    """
    print('\ny=9  ' + map_to[(1, 9)] + '   ' + map_to[(2, 9)] + '   ' + map_to[(3, 9)] + '   ' + map_to[(4, 9)] + '   ' + map_to[(5, 9)] + '   ' + map_to[(6, 9)] + '   ' + map_to[(7, 9)] + '   ' + map_to[(8, 9)] + '   ' + map_to[(9, 9)])

    print('y=8  ' + map_to[(1, 8)] + '   ' + map_to[(2, 8)] + '   ' + map_to[(3, 8)] + '   ' + map_to[(4, 8)] + '   ' + map_to[(5, 8)] + '   ' + map_to[(6, 8)] + '   ' + map_to[(7, 8)] + '   ' + map_to[(8, 8)] + '   ' + map_to[(9, 8)])

    print('y=7  ' + map_to[(1, 7)] + '   ' + map_to[(2, 7)] + '   ' + map_to[(3, 7)] + '   ' + map_to[(4, 7)] + '   ' + map_to[(5, 7)] + '   ' + map_to[(6, 7)] + '   ' + map_to[(7, 7)] + '   ' + map_to[(8, 7)] + '   ' + map_to[(9, 7)])

    print('y=6  ' + map_to[(1, 6)] + '   ' + map_to[(2, 6)] + '   ' + map_to[(3, 6)] + '   ' + map_to[(4, 6)] + '   ' + map_to[(5, 6)] + '   ' + map_to[(6, 6)] + '   ' + map_to[(7, 6)] + '   ' + map_to[(8, 6)] + '   ' + map_to[(9, 6)])

    print('y=5  ' + map_to[(1, 5)] + '   ' + map_to[(2, 5)] + '   ' + map_to[(3, 5)] + '   ' + map_to[(4, 5)] + '   ' + map_to[(5, 5)] + '   ' + map_to[(6, 5)] + '   ' + map_to[(7, 5)] + '   ' + map_to[(8, 5)] + '   ' + map_to[(9, 5)])

    print('y=4  ' + map_to[(1, 4)] + '   ' + map_to[(2, 4)] + '   ' + map_to[(3, 4)] + '   ' + map_to[(4, 4)] + '   ' + map_to[(5, 4)] + '   ' + map_to[(6, 4)] + '   ' + map_to[(7, 4)] + '   ' + map_to[(8, 4)] + '   ' + map_to[(9, 4)])

    print('y=3  ' + map_to[(1, 3)] + '   ' + map_to[(2, 3)] + '   ' + map_to[(3, 3)] + '   ' + map_to[(4, 3)] + '   ' + map_to[(5, 3)] + '   ' + map_to[(6, 3)] + '   ' + map_to[(7, 3)] + '   ' + map_to[(8, 3)] + '   ' + map_to[(9, 3)])

    print('y=2  ' + map_to[(1, 2)] + '   ' + map_to[(2, 2)] + '   ' + map_to[(3, 2)] + '   ' + map_to[(4, 2)] + '   ' + map_to[(5, 2)] + '   ' + map_to[(6, 2)] + '   ' + map_to[(7, 2)] + '   ' + map_to[(8, 2)] + '   ' + map_to[(9, 2)])

    print('y=1  ' + map_to[(1, 1)] + '   ' + map_to[(2, 1)] + '   ' + map_to[(3, 1)] + '   ' + map_to[(4, 1)] + '   ' + map_to[(5, 1)] + '   ' + map_to[(6, 1)] + '   ' + map_to[(7, 1)] + '   ' + map_to[(8, 1)] + '   ' + map_to[(9, 1)])
    
    print('    x=1 x=2 x=3 x=4 x=5 x=6 x=7 x=8 x=9\n')
    """

def tree_structure(input_node, min_size_to_split, num=''):
    
    print("structure of tree after iteration {}\n".format(num))
    draw_points(input_node.points)
    
    if not input_node.is_pure_enough(min_size_to_split):
    
        for split in input_node.splits:
            print('split at ' + str(split.dim) + '=' + str(split.midpoint) + ':', '\n')
            for node in split.children[::-1]:
                draw_points(node.points)
    
    else:
        print("node is pure\n")

def best_split(input_node, num=''):
    print("\nbest split after iteration {}".format(num))
    split = input_node.find_best_split()
    print(str(split.dim) + '=' + str(split.midpoint), '\n')

# class 0 means 'o' and class 1 means 'x'

points = [
    {'x': 0, 'y': 1, 'class': 1},
    {'x': 0, 'y': 1, 'class': 1},
    {'x': 0, 'y': 2, 'class': 1},
    {'x': 0, 'y': 2, 'class': 0},
    {'x': 1, 'y': 1, 'class': 1},
    {'x': 1, 'y': 1, 'class': 0},
    {'x': 1, 'y': 1, 'class': 0},
    {'x': 1, 'y': 2, 'class': 1},
    {'x': 1, 'y': 2, 'class': 1},
    {'x': 1, 'y': 2, 'class': 0}
]

decision_tree = DecisionTree()
decision_tree.fit(points)

assert decision_tree.predict({'x': 0, 'y': 1}) == 1
assert decision_tree.predict({'x': 0, 'y': 2}) == 0 # random => 0
assert decision_tree.predict({'x': 1, 'y': 1}) == 0
assert decision_tree.predict({'x': 1, 'y': 2}) == 1

print('passed')