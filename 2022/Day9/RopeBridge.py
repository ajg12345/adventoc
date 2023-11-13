import numpy as np
from pprint import pprint
from dataclasses import dataclass
from math import sqrt

"""
bridge spans a gorge
elves are ok
lets map rope physics to avoid falling through
consider a rope with head and tail, 
if the head moves far enough fromt he tail, the tail is pulled toward the head
model the position of hte knots in a 2d grid, 
then by followign a hypothetical series of motions (input) for the head
you can determine how the tail will move

Head must always be touching Tail
if head moves 2 steps u d l or r, the tail must move one step in that direction
if they are not in the same column or row (diagonal) and the head moves udlr,
the teail moves diagonal to keep up.

initially the head covers the tail

after moving, count the positions that the tail visited at least once
with this input:
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

the positions visited is 13
"""

file_dir = '2022/Day9/'
input_filename = file_dir + 'test.txt'
input_filename = file_dir + 'test2.txt'

input_filename = file_dir + 'series_of_motions.txt'


@dataclass
class XYPair:
    x: int
    y: int
    def get_value(self):
        return (self.x, self.y)
    
    def __add__(self, other):
        return XYPair(self.x + other.x, self.y + other.y)

def coord_dist(head, tail):
    return sqrt((head.x - tail.x)**2 + (head.y - tail.y)**2)

def coord_dir(head, tail):
    rise = (head.y - tail.y)
    run = (head.x - tail.x)
    return XYPair(run, rise)

def is_adjacent(coord1, coord2):
    return coord_dist(coord1, coord2) <= sqrt(2)

def parse_line(line):
    direction = line.split(' ')[0]
    counter = int(line.split(' ')[1])
    return [direction for i in range(counter)]

def calc_vector_move(pair):
    if abs(pair.x) == 2:
        return XYPair(pair.x/2, pair.y)
    if abs(pair.y) == 2:
        return XYPair(pair.x, pair.y/2)

def resolve_move(visited_coord, t_coord, h_coord):
    assert is_adjacent(h_coord, t_coord)
    visited_coord.append( (t_coord.get_value()) )

moves = []
for line in open(input_filename, 'r'):
    moves.extend(parse_line(line.strip('\n')))


h_coord = XYPair(0,0)
t_coord = XYPair(0,0)
visited_coord = [(t_coord.get_value())]
for move in moves:
    if move == 'U':
        h_coord.y += 1
        if t_coord != h_coord:  # rules out 1 case
            magnitude = coord_dist(h_coord, t_coord)
            if magnitude > sqrt(2):    # rules out 8 cases
                direction = coord_dir(h_coord, t_coord)
                move = calc_vector_move(direction)
                t_coord = t_coord + move

    elif move == 'D':
        h_coord.y -= 1
        if t_coord != h_coord:  # rules out 1 case
            magnitude = coord_dist(h_coord, t_coord)
            if magnitude > sqrt(2):    # rules out 8 cases    
                direction = coord_dir(h_coord, t_coord)
                move = calc_vector_move(direction)
                t_coord = t_coord + move

    elif move == 'L':
        h_coord.x -= 1
        if t_coord != h_coord:  # rules out 1 case
            magnitude = coord_dist(h_coord, t_coord)
            if magnitude > sqrt(2):    # rules out 8 cases
                direction = coord_dir(h_coord, t_coord)
                move = calc_vector_move(direction)
                t_coord = t_coord + move            
       

    elif move == 'R':
        h_coord.x += 1
        if t_coord != h_coord:  # rules out 1 case
            magnitude = coord_dist(h_coord, t_coord)
            if magnitude > sqrt(2):    # rules out 8 cases                
                direction = coord_dir(h_coord, t_coord)
                move = calc_vector_move(direction)
                t_coord = t_coord + move            

    resolve_move(visited_coord, t_coord, h_coord)

total = len(set(visited_coord))
print(f"the total number of coordinates visited at least once is {total}")
