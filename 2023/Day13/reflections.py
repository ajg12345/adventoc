""" Problem Prompt
PART 2
hot springs are damaged
condition record (input)descibes the condition of each of them
but its also missing information
Either online . damaged # or unknown ?

and there are numbers to describe the groupsize of contiguous online springs 

--solution idea:
now that I have a 

"""
from pathlib import Path
from copy import deepcopy
from pprint import pprint


class ashRockMap:
    def __init__(self, ash_rock_strings: [str]):
        self.row_ash_rock_strings = ash_rock_strings
        self.ar_map = self.build_ar_map()
        self.col_ash_rock_strings = self.flip()
        
        self.col_reflection_index = None
        self.row_reflection_index = None

        self.col_reflection_index2 = None
        self.row_reflection_index2 = None

    def flip(self) -> list():
        return_list = list()
        row_length = len(self.ar_map[0])
        col_height = len(self.ar_map)
        for j in range(row_length):
            new_string = ''
            for i in range(col_height):
                new_string += self.ar_map[i][j]
            return_list.append(new_string)
        return return_list

    def build_ar_map(self) -> list():
        return_map = []
        for s in self.row_ash_rock_strings:
            return_map.append([c for c in s])
        return return_map
    
    def get_reflection_value(self) -> int:
        return self.row_reflection_index*100 if self.row_reflection_index else self.col_reflection_index
        
    def find_reflection(self) -> None:
        row_reflection = self.find_row_reflection()
        if row_reflection > 0:
            self.row_reflection_index = row_reflection
        else:
            col_reflection = self.find_col_reflection()
            self.col_reflection_index = col_reflection

    def find_row_reflection(self) -> int:
        #look for reflection in the row_ash_rock_strings
        row_max = len(self.row_ash_rock_strings)
        for i in range(row_max-1):
            found_reflection = True
            pre_reflection_list = self.row_ash_rock_strings[i::-1]
            post_reflection_list = self.row_ash_rock_strings[i+1::]
            if len(pre_reflection_list) >= len(post_reflection_list):
                for j in range(len(post_reflection_list)):
                    if pre_reflection_list[j] != post_reflection_list[j]:
                        found_reflection = False
                        break
            else:
                for j in range(len(pre_reflection_list)):
                    if pre_reflection_list[j] != post_reflection_list[j]:
                        found_reflection = False
                        break
            if found_reflection:
                return i+1
        return -1

    def find_col_reflection(self) -> int:
        #look for reflection in the col_ash_rock_strings
        col_max = len(self.col_ash_rock_strings)
        for i in range(col_max-1):
            found_reflection = True
            pre_reflection_list = self.col_ash_rock_strings[i::-1]
            post_reflection_list = self.col_ash_rock_strings[i+1::]
            if len(pre_reflection_list) >= len(post_reflection_list):
                for j in range(len(post_reflection_list)):
                    if pre_reflection_list[j] != post_reflection_list[j]:
                        found_reflection = False
                        break
            else:
                for j in range(len(pre_reflection_list)):
                    if pre_reflection_list[j] != post_reflection_list[j]:
                        found_reflection = False
                        break
            if found_reflection:
                return i+1
        return -1

if __name__ == "__main__":
    
    DEBUG = False

    if DEBUG:
        input_filename = Path().absolute() / "2023" / "Day13" / "example_ash_and_rocks.txt"
    else:
        input_filename = Path().absolute() / "2023" / "Day13" / "ash_and_rocks.txt"

    ash_rock_strings = list()
    ar_map_list = list()
    for line in input_filename.open():
        if line == '\n':
            ar_map_list.append(ashRockMap(ash_rock_strings))
            ash_rock_strings = list()
        else:
            ash_rock_strings.append(line.strip('\n'))

    ar_map_list.append(ashRockMap(ash_rock_strings))
    ash_rock_strings = list()

    col_100row_total = 0
    for m in ar_map_list:
        m.find_reflection()
        col_100row_total += m.get_reflection_value()

    pprint('col_100row_total ' + str(col_100row_total))
    if DEBUG:
        assert col_100row_total == 405