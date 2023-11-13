from collections import OrderedDict
from dataclasses import dataclass
from math import sqrt, floor
import numpy as np
from pprint import pprint

"""
Like before, but worry doesn't divide by 3 and go for 10_000 rounds

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
    
big_mod = 1
for m in monkey_list:
    big_mod *= m.test_divisibility

round = 0
worry_level = 1
while round < 10000:
    if round % 100 == 0:
        print('.',end=' ') # for whatever reason this is taking a really really long time...
    for monkey_number in range(len(monkey_list)):
        a = monkey_list[monkey_number].get_items().copy()
        for item in a:
            
            worry_level = item
            # alter worry_level acc to monkey
            worry_level = monkey_list[monkey_number].operation(worry_level)
            
            worry_level = worry_level % big_mod

            # figure out throw location
            target_monkey = monkey_list[monkey_number].test(worry_level, item)

            # item moves
            monkey_list[target_monkey].collect_item(worry_level)
    
    round += 1
monkey_business_list = [m.inspection_count for m in monkey_list]
monkey_business_list.sort(reverse=True)
total = monkey_business_list[0] * monkey_business_list[1]
print(f"total monkey business is {total}")
