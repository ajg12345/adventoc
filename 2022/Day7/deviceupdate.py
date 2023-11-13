from collections import defaultdict
from pprint import pprint
from functools import lru_cache

"""
The elves
part 2 
the total disk space available to the filesystem is  70 000 000
and you need unused space of at least 30 000 000. you need to find a directory you
can delete that will free up enough space to run the update

in the example above the total amount of used space is 48381165,
which means that the size of the unused space must currently be 48381165
so to get 30 000 000 you need to delete a dir with a total size of at least 8381165
"""
# and i think i need a recursive function which sets the folder size as traverses down


def main():
    file_dir = '2022/Day7/'
    input_filename = file_dir + 'test.txt'
    input_filename = file_dir + 'filesystem.txt'
    

    with open(input_filename, 'r') as fin:
        blocks = ("\n" + fin.read().strip()).split("\n$ ")[1:]

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

    total_sizes = 0
    
    for abspath in dir_sizes:
        dir_sizes[abspath] = dfs(abspath)
    outermost_size = dir_sizes['/']
    unused_space = 70000000 - outermost_size
    needed_space = 30000000 - unused_space
    smallest_sizes = []
    for abspath in dir_sizes:
        dir_size = dir_sizes[abspath]
        if dir_size > needed_space:
            smallest_sizes.append(dir_size)
    print(min(smallest_sizes))


if __name__ == '__main__':
    main()
