""" Problem Prompt
PART 2
Its going to take way more steps this time
nodes that send in A = the nodes that end in Z
start every node that ends in A and follow until they all end in Z (same time)
"""
from pathlib import Path
from dataclasses import dataclass
from math import lcm

@dataclass
class Node():
    position: str = ''
    L: str = ''
    R: str = ''

class NodeMap():
    def __init__(self, list_of_nodes: str):
        self.node_dict = self.load_node_dict(list_of_nodes)

    def load_node_dict(self, list_of_nodes: list) -> list[Node]:
        return {node.position : node for node in list_of_nodes}

    def go(self, direction: str, position: str) -> str:
        if direction == 'L':
            return self.node_dict[position].L
        else:
            return self.node_dict[position].R

@dataclass
class Ghost():
    position: str
    number_of_steps: int = 0

class GhostList():
    def __init__(self, ghost_list: list):
        self.ghost_list = ghost_list

    def check_if_all_Z(self) -> bool:
        for g in self.ghost_list:
            if g.position[2] != 'Z':
                return False
        return True

def load_node(line: str) -> Node:
    position = line.split(" = ")[0]
    L = line.split(" = (")[1].split(',')[0]
    R = line.split(" = (")[1].split(', ')[1].strip(')\n')
    return Node(position, L, R)

if __name__ == "__main__":
    input_filename = Path().absolute() / "2023" / "Day8" / "maps.txt"
    # input_filename = Path().absolute() / "2023" / "Day8" / "example_ghosts.txt"

    node_list = list()
    LR_path = None

    for line in input_filename.open():
        if not LR_path:
            LR_path = line.strip('\n')
            continue
        if line == '\n':
            continue
        node_list.append(load_node(line))
    
    ghost_list = list()
    for node in node_list:
        if node.position[2] == 'A':
            ghost_list.append(Ghost(node.position))

    my_ghosts = GhostList(ghost_list)
    my_map = NodeMap(node_list)

    total_number_of_steps = 0
    for ghost in my_ghosts.ghost_list:
        i = 0
        number_of_steps = 0
        while ghost.position[2] != 'Z':
            direction = LR_path[i]
            ghost.position = my_map.go(direction, ghost.position)
            i += 1
            number_of_steps += 1
            if i == len(LR_path):
                i = 0
        ghost.number_of_steps = number_of_steps
    
    print('check values now')
    ghost_nums = []
    for ghost in my_ghosts.ghost_list:
        print(ghost.number_of_steps)
        ghost_nums.append(ghost.number_of_steps)

    total_number_of_steps = lcm(*ghost_nums)

    """
    i = 0
    while not my_ghosts.check_if_all_Z():
        if i == len(LR_path):
            i = 0
        direction = LR_path[i]
        for ghost in my_ghosts.ghost_list:
            ghost.position = my_map.go(direction, ghost.position)
        i += 1
        total_number_of_steps += 1
        if total_number_of_steps % 100_000 == 0:
            print('total_number_of_steps > ' + str(total_number_of_steps // 100_000) + '00_000')
    """
    print('total_number_of_steps ' + str(total_number_of_steps))
