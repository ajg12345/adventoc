""" Problem Prompt

Part 2
its like before but instead of walking on the loop,
you are searching for the number of tiles which are enclosed by the loop
and counting those tiles up! (this is nuts)


CURRENT STATUS
MY TECHNIQUE WORKS FOR THE TOY EXAMPLE OF example_pipe_map3.txt
but fails for the prompt example of example_pipe_map2.txt
and this is likely because of the bug mentioned on line 68
"""
from pathlib import Path
from copy import deepcopy
from pprint import pprint

class PipeMap():
    def __init__(self, pipe_map: list[str]):
        self.pipe_map = pipe_map
        
        
        self.col_max = len(self.pipe_map[0])
        self.row_max = len(self.pipe_map)
        # matrix the size of the pipe_map of zeros
        # used to label which characters are actual path variables while moving along
        self.pipe_map_path_only = self.set_zeros()

        # copy of matrix to be combined with path_only and produce something to analyze
        self.pipe_map_scratch = deepcopy(pipe_map)
        self.S_position = self.find_S()

    def set_zeros(self):
        return_list = []
        for i in range(self.row_max):
            return_list.append([0] * self.col_max)
        return return_list

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
        self.col_max = len(self.pipe_map[0])
        self.row_max = len(self.pipe_map)
        self.pipe_map_path_only = pipe_map.pipe_map_path_only
        self.pipe_map_scratch = [list(s) for s in pipe_map.pipe_map_scratch]
        self.position = pipe_map.S_position
        self.prev_position = pipe_map.S_position
        self.steps = 0
        self.enclosed_count = 0

    def record_contained_cells(self, direction):
        # make a list of lists of positions of these . chars, grouped by path crossings
        # this might have a bug related to when a wall is like F--J looking east for instance
        # if the number of groups is odd, then the group sequence is in out in out
        # if the number of groups is even then the group sequence is out in out in
        dots_in_path_crossing_groups_str = ''
        position_list = []
        # I need to add code to this part to use a stack to store JF or L7 pairs and | turning into a single '|'
        # and store J7 or LF pairs and | turning into a single ''
        # and if there is a 7 or a F without a stack element, ignore
        if direction == 'north':
            for i in range(self.position[0], 0, -1):
                value = self.pipe_map_scratch[i][self.position[1]]
                position = (i, self.position[1])
                position_list.append(position)
                if value in ['.']:
                    dots_in_path_crossing_groups_str += value
                elif value in ['-']:
                    dots_in_path_crossing_groups_str += '|'
        # I need to add code to this part to use a stack to store FJ or L7 pairs and - turning into a single '|'
        # and store F7 or LJ pairs and - turning into a single ''
        # and if there is a 7 or J without a stack element, ignore
        elif direction == 'east':
            for i in range(self.position[1], self.col_max): # make sure that this doesnt crap out
                value = self.pipe_map_scratch[self.position[0]][i]
                position = (self.position[0], i)
                position_list.append(position)
                if value in ['.']:
                    dots_in_path_crossing_groups_str += value
                elif value in ['|']:
                    dots_in_path_crossing_groups_str += '|'
        # I need to add code to this part to use a stack to store FJ or 7L pairs and | turning into a single '|'
        # and store FL or 7J pairs and - turning into a single ''
        # and if there is a J or L without a stack element, ignore
        elif direction == 'south':
            for i in range(self.position[0], self.row_max): # make sure that this doesnt crap out
                value = self.pipe_map_scratch[i][self.position[1]]
                position = (i, self.position[1])
                position_list.append(position)
                if value in ['.']:
                    dots_in_path_crossing_groups_str += value
                elif value in ['-']:
                    dots_in_path_crossing_groups_str += '|'
        # I need to add code to this part to use a stack to store 7L or J F pairs and | turning into a single '|'
        # and store 7F or JL pairs and - turning into a single ''
        # and if there is a F or L without a stack element, ignore
        else:
            for i in range(self.position[0], 0, -1): # make sure that this doesnt crap out
                value = self.pipe_map_scratch[self.position[0]][i]
                position = (self.position[0], i)
                position_list.append(position)
                if value in ['.']:
                    dots_in_path_crossing_groups_str += value
                elif value in ['|']:
                    dots_in_path_crossing_groups_str += '|'

        # count them up in groups acc to in vs out
        if dots_in_path_crossing_groups_str.count('|') % 2 != 0: # odd
            ingroup = True
        else: 
            ingroup = False
        for value in dots_in_path_crossing_groups_str:
            position = position_list.pop(0)
            if ingroup and value == '.':
                self.pipe_map_path_only[position[0]][position[1]] = 2
            else:
                ingroup = not ingroup

    def count_contained_cells(self):
        total = 0
        for row in self.pipe_map_path_only:
            for cell in row:
                if cell == 2:
                    total += 1
        return total

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
    
    DEBUG = True

    if DEBUG:
        input_filename = Path().absolute() / "2023" / "Day10" / "example_pipe_map2.txt"
    else:
        input_filename = Path().absolute() / "2023" / "Day10" / "pipe_map.txt"

    
    max_steps_away = 0
    pipe_line_list = []
    for line in input_filename.open():
        # load the pipe_map class
        pipe_line_list.append(line.strip('\n'))
        
    pipe_map = PipeMap(pipe_line_list)
    mario = MarioBros(pipe_map)

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

    # figure out the "real" S character for calculating in/out later on:
    S_char = ''
    if route_1_start in [north, south] and route_2_start in [north, south]:
        S_char = '|'
    if route_1_start in [east, west] and route_2_start in [east, west]:
        S_char = '-'
    if route_1_start in [east, north] and route_2_start in [east, north]:
        S_char = 'L'
    if route_1_start in [west, north] and route_2_start in [west, north]:
        S_char = 'J'
    if route_1_start in [east, south] and route_2_start in [east, south]:
        S_char = 'F'
    if route_1_start in [west, south] and route_2_start in [west, south]:
        S_char = '7'
    row_temp = mario.pipe_map_scratch[s[0]]


    # create and fill the pipe_map path only by walking the path with mario until he gets to S again
    mario.pipe_map_path_only[mario.position[0]][mario.position[1]] = 1
    mario.position = route_1_start
    while mario.position != s:
        # marking the actual path as 1 otherwise 0
        mario.pipe_map_path_only[mario.position[0]][mario.position[1]] = 1
        mario.move()
    
    # create a scratch pipe map which is the path values or .
    for i in range(len(mario.pipe_map_path_only)):
        for j in (range(len(mario.pipe_map_path_only[0]))):
            value = mario.pipe_map_path_only[i][j]
            if value:
                continue
            else:
                mario.pipe_map_scratch[i][j] = '.'
                
    mario.position = route_1_start
    # then walk the path again with mario, but at every step look N, E, S, W and 
    while mario.position != s:
        mario.move()
        mario.record_contained_cells('north')
        mario.record_contained_cells('east')
        mario.record_contained_cells('south')
        mario.record_contained_cells('west')

    total_contained_cells = mario.count_contained_cells()
    
    pprint(mario.pipe_map_path_only)
    pprint(mario.pipe_map_scratch)

    if DEBUG:
        assert total_contained_cells == 8
    print('total_contained_cells ' + str(total_contained_cells))
