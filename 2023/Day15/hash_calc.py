""" Problem Prompt
Gotta tilt and calculate the stress on the members
rocks will roll but not past a square thing

"""
from pathlib import Path
from pprint import pprint


if __name__ == "__main__":
    
    DEBUG = True

    if DEBUG:
        input_filename = Path().absolute() / "2023" / "Day15" / "example_hash.txt"
    else:
        input_filename = Path().absolute() / "2023" / "Day15" / "hash.txt"

    
    for line in input_filename.open():
        pass

    results_sum = 0
    pprint('results_sum ' + str(results_sum))
    if DEBUG:
        assert results_sum == 1320