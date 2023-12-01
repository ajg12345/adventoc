""" Problem Prompt
elves have marked top 50 places that there are problems with snow production.
they are loading you into a trebuchet.
their calibrayion document has been amended by an artist elf
each line of text has a valibration value, which is 2 digits in sequence
if there are more than one number its just hte first
if there is only one number its just that

THIS TIME THEY ARE ALSO SPELLED OUT

"""
from pathlib import Path


number_word_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
reverse_word_list = [number[::-1] for number in number_word_list]

def get_first_number(s: str, word_list) -> str:
    for i in range(len(s)):
        letter = s[i]
        if letter.isnumeric():
            return letter
        else:
            for j in range(len(word_list)):
                number = word_list[j]
                if s.find(number,i) == i:
                    return str(j+1)

if __name__ == '__main__':
    input_filename = Path().absolute() / '2023' / 'Day1' / 'calibration_doc.txt'
    running_sum = 0
    print(input_filename)
    
    for line in input_filename.open():
        first_digit = get_first_number(line, number_word_list)
        last_digit = get_first_number(line[::-1], reverse_word_list)
        running_sum += int(first_digit+last_digit)

    print(running_sum)