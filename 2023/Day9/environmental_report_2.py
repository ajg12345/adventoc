""" Problem Prompt

While waiting for the sun to shine so you can glide on a handglider,
you're reading some environmental reports
deciding what number comes next in linear sequences
"""
from pathlib import Path
from pprint import pprint
from functools import reduce

class Sequence():
    def __init__(self, sequence_nums: list[int]):
        self.sequence_nums = self.load_sequence(sequence_nums)
        self.sequence_list = self.generate_sequence()

    def load_sequence(self, line: str) -> list[int]:
        return [int(n) for n in line.split()]

    def generate_sequence(self) -> list[list[int]]:
        """generates lists and lists until its finished"""
        input_list = self.sequence_nums
        generated_sequences = [input_list]
        while not self.generated_last_sequence(input_list):
            new_list = []
            for i in range(len(input_list)-1):
                diff = input_list[i + 1] - input_list[i]
                new_list.append(diff)
            generated_sequences.append(new_list)
            input_list = new_list
        return generated_sequences

    def generated_last_sequence(self, input_list: list[int]) -> bool:
        return input_list == [0] * len(input_list) 
    
    def get_next_number(self) -> int:
        next_number = 0
        for s in self.sequence_list[::-1]:
            next_number = s[0] - next_number
        return next_number

if __name__ == "__main__":
    #input_filename = Path().absolute() / "2023" / "Day9" / "example_environment.txt"
    input_filename = Path().absolute() / "2023" / "Day9" / "environment.txt"

    environ_sequences = []
    sum_next_numbers = 0
    for line in input_filename.open():
        environ_sequences.append(Sequence(line))

    for s in environ_sequences:
        sum_next_numbers += s.get_next_number()

    print('sum_next_numbers ' + str(sum_next_numbers))
