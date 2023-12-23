""" Problem Prompt
PART 2
there is a smudge, basically brute force every option until you find it

and important thing to think about is that there are plenty
of ways that the ar_map can change by one value and still generate the 
original reflection point, and that reflection point must be ignored
in the final calculation

not sure whats happening here, its passing all of the example
calculations, but not the main big one...

my print statements aren't working (i,j) and there's something weird about 
the third real example...
"""
from pathlib import Path
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

    def print_original_reflection(self) -> None:
        if self.col_reflection_index and self.col_reflection_index > 0:
            pprint('original reflection is col '+ str(self.col_reflection_index))
        else:
            pprint('original reflection is row '+ str(self.row_reflection_index))
            
    def print_new_reflection(self) -> None:
        if self.col_reflection_index2 and self.col_reflection_index2 > 0:
            pprint('new reflection is col '+ str(self.col_reflection_index2))
        else:
            pprint('new reflection is row '+ str(self.row_reflection_index2))
        

    def check_if_found_new(self) -> bool:
        colfound = (self.col_reflection_index2 and self.col_reflection_index2 >= 0)
        rowfound = (self.row_reflection_index2 and self.row_reflection_index2 >= 0)
        if colfound:
            return (self.col_reflection_index2 != self.col_reflection_index)

        if rowfound:
            return (self.row_reflection_index != self.row_reflection_index2)
        return False

    def regenerate_row_strings(self) -> None:
        # use modified ar_map to regenerate row_ash_rock_strings
        new_row_strings = []
        for row in self.ar_map:
            new_row_strings.append(''.join(row))
        self.row_ash_rock_strings = new_row_strings
    
    def switch_and_regenerate(self, i: int, j: int) -> None:
        old_char = self.ar_map[i][j]
        self.ar_map[i][j] = '#' if old_char == '.' else '.'
        self.regenerate_row_strings()
        self.col_ash_rock_strings = self.flip()

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
        return self.row_reflection_index2*100 if self.row_reflection_index2 and self.row_reflection_index2 >0  else self.col_reflection_index2
        
    def find_original_reflection(self) -> None:
        row_reflection = self.find_row_reflection()
        if row_reflection > 0:
            self.row_reflection_index = row_reflection
        else:
            col_reflection = self.find_col_reflection()
            self.col_reflection_index = col_reflection
    
    def find_reflection(self) -> None:
        row_reflection = self.find_row_reflection()
        if row_reflection > 0 and row_reflection != self.row_reflection_index:
            self.row_reflection_index2 = row_reflection
        col_reflection = self.find_col_reflection()
        if col_reflection > 0 and col_reflection != self.col_reflection_index:
            self.col_reflection_index2 = col_reflection

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
    
    DEBUG = True

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
    ar_map_count = 0
    for m in ar_map_list:
        ar_map_count += 1
        pprint("checking " + str(ar_map_count))
        next_map = False
        m.find_original_reflection()
        row_length = len(m.ar_map)
        col_length = len(m.ar_map[0])
        for i in range(row_length):
            if next_map:
                break
            for j in range(col_length):
                m.switch_and_regenerate(i,j)
                m.find_reflection()
                if m.check_if_found_new():
                    col_100row_total += m.get_reflection_value()
                    next_map = True
                    m.switch_and_regenerate(i,j)
                    m.print_original_reflection()
                    m.print_new_reflection()
                    print('i,j smudge is ' + str(i) + ',' + str(j))
                    pprint(m.row_ash_rock_strings)
                    break
                m.switch_and_regenerate(i,j)

    pprint('col_100row_total ' + str(col_100row_total))
    if DEBUG:
        assert col_100row_total == 400