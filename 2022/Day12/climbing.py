from collections import OrderedDict, defaultdict
from functools import lru_cache
from dataclasses import dataclass
from math import sqrt, floor
import numpy as np
from pprint import pprint

"""
Climb the mountain in as few steps as possible
This will require building a tree and recording places visited in order to prevent cycles
I'll need a node data struct, 
I'll need a global visited struct
I'll need a grid made of strings which are a certain length
I'll need a recursive function

the answer is to find the fewest steps possible


"""
class Mountain():
    """
    mnt = Mountain(grid)
    mnt.print()
    print(mnt.find_start())
    print(mnt.get_height((2, 1)))
    print(mnt.return_paths((0,0)))
    print(mnt.return_paths((0,3)))
    """
    def __init__(self, grid):
        self.grid = grid
        self.grid_height = len(grid)
        self.grid_length = len(grid[0])
        self.one_above = {
            'a':'b',
            'b':'c',
            'c':'d',
            'd':'e',
            'e':'f',
            'f':'g',
            'g':'h',
            'h':'i',
            'i':'j',
            'j':'k',
            'k':'l',
            'l':'m',
            'm':'n',
            'n':'o',
            'o':'p',
            'p':'q',
            'q':'r',
            'r':'s',
            's':'t',
            't':'u',
            'u':'v',
            'v':'w',
            'w':'x',
            'x':'y',
            'y':'z', 'z':'E'}

    def get_height(self, pos):
        return self.grid[pos[0]][pos[1]]
        
    def is_reachable(self, height1, height2):
        if height1 == 'S':
            height1 = 'a'
        if height2 == 'S':
            height2 = 'a'
        if height1 == 'E':
            height1 = 'z'
        if height2 == 'E':
            height2 = 'z'
        if height1 >= height2 or height2 == self.one_above[height1]:
            return True
        return False

    def return_paths(self, pos):
        height = self.get_height(pos)
        r = pos[0]
        c = pos[1]
        neighbors = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)] # N E S W
        corrected_neighbors = [n if (0 <= n[0] < self.grid_height) and (0 <= n[1] < self.grid_length) else None for n in neighbors]
        return [neighbor if neighbor and self.is_reachable(height, self.get_height(neighbor) ) else None for neighbor in corrected_neighbors]

    def find_pos(self, letter):
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                if self.get_height((row, column)) == letter:
                    return (row, column)

    def print(self):
        for row in self.grid:
            pprint(row)

# path_lengths = defaultdict(int)
paths = defaultdict(int)
length_to_point = defaultdict(list)

@lru_cache(None)
def find_next_path(pos, length):
    for p in mnt.return_paths(pos):
        if not p or p in visited[p]:
            continue
        if paths[p] > 0:
            paths[p] = min([paths[p], length+1])
        else: 
            paths[p] = length+1
        visited[pos].append(pos)
        find_next_path(p, length+1)
    return 

file_dir = '2022/Day12/'
input_filename = file_dir + 'test.txt'
# input_filename = file_dir + 'mountains.txt'
#reached  maximum recusion depth with object

grid = []
for raw_line in open(input_filename, 'r'):
    grid.append(raw_line.strip('\n'))

mnt = Mountain(grid)

starting_pos = mnt.find_pos('S')
ending_pos = mnt.find_pos('E')
for p in mnt.return_paths(starting_pos):
    if p:
        visited[p].append(p)
        find_next_path(p, 1)


# calculate paths
smallest_path = paths[ending_pos]

print(f"Minimum path length from S to E is {smallest_path}")


"""
def find_next_path(pos, length, visited):
    for p in mnt.return_paths(pos):
        if not p or p in visited:
            continue
        if paths[p] > 0:
            paths[p] = min([paths[p], length+1])
        else: 
            paths[p] = length+1
        new_visited = visited.copy()
        new_visited.append(pos)
        find_next_path(p, length+1, new_visited)
    return 

"""