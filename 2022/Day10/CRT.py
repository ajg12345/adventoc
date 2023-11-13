from collections import OrderedDict
from dataclasses import dataclass
from math import sqrt
import numpy as np
from pprint import pprint



"""
must replace aCRT and its precise clock circuit
figure out the signal sent to the CPU
CPU has single register X intialized with 1
supports 2 instructions
addx V
    takes 2 cyc to complete, a fter which the x register is increased by the value V
noop
    takes 1 cycle to complete has no affect

instructions are puzzle input
example:

noop
addx 3
addx -5

c1: x is 1, noop starts and finishes
c2: x is 1, addx 3 begins
c3: x is still 1, addx 3 finishes
c4: x is 4, addx -5 begins
c5: x is 4, addx -5 finishes 
c6: x is 1

signal strength is cycle number ultiplied by the value of the x register
look DURING the 20th cycle and every 40 cycles after that

in test.txt the sum of the sig str during 20, 60 100 140 180 220 is 13140

"""

file_dir = '2022/Day10/'
input_filename = file_dir + 'test.txt'
input_filename = file_dir + 'signal_ops.txt'

cycles = []
for raw_line in open(input_filename, 'r'):
    line = raw_line.strip('\n')
    if line[0] != 'n':
        operation = line.split(' ')[0]
        value = int(line.split(' ')[1])
        cycles.append(0)
        cycles.append(value)
    else:
        cycles.append(0)

x = 1
cycle_counter = 1
partial_sums = 0
important_cycles = [20, 60, 100, 140, 180, 220]
for cycle in cycles:
    # beginning of cycle
    # account new operation

    # mid cycle
    if cycle_counter in important_cycles:
        partial_sums += (x * cycle_counter)
    
    # end of cycle
    x += cycle
    cycle_counter += 1

print(f"The sum of these signal strengths is {partial_sums}")
