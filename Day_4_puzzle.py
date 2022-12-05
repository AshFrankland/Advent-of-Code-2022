def get_input():
    with open('Day_4_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
        input_strings = []
        for line in raw_input:
            input_strings.append(line.rstrip('\n'))
        input_pairs = []
        for line in input_strings:
            input_pairs.append(line.split(','))
        for pair in range(len(input_pairs)):
            input_pairs[pair][0] = input_pairs[pair][0].split('-')
            input_pairs[pair][1] = input_pairs[pair][1].split('-')
        for pair in input_pairs:
            for num in pair:
                num[0] = int(num[0])
                num[1] = int(num[1])
        return input_pairs

def check_waste(input_pairs):
    count = 0
    for pair in input_pairs:
        if (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]):
            count += 1
    return count

def check_overlap(input_pairs):
    count = 0
    for pair in input_pairs:
        if (pair[0][0] in range(pair[1][0], pair[1][1] + 1)) or (pair[0][1] in range(pair[1][0], pair[1][1] + 1)) or (pair[1][0] in range(pair[0][0], pair[0][1] + 1)) or (pair[1][1] in range(pair[0][0], pair[0][1] + 1)):
            count += 1
    return count

def main():
    input_pairs = get_input()
    part1 = check_waste(input_pairs)
    print(part1)
    part2 = check_overlap(input_pairs)
    print(part2)

if __name__ == '__main__':
    main()