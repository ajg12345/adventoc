""" Problem Prompt

PART 2
seeds actually describes ranges of seeds numbers
the seeds numbers come in pairs, start and length

"""
from pathlib import Path
from functools import cache

#YOU MUST ADD BLANK LINE TO END OF INPUT FILE FOR THIS TO WORK (SHORTCUT)

# run the numbers backwards through this (0 -> inf) until you hit a number in the seed set, then stop
# calculate a sorted list of number ranges based on the seed expressions to iterate through after its fully reverse mapped

class Mapping:
    def __init__(self, destination_start: int, source_start: int, range_length: int):
        self.destination_start = destination_start
        self.source_start = source_start
        self.range_length = range_length

        self.source_range = (source_start, source_start + range_length)
        self.destination_range = (destination_start, destination_start + range_length)


class Mapping_group:
    def __init__(self, name: str):
        self.name = name
        self.mapping_list = list()

class Almanac:
    def __init__(self, mapping_groups: list()):
        self.mapping_groups = mapping_groups

    def map_io(self, input: int) -> int:
        for group in self.mapping_groups[::-1]:
            for mapping in group.mapping_list:
                if mapping.destination_range[0] <= input <= mapping.destination_range[1]:
                    distance = input - mapping.destination_range[0]
                    input = mapping.source_start + distance
                    break
        return input

def load_seeds(line: str) -> list():
    seed_numbers = [int(seed) for seed in line.split(': ')[1].split()]
    seed_pairs = list()
    first_seed = seed_numbers.pop(0)
    second_seed = 0
    for seed in seed_numbers:
        if first_seed != 0 and second_seed == 0:
            second_seed = seed
            seed_pairs.append((first_seed, second_seed))
            first_seed = 0
            second_seed = 0
        elif first_seed == 0 and second_seed == 0:
            first_seed = seed
    return seed_pairs


if __name__ == "__main__":
    #input_filename = Path().absolute() / "2023" / "Day5" / "example_almanac.txt"
    input_filename = Path().absolute() / "2023" / "Day5" / "almanac.txt"

    seed_pairs = []
    
    map_names = ['seed-to-soil map:',
                'soil-to-fertilizer map:',
                'fertilizer-to-water map:',
                'water-to-light map:',
                'light-to-temperature map:',
                'temperature-to-humidity map:',
                'humidity-to-location map:']

    current_map_group = None
    map_group_list = list()

    # build mapping groups full of mapping objects
    for line in input_filename.open():
        line = line.strip('\n')
        if not line:
            continue
        elif line.split(': ')[0] == 'seeds':
            seed_pairs = load_seeds(line)
        elif line in map_names:
            current_map_group = Mapping_group(line)
            map_group_list.append(current_map_group)
        else:
            dest = int(line.split()[0])
            source = int(line.split()[1])
            range_length = int(line.split()[2])
            current_map_group.mapping_list.append(Mapping(dest, source, range_length))
    
    my_almanac = Almanac(map_group_list)

    min_processed_seed = 0
    first_seed = True
    seed_pairs_processed = []

    for pair in seed_pairs:
        start = pair[0]
        stop = pair[1] + pair[0]
        seed_pairs_processed.append((start, stop))

    attempt_size = 20_283_900
    #attempt_size = 100    # example version

    sorted_pairs = sorted(seed_pairs_processed, key=lambda x: x[0])
    final_locations = [x for x in range(10283800, attempt_size)] #possible 20283861
    final = [x for x in range(3,10)]

    #final_locations = [x for x in range(attempt_size)]  #example version
    best_minimum_location = 0
    for location in final_locations:
        if location % 10_000 == 0:
            print('checked ' + str(location // 10_000) + '0_000 records...')
        if best_minimum_location > 0:
            break
        seed = my_almanac.map_io(location)
        for pair in sorted_pairs:
            if pair[0] <= seed <= pair[1]:
                best_minimum_location = location
                break
            elif seed < pair[0]:
                # no need to check further (optimization)
                break

    if best_minimum_location == 0:
        print('no good location found in ' + str(attempt_size))
    else:
        print('best_minimum_location ' + str(best_minimum_location))


