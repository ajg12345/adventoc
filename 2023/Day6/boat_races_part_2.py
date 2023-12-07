""" Problem Prompt
boat races to win a trip to Desert Island
you get a time, and have to travel the farthest
you get a timing_sheet as input, with other racers distance records.
boats are toy boats with charge buttons that are charged and released
only hold button at start of race, and boats dont move until button is released

you must beat every race (longer distance in the same amount of time)
there are many discrete values of "hold down time"
figure out the totla number of these, and then multiply the total number of these together
that total is the amount to win
"""
from pathlib import Path
import math


class Race():
    def __init__(self, time: int, distance: int):
        self.time = time
        self.distance = distance
        self.win_hold_count = self.find_hold_range()
        

    def find_hold_range(self) -> int:
        if self.distance == 200:
            print("..")
        inner_term = math.sqrt(self.time**2 - 4*self.distance)
        pos_inner = inner_term
        neg_inner = -1*inner_term
        max_hold = ((-1*self.time) + neg_inner)/-2
        min_hold = ((-1*self.time) + pos_inner)/-2 + 0.0000000001
        ways = len(range(math.ceil(min_hold), math.ceil(max_hold), 1))
        return ways
        # return math.floor(max_hold) - math.ceil(min_hold) + 1

if __name__ == "__main__":
    
    input_filename = Path().absolute() / "2023" / "Day6" / "race_list.txt"

    time = 0
    distance = 0
    races = list()
    for line in input_filename.open():
        line_list = line.strip('\n').split()
        line_list.pop(0)
        if not time:
            number = ''.join(line_list)
            time = int(number)
            continue
        if not distance:
            number = ''.join(line_list)
            distance =  int(number)
            break
    race = Race(time, distance)
    
    total_ways_to_win_product = race.win_hold_count
    
    print('total_ways_to_win_product ' + str(total_ways_to_win_product))
