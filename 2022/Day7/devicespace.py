from collections import defaultdict
from pprint import pprint
from functools import lru_cache

"""
The elves

the puzzle input is a terminal history of commands and outputs.
from this construct the file hierarchy structure with sizes of each folder
from that calcuclate the sum of sizes of all directories with a size of at most 100,000

as an example:
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

the test.txt file should count a total size for dirs under 100000 of 95437
"""
# and i think i need a recursive function which sets the folder size as traverses down


def main():
    file_dir = '2022/Day7/'
    input_filename = file_dir + 'test.txt'
    input_filename = file_dir + 'filesystem.txt'
    

    with open(input_filename, 'r') as fin:
        blocks = ("\n" + fin.read().strip('\n')).split("\n$ ")[1:]

    # pprint(blocks[:5])
    path = []

    dir_sizes = defaultdict(int)
    children = defaultdict(list)

    def parse(block):
        lines = block.split("\n")
        command = lines[0]
        outputs = lines[1:]

        parts = command.split(' ')
        op = parts[0]
        if op == "cd":
            if parts[1] == '..':
                path.pop()
            else:
                path.append(parts[1])
            return
        
        abspath = '/'.join(path)
        assert op[0:2] == 'ls'

        sizes = []
        for line in outputs:
            if not line.startswith("dir"):
                sizes.append(int(line.split(' ')[0]))
            else:
                dir_name = line.split(' ')[1]
                children[abspath].append(f"{abspath}/{dir_name}")

        dir_sizes[abspath] = sum(sizes)
    
    for block in blocks:
        parse(block)

    @lru_cache(None)
    def dfs(abspath):
        size = dir_sizes[abspath]
        for child in children[abspath]:
            size += dfs(child)
        return size

    total_sum = 0
    for abspath in dir_sizes:
        path_total = dfs(abspath)
        if path_total <= 100000:
            total_sum += path_total

    print(total_sum)


if __name__ == '__main__':
    main()
