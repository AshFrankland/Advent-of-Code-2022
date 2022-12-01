import pprint

def get_input():
    with open('Day_1_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
        int_list = []
        for line in raw_input:
            if line == '\n':
                int_list.append('')
            else:
                int_list.append(int(line.rstrip('\n')))
        int_list.append('')
        return int_list

def count_calories(int_list):
    highest_sum = 0
    current_sum = 0
    for num in int_list:
        if num == '':
            if current_sum > highest_sum:
                highest_sum = current_sum
            current_sum = 0
        else:
            current_sum += num
    return highest_sum

def top_three(int_list):
    top_1 = 0
    top_2 = 0
    top_3 = 0
    current_sum = 0
    for num in int_list:
        if num == '':
            if current_sum > top_1:
                top_3 = top_2
                top_2 = top_1
                top_1 = current_sum
            elif current_sum > top_2:
                top_3 = top_2
                top_2 = current_sum
            elif current_sum > top_3:
                top_3 = current_sum
            current_sum = 0
        else:
            current_sum += num
    sum_3 = top_1 + top_2 + top_3
    return sum_3

def main():
    int_list = get_input()
    first = count_calories(int_list)
    print(first)
    second = top_three(int_list)
    print(second)

if __name__ == '__main__':
    main()