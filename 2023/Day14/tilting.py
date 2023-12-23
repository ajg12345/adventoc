""" Problem Prompt
Gotta tilt and calculate the stress on the members
rocks will roll but not past a square thing

"""
from pathlib import Path
from pprint import pprint


if __name__ == "__main__":
    
    DEBUG = True

    if DEBUG:
        input_filename = Path().absolute() / "2023" / "Day14" / "example_rocks.txt"
    else:
        input_filename = Path().absolute() / "2023" / "Day14" / "rocks.txt"

    
    for line in input_filename.open():
        pass

    load = 0
    pprint('load ' + str(load))
    if DEBUG:
        assert load == 136