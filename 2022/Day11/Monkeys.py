from collections import OrderedDict
from dataclasses import dataclass
from math import sqrt, floor
import numpy as np
from pprint import pprint

"""
Monkeys have taken things and wont give them back
predict where monkeys throw things.
monkeys throw based on when you're more or less worried

you take notes on the monkey behavior (puzzle input)
Starting items is a stack of items and their number is the worry level
Operation is how your worry level changes once the monkey inspects the item
test shows how the monkey interprets your worry level
    True and false determine the monkey behavior once its done
after a monkey inspects an item but before it tests your worry level ,your relief that the monkeys inspection didn't damage
the item causes the worry level to be divided by three and rounded down to nearest integer

the monkeys inspect and throw items
the monkeys go in order, monkey 0, monkey 1, etc each going in order, for each round, 
    inspecting and then possibly throwing an item
whena monkey throws an item to another monkey, it goes to the end of the monkey's list
if a monkey has no items, its turn ends

calculate the level OF MONKEY BUSINESS = PRODUCT OF 2 MOST ACTIVE MONKEY INSPECTION COUNT 
AFTER 20 ROUNDS

for example:
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1

"""

class Monkey():
    def __init__(self, items, op_operator, op_value, op_value_is_self, dv, true_location, false_location):
        self.items = items
        self.op_operator = op_operator
        self.op_value = op_value
        self.op_value_is_self = op_value_is_self
        self.test_divisibility = dv
        self.true_location = true_location
        self.false_location = false_location
        self.inspection_count = 0

    def get_items(self):
        return self.items

    def collect_item(self, item):
        self.items.append(item)
    
    def operation(self, worry_level):
        self.inspection_count += 1
        if not self.op_value_is_self:
            if self.op_operator == '*':
                return worry_level * self.op_value
            return worry_level + self.op_value
        else:
            if self.op_operator == '*':
                return worry_level * worry_level
            return worry_level + worry_level

    def test(self, worry_level, item):
        self.items.remove(item)
        if worry_level % self.test_divisibility == 0:
            return self.true_location
        else:
            return self.false_location

file_dir = '2022/Day11/'
input_filename = file_dir + 'test.txt'
input_filename = file_dir + 'MonkeyList.txt'

# begin parsing file
items = []
op_operator = None
op_value = None
op_value_is_self = None
test_divisibility = None
true_location = None
false_location = None
monkey_list = []
for raw_line in open(input_filename, 'r'):
    line = raw_line.strip('\n ').split(' ')

    if line[0] == '':
        continue

    if line[0] == 'Monkey':
        items = []
        op_operator = None
        op_value = None
        op_value_is_self = None
        test_divisibility = None
        true_location = None
        false_location = None
    elif line[0] == 'Starting':
        raw_items = line[2:]
        items = [int(i.strip(',')) for i in raw_items]
    elif line[0] == 'Operation:':
        op_operator = line[4]
        if line[5].isalpha():
            op_value_is_self = True
        else:
            op_value = int(line[5])
    elif line[0] == 'Test:':
        test_divisibility = int(line[3])
    elif line[1] == 'true:':
        true_location = int(line[5])
    elif line[1] == 'false:':
        false_location = int(line[5])
        monkey_list.append(Monkey(items, op_operator, op_value, op_value_is_self, test_divisibility, true_location, false_location))
    
       
round = 0
worry_level = 1
while round < 20:
    for monkey_number in range(len(monkey_list)):
        a = monkey_list[monkey_number].get_items().copy()
        for item in a:
            
            worry_level = item
            # alter worry_level acc to monkey
            worry_level = monkey_list[monkey_number].operation(worry_level)
            
            # releieved they didn't damage it
            worry_level = floor(worry_level/3)

            # figure out throw location
            target_monkey = monkey_list[monkey_number].test(worry_level, item)

            # item moves
            monkey_list[target_monkey].collect_item(worry_level)
    round += 1
monkey_business_list = [m.inspection_count for m in monkey_list]
monkey_business_list.sort(reverse=True)
total = monkey_business_list[0] * monkey_business_list[1]
print(f"total monkey business is {total}")
