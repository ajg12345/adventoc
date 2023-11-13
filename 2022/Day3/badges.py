from collections import Counter
"""
Each rucksack has a badge. Identify the badge by finding the item which corresponds to the common item in three consecutive lines of text. 

"""


def calc_priority(item_letter):
    upper_value = 26 if item_letter.isupper() else 0
    alpha_conversion_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
        'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    return alpha_conversion_values[item_letter.lower()] + upper_value


file_dir = '2022/Day3/'
input_filename = file_dir + 'contents.txt'
# input_filename = file_dir + 'test.txt'
priority_sum = 0
line_number = 1
rucksack_group = list()
for line in open(input_filename, 'r'):
    rucksack_group.append(Counter(line))
    if line_number % 3 == 0:
        badge_letter_counter = rucksack_group[0] & rucksack_group[1] & rucksack_group[2]
        badge_letter = list(badge_letter_counter.keys())[0]
        priority_sum += calc_priority(badge_letter)
        rucksack_group = list()
    line_number += 1

print(f"The sum of badge priority is {str(priority_sum)}")
