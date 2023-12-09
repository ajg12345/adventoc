""" Problem Prompt
find a path through a spooky desert acc to L R turns using the map (prompt)
"""
from pathlib import Path
from dataclasses import dataclass

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

def load_node(line: str) -> Node:
    position = line.split(" = ")[0]
    L = line.split(" = (")[1].split(',')[0]
    R = line.split(" = (")[1].split(', ')[1].strip(')\n')
    return Node(position, L, R)

if __name__ == "__main__":
    
    input_filename = Path().absolute() / "2023" / "Day8" / "maps.txt"
    node_list = list()
    LR_path = None

    for line in input_filename.open():
        if not LR_path:
            LR_path = line.strip('\n')
            continue
        if line == '\n':
            continue
        node_list.append(load_node(line))
    
    mymap = NodeMap(node_list)

    total_number_of_steps = 0
    starting_position = 'AAA'
    position = starting_position
    ending_position = 'ZZZ'
    i = 0
    while position != ending_position:
        if i == len(LR_path):
            i = 0
        direction = LR_path[i]
        position = mymap.go(direction, position)
        i += 1
        total_number_of_steps += 1

    print('total_number_of_steps ' + str(total_number_of_steps))
    # assert total_number_of_steps == 2
    assert total_number_of_steps == 6
