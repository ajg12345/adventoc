"""
Every elf has an ID number so they can divide and conquer the cleanup effort.
some overlap.
find the number which completely overlap

75-76,18-75
2-54,1-50
82-83,78-82
13-37,37-75
79-80,2-80
29-90,30-89

Total of 1 assignment pair fully contains the other in this list. 
"""


def process_assignment_record(line):
    first_elf = line.split(',')[0]
    second_elf = line.split(',')[1]
    return {'elf1': [int(first_elf.split('-')[0]), int(first_elf.split('-')[1])],
            'elf2': [int(second_elf.split('-')[0]), int(second_elf.split('-')[1])]}


file_dir = '2022/Day4/'
input_filename = file_dir + 'test.txt'
input_filename = file_dir + 'assignments.txt'
overlapped_count = 0

for line in open(input_filename, 'r'):
    pair = process_assignment_record(line)

    if pair['elf1'][0] <= pair['elf2'][0] and pair['elf1'][1] >= pair['elf2'][1]:
        overlapped_count += 1
        continue
    if pair['elf2'][0] <= pair['elf1'][0] and pair['elf2'][1] >= pair['elf1'][1]:
        overlapped_count += 1

print(f"The total letter priority is {str(overlapped_count)}")
