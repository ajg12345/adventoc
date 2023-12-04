""" Problem Prompt
need to go up a gondola lift, but its broken
greasy the elf can't fix it, needs helpengine part is missing
just add up all the parts numbers in the schematic.txt to find out whats missing

Now just focus on the "gear" which is '*' adjacent to exactly 2 part numbers
in that case, multiply them together. SO do that to each gear and add up all of those
numbers.
"""
from pathlib import Path
from pprint import pprint


def load_schematic(schematic, filename: str):
    for line in filename.open():
        schematic.append(line)


def get_entire_number(schematic_row: str, jpos: int, jmax: int):
    jend = 0
    jvalue_str = ""
    for j in range(jpos, jmax):
        if schematic_row[j].isdigit():
            jvalue_str += schematic_row[j]
            jend = j
        else:
            break
    jvalue = int(jvalue_str)
    return jend, jvalue


def touching(number, asterisk):
    return (number[1] - 1 <= asterisk[0] <= number[1] + 1) and (
        number[2] - 1 <= asterisk[1] <= number[3] + 1
    )


if __name__ == "__main__":
    schematic = list()
    input_filename = Path().absolute() / "2023" / "Day3" / "schematic.txt"
    load_schematic(schematic, input_filename)
    imax = len(schematic)
    jmax = len(schematic[0]) - 1
    gear_number_sum = 0

    asterisks = list()  # list of just asterisk positions tuples (i,j)
    numbers = list()  # list of numbers (values, ipos, jstart, jend)
    for i in range(imax):
        j = 0
        while j < jmax:
            if schematic[i][j].isdigit():
                jend, jvalue = get_entire_number(schematic[i], j, jmax)
                numbers.append((jvalue, i, j, jend))
                j = jend + 1
                continue
            if schematic[i][j] == "*":
                asterisks.append((i, j))
            j += 1

    for a in asterisks:
        adjacent_numbers = list()

        # identify if the asterisk touches exactly 2 numbers
        for n in numbers:
            if touching(n, a):
                adjacent_numbers.append(n)
        # and if so, store those values in the gear values total and set is_gear to True
        if len(adjacent_numbers) == 2:
            first_number = adjacent_numbers.pop()
            second_number = adjacent_numbers.pop()
            gear_number_sum += first_number[0] * second_number[0]

    print(gear_number_sum)
