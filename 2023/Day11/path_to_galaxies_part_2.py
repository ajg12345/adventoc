""" Problem Prompt
PART 2
hot springs

"""
from pathlib import Path
from copy import deepcopy
from pprint import pprint


def int_sign(x):
   if (x==0): 
       return 1
   else: 
       return (x//abs(x))

class GalaxyMap():
    def __init__(self, galaxy_map: list()):
        self.galaxy_map = galaxy_map
        self.row_max = len(galaxy_map)
        self.col_max = len(galaxy_map[0])
        self.pound_list = self.load_pound_list()
        self.distance_matrix = self.load_distance_matrix()

    def load_pound_list(self) -> list():
        pound_list = []
        for i in range(self.row_max):
            for j in range(self.col_max):
                if galaxy_map[i][j] == '#':
                    pound_list.append((i,j))
        return pound_list
    
    def pound_distance(self, a, b) -> bool:
        xdist = abs(a[0] - b[0])
        ydist =  abs(a[1] - b[1])
        return xdist + ydist

    def pound_distance_walk(self, a, b) -> bool:
        #this needs to be more of a walk and accruing distance
        row_path = []
        col_path = []
        # int_sign()
        for i in range(a[0], b[0], int_sign(b[0] - a[0]) ):
            row_path.append(self.galaxy_map[i + int_sign(b[0] - a[0])][a[1]])
        # this walk gets you to b[0], a[1]

        for i in range(a[1], b[1], int_sign(b[1] - a[1]) ):
            col_path.append(self.galaxy_map[b[0]][i + int_sign(b[1] - a[1])])

        col_path_len = len(col_path)
        row_path_len = len(row_path)
        col_path_exp = col_path.count('1')
        row_path_exp = row_path.count('1')

        if (a[0] == 2 and a[1] == 0 and b[0] == 6 and b[1] == 1):
            print('watch this')

        exp_size = 1_000_000
        total_row_path_length = row_path_len + (row_path_exp * exp_size) - (2*row_path_exp)
        total_col_path_length = col_path_len + (col_path_exp * exp_size) - (2*col_path_exp)
        path_sum = total_row_path_length + total_col_path_length
        return path_sum

    def load_distance_matrix(self):
        distance_matrix = list()
        source_pound_list = self.pound_list
        target_pound_list = deepcopy(self.pound_list)
        for s in range(len(source_pound_list)):
            distance_matrix.append([])
            for t in range(len(target_pound_list)):
                if t <= s:
                    continue
                source = source_pound_list[s]
                target = target_pound_list[t]
                distance_matrix[s].append(self.pound_distance_walk(source, target))
        return distance_matrix




if __name__ == "__main__":
    
    DEBUG = False

    if DEBUG:
        input_filename = Path().absolute() / "2023" / "Day11" / "example_galaxies.txt"
    else:
        input_filename = Path().absolute() / "2023" / "Day11" / "galaxies.txt"


    galaxy_map = []
    for line in input_filename.open():
        line = line.strip('\n')
        galaxy_line_list = [char for char in line]
        galaxy_map.append(galaxy_line_list)
    

    def is_dot_row(row_str: str) -> bool:
        for char in row_str:
            if char != '.':
                return False
        return True

    galaxy_row_max = len(galaxy_map)
    galaxy_col_max = len(galaxy_map[0])

    row_index_of_dots = []
    for i in range(galaxy_row_max):
        if is_dot_row(galaxy_map[i]):
            row_index_of_dots.append(i)

    col_index_of_dots = []
    for j in range(galaxy_col_max):
        galaxy_col_str = ''
        for i in range(galaxy_row_max):
            galaxy_col_str += galaxy_map[i][j]
        if is_dot_row(galaxy_col_str):
            col_index_of_dots.append(j)

    # modify the galaxy_map

    # modify the col inserts first by adding a single '.' in descending order
    for j in range(galaxy_col_max, 0, -1):
        galaxy_col_str = ''
        if col_index_of_dots and j == col_index_of_dots[-1]:
            col_index_of_dots.pop()
            for i in range(galaxy_row_max):
                galaxy_map[i].insert(j, '1')
    
    
    # modify the row inserts second, easily, by just adding a list of '.'s
    galaxy_col_max = len(galaxy_map[0])

    for i in range(galaxy_row_max, 0, -1):
        if row_index_of_dots and i == row_index_of_dots[-1]:
            row_index_of_dots.pop()
            galaxy_map.insert(i, ['1'] * galaxy_col_max)
    
    
    my_map = GalaxyMap(galaxy_map)
    
    shortest_path_sums = 0
    for i in range(len(my_map.distance_matrix)):
        shortest_path_sums += sum(my_map.distance_matrix[i])

    # --========galaxy_map is expanded
    # calculate the shortest distance as described

    pprint('shortest_path_sums ' + str(shortest_path_sums))
    if DEBUG:
        assert shortest_path_sums == 8410

# 8492 vs 8410  82 higher
# 1112 vs 1030  82 higher (always?)