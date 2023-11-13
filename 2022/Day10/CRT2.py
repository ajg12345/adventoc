from collections import OrderedDict
from dataclasses import dataclass
from math import sqrt
import numpy as np
from pprint import pprint



"""
the x register controls the horizontal position of a sprite

The Sprite is 3 px wide and the x register sets the hpos
    of the middle of the sprite
the crt is 40 wide and 6 high, drawn left to right 0-39

the CRT draws a single pixel during each cycle

so for example
at the start of the test case, the sprite middle is x register 1
and since at that starting cycle its trying to draw cycle 1, 
its lit

this is the idea, you can light a pixel (cycle) if the sprite is active
which depends on the register (x)

"""

file_dir = '2022/Day10/'
input_filename = file_dir + 'test.txt'
input_filename = file_dir + 'signal_ops.txt'


class CRT():
    def __init__(self):
        self.crt_screen = ['.' for i in range(240)]

    def print_screen(self):
        for line in range(6):
            pprint(''.join(self.crt_screen[line*40: (line+1)*40]))
        
    def draw(self, position):
        self.crt_screen[position] = '#'

crt = CRT()
cycles = []
for raw_line in open(input_filename, 'r'):
    line = raw_line.strip('\n')
    if line[0] != 'n':
        value = int(line.split(' ')[1])
        cycles.append(0)
        cycles.append(value)
    else:
        cycles.append(0)

x = 1
cycle_counter = 1
for cycle in cycles:
    # beginning of cycle
    # account new operation

    pixel_position = (cycle_counter - 1) % 40
    if pixel_position == x-1:
        crt.draw(cycle_counter-1)

    if pixel_position == x:
        crt.draw(cycle_counter-1)
    
    if pixel_position == x+1:
        crt.draw(cycle_counter-1)
    
    # if cycle_counter == 45:
        # pass

    # end of cycle
    x += cycle
    cycle_counter += 1

crt.print_screen()
