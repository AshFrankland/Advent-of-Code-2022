def get_input():
    with open('Day_3_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
        input = []
        for line in raw_input:
            input.append(line.rstrip('\n'))
        split_input = []
        for sack in input:
            split_input.append((sack[:len(sack)//2], sack[len(sack)//2:]))
        return split_input, input

def find_matches(rucksacks):
    items_dict = {}
    for sack in rucksacks:
        for item in sack[0]:
            if item in sack[1]:
                if item in items_dict:
                    items_dict[item] += 1
                else:
                    items_dict[item] = 1
                break
    return items_dict

def find_badges(rucksacks):
    badges_dict = {}
    for group in range(len(rucksacks)//3):
        for item in rucksacks[group*3]:
            if item in rucksacks[(group*3) + 1] and item in rucksacks[(group*3) + 2]:
                if item in badges_dict:
                    badges_dict[item] += 1
                else:
                    badges_dict[item] = 1
                break
    return badges_dict

def assign_priority(items):
    for item in items:
        if ord(item) <= 90:
            items[item] *= (ord(item) - 38)
        else:
            items[item] *= (ord(item) - 96)
    return items

def main():
    rucksacks_split, rucksacks = get_input()
    items = find_matches(rucksacks_split)
    items = assign_priority(items)
    part1 = 0
    for num in items:
        part1 += items[num]
    print(part1)
    badges = find_badges(rucksacks)
    badges = assign_priority(badges)
    part2 = 0
    for num in badges:
        part2 += badges[num]
    print(part2)

if __name__ == '__main__':
    main()