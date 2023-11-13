"""
An elf got a crane. it moves one box at a time.
program moving the boxes and simulate movement acc to the inputs moves.txt
then print the top crate of each stack. There are 9 stacks

as an example:
        [F] [Q]         [Q]        
[B]     [Q] [V] [D]     [S]        
[S] [P] [T] [R] [M]     [D]        
[J] [V] [W] [M] [F]     [J]     [J]
[Z] [G] [S] [W] [N] [D] [R]     [T]
[V] [M] [B] [G] [S] [C] [T] [V] [S]
[D] [S] [L] [J] [L] [G] [G] [F] [R]
[G] [Z] [C] [H] [C] [R] [H] [P] [D]
 1   2   3   4   5   6   7   8   9 

move 3 from 5 to 2
move 3 from 8 to 4
move 7 from 7 to 3
move 14 from 3 to 9

"""


def parse_instructions(line, stacks):
    operation_buffer = line.split(' ')
    if operation_buffer[0] != 'move':
        if operation_buffer[0] == '\n':
            return
        if line[1] != '1':
            load_level(line, stacks)
    else:
        crane_box(operation_buffer, stacks)


def load_level(line, stacks):
    for stack_column in range(9):
        start = stack_column * 4
        end = start + 4
        contents = line[start:end]
        letter = contents[1]
        if '[' in contents:
            stacks[str(stack_column + 1)].insert(0, letter)


def crane_box(operation_buffer, stacks):
    box_count = int(operation_buffer[1])
    source = operation_buffer[3]
    destination = operation_buffer[5][0]
    for i in range(box_count):
        letter = stacks[source].pop()
        stacks[destination].append(letter)


def print_stack_tops(stacks):
    for key in stacks:
        letter = ' ' if not stacks[key] else stacks[key].pop()
        print(letter, end='')


def main():
    file_dir = '2022/Day5/'
    input_filename = file_dir + 'test.txt'
    input_filename = file_dir + 'moves.txt'

    stacks = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}

    for line in open(input_filename, 'r'):
        parse_instructions(line, stacks)
    print_stack_tops(stacks)


if __name__ == '__main__':
    main()
