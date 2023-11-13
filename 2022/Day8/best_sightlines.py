import numpy as np
from pprint import pprint

"""
grid of trees
for reforestation effort
trying to find a treehouse spot with the best sightlines

puzzle input is height of each tree
for example

3 0 3 7 3
2 5 5 1 2
6 5 3 3 2
3 3 5 4 9
3 5 3 9 0

0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 8 0 0
0 0 0 0 0

and 8 is the max
"""

file_dir = '2022/Day8/'
input_filename = file_dir + 'test.txt'
input_filename = file_dir + 'forest.txt'

tree_grid = []
for line in open(input_filename, 'r'):
    tree_line = [int(char) for char in line.strip('\n')]
    tree_grid.append(tree_line)


grid = np.array(tree_grid)
dim = len(grid)
sightlines = np.ones((dim, dim))

def record_sightlines(grid, sightlines):
    starting_views = ['left', 'top', 'right', 'bottom']
    for view in starting_views:
        for row in range(dim):
            for column in range(dim):
                if column == 0:
                    sightlines[row, column] = 0
                tree_height = grid[row, column]
                trees_in_sight = 0
                for neighbor_position in range(column):
                    neighbor_height = grid[row, column - (neighbor_position + 1)]
                    trees_in_sight += 1
                    if neighbor_height >= tree_height:
                        break
                sightlines[row, column] *= trees_in_sight
        pprint(sightlines)
        grid = np.rot90(grid)
        sightlines = np.rot90(sightlines)
        

record_sightlines(grid, sightlines)

max = sightlines.max()
print(f"the total number of visible trees is {max}")
