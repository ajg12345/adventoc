from collections import OrderedDict
from dataclasses import dataclass
from math import sqrt
import numpy as np
from pprint import pprint



"""
bridge snaps
elves are ok
lets map rope physics to avoid falling through
consider a rope with head and ten segments including a tail 

again heres a sample input of head movement:
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20

the positions visited of the tail is 36
"""

file_dir = '2022/Day9/'
input_filename = file_dir + 'test3.txt'
# input_filename = file_dir + 'test4.txt'
# input_filename = file_dir + 'series_of_motions.txt'

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

def record_coord(visited_coord, rope):
    visited_coord.append( (rope['9'].get_value()) )

def move_follow_from_lead(move, rope, name, rope_order):
    h_coord = rope[name]
    if name == '9':
        t_coord = h_coord
    else:
        t_coord = rope[rope_order[name]]
    if not move:
        return None
    rope[name] = h_coord + move
    h_coord = rope[name]
    if t_coord != h_coord:  # rules out 1 case where they are equal
        magnitude = coord_dist(h_coord, t_coord)
        if magnitude > sqrt(2):    # rules out 8 cases
            direction = coord_dir(h_coord, t_coord)
            return calc_vector_move(direction)
        else:
            return None
    else:
        return None

raw_moves = []
for line in open(input_filename, 'r'):
    raw_moves.extend(parse_line(line.strip('\n')))

translation = {'U': XYPair(0,1), 'D': XYPair(0,-1), 'L': XYPair(-1,0), 'R': XYPair(1,0)}
head_moves = [translation[m] for m in raw_moves]

rope = OrderedDict({'H': XYPair(0, 0),
                    '1': XYPair(0, 0),
                    '2': XYPair(0, 0),
                    '3': XYPair(0, 0),
                    '4': XYPair(0, 0),
                    '5': XYPair(0, 0),
                    '6': XYPair(0, 0),
                    '7': XYPair(0, 0),
                    '8': XYPair(0, 0),
                    '9': XYPair(0, 0)})
rope_order = {  'H':'1',
                '1':'2',
                '2':'3',
                '3':'4',
                '4':'5',
                '5':'6',
                '6':'7',
                '7':'8',
                '8':'9',
                '9': None}
visited_coord = []
for m in head_moves:
    move = m
    for name, coord in rope.items():
        if name == '9':
            move_follow_from_lead(move, rope, name, rope_order)
            record_coord(visited_coord, rope)
        else:
            move = move_follow_from_lead(move, rope, name, rope_order)
    pprint(rope)
total = len(set(visited_coord))
print(f"the total number of coordinates visited by 9 at least once is {total}")
