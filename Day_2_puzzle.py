def get_input():
    with open('Day_2_input.txt') as puzzle_input:
        raw_input = puzzle_input.readlines()
        input_strings = []
        for line in  raw_input:
            input_strings.append(line.rstrip('\n'))
        results_dict = {'A X': 0, 'A Y': 0, 'A Z': 0, 'B X': 0, 'B Y': 0, 'B Z': 0, 'C X': 0, 'C Y': 0, 'C Z': 0}
        for game in input_strings:
            results_dict[game] += 1
        return results_dict

def get_assumed_score(results):
    score = (results['A X']*4) + (results['A Y']*8) + (results['A Z']*3) + (results['B X']*1) + (results['B Y']*5) + (results['B Z']*9) + (results['C X']*7) + (results['C Y']*2) + (results['C Z']*6)
    return score

def get_score(results):
    score = (results['A X']*3) + (results['A Y']*4) + (results['A Z']*8) + (results['B X']*1) + (results['B Y']*5) + (results['B Z']*9) + (results['C X']*2) + (results['C Y']*6) + (results['C Z']*7)
    return score

def main():
    results = get_input()
    assumed_score = get_assumed_score(results)
    print(assumed_score)
    score = get_score(results)
    print(score)

if __name__ == '__main__':
    main()