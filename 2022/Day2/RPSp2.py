"""
Like before but the strategy sheet has a diff interpretation
Calculate the total score of the input sheet.

EXAMPLE SCORING:
A Y
B X
C Z

total of 12

A-Rock, B-Paper, C-Scissors, opponent
X-must lose, Y-must draw, Z-must win, player outcome
"""


def calc_round(line):
    all_outcome_scores = {'A X': 3, 'B Y': 5, 'C Z': 7,
                          'A Z': 8, 'B X': 1, 'C Y': 6,
                          'A Y': 4, 'B Z': 9, 'C X': 2}
    return all_outcome_scores[line[0:3]]


file_dir = '2022/Day2/'
input_filename = file_dir + 'strategy.txt'
# input_filename = file_dir + 'test.txt'
total_score = 0

for line in open(input_filename, 'r'):
    total_score += calc_round(line)

print(f"The the total score acc to strategy guide is {str(total_score)}")
