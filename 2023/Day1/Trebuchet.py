""" Problem Prompt
elves have marked top 50 places that there are problems with snow production.
they are loading you into a trebuchet.
their calibrayion document has been amended by an artist elf
each line of text has a valibration value, which is 2 digits in sequence
if there are more than one number its just hte first
if there is only one number its just that

"""
from pathlib import Path


def get_first_digit(s: str) -> str:
    for letter in s:
        if letter.isnumeric():
            return letter


if __name__ == "__main__":
    input_filename = Path().absolute() / "2023" / "Day1" / "calibration_doc.txt"
    running_sum = 0
    for line in input_filename.open():
        first_digit = get_first_digit(line)
        last_digit = get_first_digit(line[::-1])
        running_sum += int(first_digit + last_digit)

    print(running_sum)
