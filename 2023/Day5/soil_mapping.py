""" Problem Prompt
need sand to filter water?
get on the ferry to get more sand
while you wait, help with food prod problem
There is an Island Island almanac (input)

it lists all of seeds to plant, and soil with each seen and fertilizer with each soil, and water with each fertilizer
seed -> soil -> fertilizer -> water -> light -> temp -> humidity -> location

each line within a map section of the almanac contains 3 numbers, destination range start, source range start and range length
destination, source, range length
and anything not covered by the map endsup the same as previous

translate all of those seeds to their eventual location and find the lowest location number.

PART 2

"""
from pathlib import Path

#YOU MUST ADD BLANK LINE TO END OF INPUT FILE FOR THIS TO WORK (SHORTCUT)

class Mapping:
    def __init__(self, destination_start: int, source_start: int, range_length: int):
        self.destination_start = destination_start
        self.source_start = source_start
        self.range_length = range_length

        self.source_range = (source_start, source_start + range_length)


class Mapping_group:
    def __init__(self, name: str):
        self.name = name
        self.mapping_list = list()

    
    def map_io(self, input: int):
        for mapping in self.mapping_list:
            if mapping.source_range[0] <= input <= mapping.source_range[1]:
                distance = input - mapping.source_range[0]
                return mapping.destination_start + distance
        return input

if __name__ == "__main__":
    input_filename = Path().absolute() / "2023" / "Day5" / "almanac.txt"

    seeds = []
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
            seeds = [int(seed) for seed in line.split(': ')[1].split()]
        elif line in map_names:
            current_map_group = Mapping_group(line)
            map_group_list.append(current_map_group)
        else:
            dest = int(line.split()[0])
            source = int(line.split()[1])
            range = int(line.split()[2])
            current_map_group.mapping_list.append(Mapping(dest, source, range))

    # run the seeds through the mappings in order
    processed_seeds = []
    for seed in seeds:
        if seed == 13:
            print(seed)
        new_seed_value = seed
        
        for group in map_group_list:
            new_seed_value = group.map_io(new_seed_value)
        processed_seeds.append(new_seed_value)

    lowest_location = min(processed_seeds)
    print(lowest_location)
