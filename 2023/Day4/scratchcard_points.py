""" Problem Prompt

there are scratchcards aligned in a puzzle prompt
each line has 2 sections, scratched, and winning numbers separated by a pipe.
first match is 1 point and each match after the first one doubles the point value of the card.


"""
from pathlib import Path
from dataclasses import dataclass


class Card:
    def __init__(self, input_line: str):
        self.input_line = input_line
        self.scratch_list = self.get_scratch_list(input_line)
        self.win_list = self.get_win_list(input_line)

    def get_scratch_list(self, input_line):
        scratch_str = input_line.split(": ")[1].split(" | ")[0]
        return [int(scratch) for scratch in scratch_str.split()]

    def get_win_list(self, input_line):
        win_str = input_line.split(": ")[1].split(" | ")[1]
        return [int(win) for win in win_str.split()]


def load_cards(card_piles, filename: str):
    for line in filename.open():
        card_piles.append(Card(line))


if __name__ == "__main__":
    input_filename = Path().absolute() / "2023" / "Day4" / "scratchcards.txt"

    card_piles = list()
    load_cards(card_piles, input_filename)

    total_points = 0

    for card in card_piles:
        wins = 0
        for i in card.scratch_list:
            if i in card.win_list:
                wins += 1
        if wins:
            total_points += 2 ** (wins - 1)

    # assert total_points == 13
    print(total_points)
