""" Problem Prompt

while on metal island you see everything made of metal and wander towards hot springs
you are among a field of pipes, which an animal is in
you realize that the pipes contain one large loop with an animal 'S' is in
find out what pipe in the loop is that maximum distance from the animal
and print the number of steps from animal position to that pipe

IN MY CASE, I HAVE A PIPEMAP CLASS AND A PLUMBERTWINS CLASS
I'll pretend that two plumbers are running away from the animal in both 
directions at the same "speed" and constantly for when they eventually overlap
"""
from pathlib import Path
from pprint import pprint
from dataclasses import dataclass


class PipeMap():
    def __init__(self, pipe_map: list[str]):
        self.pipe_map = pipe_map
        self.col_max = len(self.pipe_map[0])
        self.row_max = len(self.pipe_map)
        self.S_position = self.find_S()

    def find_S(self) -> (int, int):
        S_column = None
        S_row = None
        for i in range(self.row_max):
            row = self.pipe_map[i]
            S_row = i
            if -1 != row.find('S'):
                S_column = row.find('S')
                break
        return (S_row, S_column)
    
    def in_bounds(self, position: (int, int)) -> bool:
        return (0 <= position[0] < self.row_max) and (0 <= position[1] < self.col_max)


class MarioBros():
    def __init__(self, pipe_map: PipeMap):
        self.pipe_map = pipe_map.pipe_map
        self.position = pipe_map.S_position
        self.prev_position = pipe_map.S_position
        self.steps = 0

    def move(self):
        next_position = None
        current_row = self.position[0]
        current_col = self.position[1]
        prev_row = self.prev_position[0]
        prev_col = self.prev_position[1]
        pipe_map_char = self.pipe_map[current_row][current_col]
        row_diff = current_row - prev_row
        col_diff = current_col - prev_col
        if row_diff == -1: # prev moved N
            if pipe_map_char == '|':
                next_position = (current_row - 1, current_col)
            if pipe_map_char == '7':
                next_position = (current_row, current_col - 1)
            if pipe_map_char == 'F':
                next_position = (current_row, current_col + 1)
        if col_diff == 1: # prev moved E
            if pipe_map_char == '-':
                next_position = (current_row, current_col + 1)
            if pipe_map_char == '7':
                next_position = (current_row + 1, current_col)
            if pipe_map_char == 'J':
                next_position = (current_row - 1, current_col)
        if row_diff == 1: # prev moved S
            if pipe_map_char == '|':
                next_position = (current_row + 1, current_col)
            if pipe_map_char == 'J':
                next_position = (current_row, current_col - 1)
            if pipe_map_char == 'L':
                next_position = (current_row, current_col + 1)
        if col_diff == -1: # prev moved W
            if pipe_map_char == '-':
                next_position = (current_row, current_col - 1)
            if pipe_map_char == 'F':
                next_position = (current_row + 1, current_col)
            if pipe_map_char == 'L':
                next_position = (current_row - 1, current_col)
        self.prev_position = self.position
        self.position = next_position
        self.steps += 1

if __name__ == "__main__":
    
    DEBUG = False

    if DEBUG:
        input_filename = Path().absolute() / "2023" / "Day10" / "example_pipe_map.txt"
    else:
        input_filename = Path().absolute() / "2023" / "Day10" / "pipe_map.txt"

    
    max_steps_away = 0
    pipe_line_list = []
    for line in input_filename.open():
        # load the pipe_map class
        pipe_line_list.append(line.strip('\n'))
        
    pipe_map = PipeMap(pipe_line_list)
    mario = MarioBros(pipe_map)
    luigi = MarioBros(pipe_map)

    # set them on their way and increment their steps
    s = pipe_map.S_position
    route_1_start = None
    route_2_start = None
    north = (s[0] - 1, s[1])
    north_char = pipe_map.pipe_map[north[0]][north[1]]

    east = (s[0], s[1] + 1)
    east_char = pipe_map.pipe_map[east[0]][east[1]]

    south = (s[0] + 1, s[1])
    south_char = pipe_map.pipe_map[south[0]][south[1]]

    west =  (s[0], s[1] - 1)
    west_char = pipe_map.pipe_map[west[0]][west[1]]

    if north_char in ['|', 'F', '7'] and pipe_map.in_bounds(north):
        route_1_start = north
    
    if east_char in ['-', 'J', '7'] and pipe_map.in_bounds(east):
        if not route_1_start:
            route_1_start = east
        else:
            route_2_start = east
    
    if south_char in ['|', 'J', 'L'] and pipe_map.in_bounds(south):
        if not route_1_start:
            route_1_start = south
        else:
            route_2_start = south

    if west_char in ['-', 'F', 'L'] and pipe_map.in_bounds(west):
        route_2_start = west

    mario.position = route_1_start
    mario.steps = 1
    luigi.position = route_2_start
    luigi.steps = 1

    while mario.position != luigi.position:
        mario.move()
        luigi.move()
    
    max_steps_away = mario.steps
    if DEBUG:
        assert max_steps_away == 8
    print('sum_next_numbers ' + str(max_steps_away))
