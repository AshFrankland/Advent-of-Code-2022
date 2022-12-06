import copy

def get_input():
    with open('Day_5_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
        input_strings = []
        for line in raw_input:
            input_strings.append(line.rstrip('\n'))
        divider = input_strings.index('')
        crate_map = {}
        for stack in range(int(input_strings[divider - 1][-2])):
            crate_map[stack + 1] = []
        for row in range(divider - 2, -1, -1):
            stack = 1
            for crate in range(1, len(input_strings[row]), 4):
                if input_strings[row][crate] != ' ':
                    crate_map[stack].append(input_strings[row][crate])
                stack += 1
        for line in range(divider + 1):
            input_strings.pop(0)
        input_instructions = []
        for line in input_strings:
            input_instructions.append(line.lstrip('move '))
        input_nums = []
        for inst in input_instructions:
            input_nums.append(inst.split(' '))
        inst_nums = []
        for inst in input_nums:
            nums = []
            for num in inst:
                if num not in {'from', 'to'}:
                    nums.append(int(num))
            inst_nums.append(nums)
        return crate_map, inst_nums

def move_crates(crate_map, inst_nums):
    for inst in inst_nums:
        count = inst[0]
        while count > 0:
            crate_map[inst[2]].append(crate_map[inst[1]].pop())
            count -= 1
    return crate_map

def move_stacks(crate_map, inst_nums):
    for inst in inst_nums:
        count = inst[0]
        stack = []
        while count > 0:
            stack.append(crate_map[inst[1]].pop())
            count -= 1
        stack.reverse()
        for crate in stack:
            crate_map[inst[2]].append(crate)
    return crate_map

def main():
    crate_map, inst_nums = get_input()
    crate_map_1 = copy.deepcopy(crate_map)
    crate_map_1 = move_crates(crate_map_1, inst_nums)
    part1 = ''
    for stack in range(len(crate_map_1)):
        part1 += crate_map_1[stack + 1][-1]
    print(part1)
    crate_map_2 = copy.deepcopy(crate_map)
    crate_map_2 = move_stacks(crate_map_2, inst_nums)
    part2 = ''
    for stack in range(len(crate_map_2)):
        part2 += crate_map_2[stack + 1][-1]
    print(part2)

if __name__ == '__main__':
    main()