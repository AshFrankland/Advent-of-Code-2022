def get_input():
    with open('Day_6_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
        input_string = raw_input[0]
        return input_string

def find_marker(input_string):
    for index in range(3, len(input_string)):
        marker = (input_string[index-3] + input_string[index-2] +
        input_string[index-1] + input_string[index])
        count = 0
        for char in marker:
            count += marker.count(char)
        if count == 4:
            return (index + 1)

def find_msg(input_string):
    for index in range(13, len(input_string)):
        marker = (input_string[index-13] + input_string[index-12] +
        input_string[index-11] + input_string[index-10] +
        input_string[index-9] + input_string[index-8] +
        input_string[index-7] + input_string[index-6] +
        input_string[index-5] + input_string[index-4] +
        input_string[index-3] + input_string[index-2] +
        input_string[index-1] + input_string[index])
        count = 0
        for char in marker:
            count += marker.count(char)
        if count == 14:
            return (index + 1)

def main():
    input_string = get_input()
    part1 = find_marker(input_string)
    print(part1)
    part2 = find_msg(input_string)
    print(part2)

if __name__ == '__main__':
    main()