from collections import Counter
"""
Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two
compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need
your help finding the errors. Every item type is identified by a single lowercase or uppercase letter
(that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always
has the same number of items in each of its two compartments, so the first half of the characters represent
items in the first compartment, while the second half of the characters represent items in the
second compartment.

Basically, split each line in half, find the character that appears in both, and sum up the priority of all
of these error "items"
(Its priority is the alphabetical order value:
Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.)
the test file input should be 157
"""


def calc_priority(item_letter):
    upper_value = 26 if item_letter.isupper() else 0
    alpha_conversion_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
        'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    return alpha_conversion_values[item_letter.lower()] + upper_value


file_dir = '2022/Day3/'
input_filename = file_dir + 'contents.txt'
priority_sum = 0

for line in open(input_filename, 'r'):
    length_of_line = len(line)
    first_half = line[0:length_of_line]
    mid_length = int(length_of_line / 2)
    second_half = line[mid_length:length_of_line]
    first_letter_counter = Counter(first_half)
    second_letter_counter = Counter(second_half)
    item_letter = list((first_letter_counter & second_letter_counter).keys())[0]

    priority_sum += calc_priority(item_letter)

print(f"The total letter priority is {str(priority_sum)}")
