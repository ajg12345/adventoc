import numpy as np
from pprint import pprint

"""
grid of trees
for reforestation effort
trying to find a treehouse
need tree cover to remain hidden
look for number of trees that are visible from outside the grid

puzzle input is height of each tree
for example

3 0 3 7 3
2 5 5 1 2
6 5 3 3 2
3 3 5 4 9
3 5 3 9 0

0 0 0 0 0
0 1 1 0 0
0 1 0 1 0
0 0 1 0 0
0 0 0 0 0

(thats a five by five grid)

determine how many trees are visible
the example has 21 trees visible
"""

file_dir = '2022/Day8/'
input_filename = file_dir + 'test.txt'
# input_filename = file_dir + 'forest.txt'


tree_grid = []
for line in open(input_filename, 'r'):
    tree_line = [int(char) for char in line.strip('\n')]
    tree_grid.append(tree_line)


grid = np.array(tree_grid)
dim = len(grid)
seen = np.zeros((dim, dim))

pprint(grid)
visible_count = (dim * dim) - ( (dim - 2) * (dim - 2) )
def mark_internal_trees(grid, seen):
    starting_views = ['left', 'top', 'right', 'bottom']
    for view in starting_views:
        for row in range(dim - 2):
            tallest_tree = grid[row + 1, 0]
            if tallest_tree == 9:
                continue
            for column in range(dim - 2):
                if tallest_tree == 9:
                    break
                if grid[row + 1, column + 1] > tallest_tree:
                    tallest_tree = grid[row + 1, column + 1]
                    seen[row + 1, column + 1] = 1
        grid = np.rot90(grid)
        seen = np.rot90(seen)

mark_internal_trees(grid, seen)

total = seen.sum() + visible_count
print(f"the total number of visible trees is {total}")
