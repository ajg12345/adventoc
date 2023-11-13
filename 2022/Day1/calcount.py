# import os

# r only eat star fruit
# retrieve >50 stars by christmas, each day has 1 star puzzle that unlocks a followup star
# input file is Calories
# each line is an item and a blank space separates each elfs input
# find the elf carrying the most calories and what is it

# filename = os.path.basename(__file__)
input_filename = 'calories.txt'
max_calories = 0
max_line_number = 0
temp_calorie_total = 0
line_number = 0
for line in open(input_filename, 'r'):
    line_number += 1
    if line != '\n':
        temp_calorie_total += int(line)
    else:
        if temp_calorie_total > max_calories:
            max_calories = temp_calorie_total
            max_line_number = line_number
        temp_calorie_total = 0

print(f"The max calories were for elf ending on line {str(max_line_number-1)}")
print(f" with a total of {str(max_calories)} calories")