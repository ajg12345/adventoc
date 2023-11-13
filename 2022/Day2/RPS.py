"""Elves have RPS tournament
winner is player with highest score
total score is sum of scores for each round
single round score is shape (1-Rock, 2-Paper, 3-Scissors) +
    outcome of the round (0 for loss, 3 for draw, 6 if win)
must calculate score for input file "strategy.txt"
it is A-R, B-P, C-S, and the second column is X-R, Y-P, Z-S

calculate the total score of the input sheet.
EXAMPLE SCORING:
A Y
B X
C Z

total of 15

A-Rock, B-Paper, C-Scissors, opponent
X-Rock, Y-Paper, Z-Scissors, player
"""


def calc_round(line):
    all_outcome_scores = {'A X': 4, 'B Y': 5, 'C Z': 6,
                          'A Z': 3, 'B X': 1, 'C Y': 2,
                          'A Y': 8, 'B Z': 9, 'C X': 7}
    return all_outcome_scores[line[0:3]]


file_dir = '2022/Day2/'
input_filename = file_dir + 'strategy.txt'
# input_filename = file_dir + 'test.txt'
total_score = 0

for line in open(input_filename, 'r'):
    total_score += calc_round(line)

print(f"The the total score acc to strategy guide is {str(total_score)}")
