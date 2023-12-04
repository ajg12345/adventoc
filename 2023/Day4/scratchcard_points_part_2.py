""" Problem Prompt

there are scratchcards aligned in a puzzle prompt
each line has 2 sections, scratched, and winning numbers separated by a pipe.
first match is 1 point and each match after the first one doubles the point value of the card.

PART 2
scratch cards cause you to win more scratchcards == # of winning numbers you have.
so if card 10 has 
"""
from pathlib import Path


class Card:
    def __init__(self, input_line: str):
        self.input_line = input_line
        self.scratch_list = self.get_scratch_list(input_line)
        self.win_list = self.get_win_list(input_line)
        self.winner_count = 0
        self.is_winner = self.is_winner()
        self.card_count = 1

    def get_scratch_list(self, input_line):
        scratch_str = input_line.split(": ")[1].split(" | ")[0]
        return [int(scratch) for scratch in scratch_str.split()]

    def get_win_list(self, input_line):
        win_str = input_line.split(": ")[1].split(" | ")[1]
        return [int(win) for win in win_str.split()]

    def is_winner(self):
        for i in self.scratch_list:
            if i in self.win_list:
                self.is_winner = True
                self.winner_count += 1


def load_cards(card_piles, filename: str):
    for line in filename.open():
        card_piles.append([Card(line)])


# this is necessary, because copying the object as defined above is too slow
def create_list_from_cardgroups(card_groups):
    return_list = list()
    for card in card_groups:
        return_list.append([card[0].winner_count])
    return return_list


if __name__ == "__main__":
    input_filename = Path().absolute() / "2023" / "Day4" / "scratchcards.txt"

    card_groups = list()  # list of groups of cards by their copy number
    load_cards(card_groups, input_filename)
    card_list = create_list_from_cardgroups(card_groups)

    total_cards = 0

    for group_i in range(len(card_list)):
        card_group = card_list[group_i]
        print(group_i)
        for wincount in card_group:
            for copy_counter in range(wincount):
                card_list[group_i + copy_counter + 1].append(
                    card_list[group_i + copy_counter + 1][0]
                )
    for group in card_list:
        total_cards += len(group)

    print(total_cards)
