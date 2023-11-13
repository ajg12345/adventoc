# import os

# r only eat star fruit
# retrieve >50 stars by christmas, each day has 1 star puzzle that unlocks a followup star
# input file is Calories
# each line is an item and a blank space separates each elfs input
# find the elf carrying the most calories and what is it

# filename = os.path.basename(__file__)
top_elves = list()

input_filename = 'calories.txt'
# input_filename = 'test.txt'
max_line_number = 0
temp_calorie_total = 0
line_number = 0
for line in open(input_filename, 'r'):
    line_number += 1
    if line != '\n':
        temp_calorie_total += int(line)
    else:
        top_elves.append(temp_calorie_total)
        temp_calorie_total = 0

top_elves.sort()
total_calories = sum(top_elves[-3:])

print(f"The max calories were for top three elves is {str(total_calories)}")
