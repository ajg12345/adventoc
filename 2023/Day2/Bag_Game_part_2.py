""" Problem Prompt
I've landed in Snow Islan, htere is no snow.
see bag of cubes which are red green or blue.
each game he hides a secret number of cubes of each color in the bag.
he needs to know information on the cubes.
he'll reach in and grab a few, show them and put them back, a few times per game
puzzle input is the log of several games
there is ID number, semicolon list of subset of cubes revealed

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

red must be less than 12, green less than 13, blue less than 14

"""
from pathlib import Path
from dataclasses import dataclass, field


@dataclass
class Draw:
    """describes each draw of game"""
    red: int = 0
    green: int = 0
    blue: int = 0

@dataclass
class Bag:
    """collection of draws"""
    draw_list: list[Draw] = field(default_factory=list)

    def min_required_color_power(self) -> int:
        """ assumes there are never 0 red/blue/green in a draw """
        min_red = 0
        min_green = 0
        min_blue = 0
        for d in self.draw_list:
            min_red = max(d.red, min_red)
            min_green = max(d.green, min_green)
            min_blue = max(d.blue, min_blue)
        return min_red * min_green * min_blue

def load_draw_from_line(line: str) -> Bag:
    draw_string = line.split(': ')[1].split('; ')
    return_bag = Bag()
    for d in draw_string:
        draws = d.split(', ')
        new_draw = Draw()
        for color in draws:
            if 'red' in color:
                new_draw.red = int(color.split()[0])
            if 'green' in color:
                new_draw.green = int(color.split()[0])
            if 'blue' in color:
                new_draw.blue = int(color.split()[0])
        return_bag.draw_list.append(new_draw)
    return return_bag

if __name__ == '__main__':
    input_filename = Path().absolute() / '2023' / 'Day2' / 'cube_games.txt'

    power_sum = 0

    for line in input_filename.open():
        bag_game = load_draw_from_line(line)
        power_sum += bag_game.min_required_color_power()
    
    print(power_sum)