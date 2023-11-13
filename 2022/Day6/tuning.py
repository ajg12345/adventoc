"""
The elves have a comm device which needs to lock on to a signal
the signal is a series of seemingly random char received one at a time
you need to add a subroutine to the device which detects a start-of-packet marker in the dataastream
the start of packet is 4 characterst hat are alll different

datastream buffer is the input
as an example:
mjqjpqmgbljsphdztnvjfqwrcgsmlb
should return 7 because position 7 (aka 6) is the first character of a marker

"""


def detect_signal(line):
    for char_pos in range(len(line)):
        message_len = 4

        # this is message length for part 2

        message_len = 14

        if char_pos < message_len:
            continue
        else:
            char_set = set(line[char_pos - message_len:char_pos])
            if len(char_set) == message_len:
                return char_pos


def main():
    file_dir = '2022/Day6/'
    input_filename = file_dir + 'test.txt'
    input_filename = file_dir + 'datastream.txt'

    for line in open(input_filename, 'r'):
        first_marker = detect_signal(line)
        print(first_marker)


if __name__ == '__main__':
    main()
