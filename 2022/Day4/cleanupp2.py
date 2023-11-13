"""
Every elf has an ID number so they can divide and conquer the cleanup effort.
some overlap.
find the number which overlap at all

6-34,9-89
13-77,12-76
18-81,17-81
2-34,2-33
17-92,20-93
    24-89,7-11
    7-11,24-89
6-49,27-49
17-69,16-69
34-57,35-58
71-76,73-87
69-72,70-72
30-70,29-69
48-85,52-84
14-69,13-15
2-61,3-70
17-86,17-85
7-98,8-98
8-93,12-94
16-35,35-49

Total of 2 assignment pair overlaps at all.
"""


def process_assignment_record(line):
    first_elf = line.split(',')[0]
    second_elf = line.split(',')[1]
    return {'elf1': [int(first_elf.split('-')[0]), int(first_elf.split('-')[1])],
            'elf2': [int(second_elf.split('-')[0]), int(second_elf.split('-')[1])]}


file_dir = '2022/Day4/'
input_filename = file_dir + 'test2.txt'
input_filename = file_dir + 'assignments.txt'
overlapped_count = 0

for line in open(input_filename, 'r'):
    """
        if pair['elf1'][0] <= pair['elf2'][0] and pair['elf2'][1] <= pair['elf1'][1]:
            overlapped_count += 1
            continue
        if pair['elf2'][0] <= pair['elf1'][0] and pair['elf1'][1] >= pair['elf2'][1]:
            overlapped_count += 1
            continue
        if pair['elf1'][0] >= pair['elf2'][0] and pair['elf1'][1] <= pair['elf2'][1]:
            overlapped_count += 1
            continue
        if pair['elf1'][0] <= pair['elf2'][0] and pair['elf1'][1] >= pair['elf2'][1]:
            overlapped_count += 1
    """
    pair = process_assignment_record(line)
    if pair['elf1'][1] >= pair['elf2'][0] and pair['elf1'][0] <= pair['elf2'][1]:
        overlapped_count += 1
        continue
    if pair['elf2'][1] >= pair['elf1'][0] and pair['elf2'][0] <= pair['elf1'][1]:
        overlapped_count += 1
        continue
    if pair['elf2'][0] == pair['elf1'][0] or pair['elf1'][1] == pair['elf2'][1]:
        overlapped_count += 1

print(f"The total letter priority is {str(overlapped_count)}")
