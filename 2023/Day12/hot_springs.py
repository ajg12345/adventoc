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


class Record():
    def __init__(self, line: str):
        self.springs_init = list(line.strip('\n').split()[0])
        self.groupsizes = ((line.strip('\n')).split()[1]).split(',')
        self.total_working = sum(self.groupsizes)
        self.total_broken = len(self.springs_init) - self.total_working
        self.total_questions = self.springs_init.count('?')
        self.missing_working = self.total_working - self.springs_init.count('#')
        self.missing_broken = self.total_broken - self.springs_init.count('.')

    def _is_valid_grouping(self, poss_springs: list()):
        for i in range(len(self.springs_init)):
            source_pos = self.springs_init[i]
            target_pos = poss_springs[i]
            if source_pos != '?' and (source_pos != target_pos):
                return False
        return True
    
    def _is_valid_count(self, poss_springs: list()):
        return poss_springs.count('#') == sum(self.groupsizes)
    
    def _is_valid(self, poss_springs: list()):
        return self._is_valid_count(poss_springs) and self._is_valid_grouping(poss_springs)

if __name__ == "__main__":
    
    DEBUG = True

    if DEBUG:
        input_filename = Path().absolute() / "2023" / "Day12" / "example_condition.txt"
    else:
        input_filename = Path().absolute() / "2023" / "Day12" / "condition.txt"

    possible_arrangement_count = 0
    record_list = list()
    for line in input_filename.open():
        record_list.append(Record(line))
        my_record = record_list[-1]
        # brute force some high number of possible combinations of poss_springs
        
        # check each against is_valid()






    pprint('possible_arrangement_count ' + str(possible_arrangement_count))
    if DEBUG:
        assert possible_arrangement_count == 21