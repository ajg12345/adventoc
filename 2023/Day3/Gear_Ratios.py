""" Problem Prompt
need to go up a gondola lift, but its broken
greasy the elf can't fix it, needs helpengine part is missing
just add up all the parts numbers in the schematic.txt to find out whats missing

any number adjacent to a symbol even diagonally, is a part number and show be included in your sum
periods do not count
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


def check_if_symbol_near_number(schematic, istart, jstart, jend, imax, jmax):
    # generate a box of characters surrounding the number and check for any symbols anywhere within
    for i in range(istart - 1, istart + 2):
        if 0 <= i < imax:
            for j in range(jstart - 1, jend + 2):
                if 0 <= j < jmax:
                    schematic_neighbor = schematic[i][j]
                    if (not schematic_neighbor.isalnum()) and (
                        schematic_neighbor not in [".", "\n"]
                    ):
                        return True
    return False


if __name__ == "__main__":
    schematic = list()
    input_filename = Path().absolute() / "2023" / "Day3" / "schematic.txt"
    load_schematic(schematic, input_filename)
    imax = len(schematic)
    jmax = len(schematic[0]) - 1
    part_number_sum = 0
    for i in range(imax):
        j = 0
        while j < jmax:
            ij_character = schematic[i][j]
            if ij_character.isdigit():
                jend, jvalue = get_entire_number(schematic[i], j, jmax)

                if check_if_symbol_near_number(schematic, i, j, jend, imax, jmax):
                    part_number_sum += jvalue

                j = jend + 1
            else:
                j += 1

    print(part_number_sum)
