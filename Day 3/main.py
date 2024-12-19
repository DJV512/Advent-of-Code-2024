FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import re

def main():

    data = parse_data()

    answer1 = part1(data)
    answer2 = part2(data)

    print()
    print("--------Part 1 Answer-------------")
    print(answer1)
    print()
    print("--------Part 2 Answer-------------")
    print(answer2)
    print()


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()
    return data


def part1(data):
    results = []
    pattern = r'mul\(([0-9]{1,3},[0-9]{1,3})\)'
    for row in data:
        found = re.findall(pattern, row)
        for x in found:
            results.append(x)
    total = 0
    for item in results:
        x,y = item.split(",")
        total += int(x) * int(y)
    return total


def part2(data):
    results =  []
    pattern = r'mul\(([0-9]{1,3},[0-9]{1,3})\)|don\'t\(\)|do\(\)'
    for row in data:
        for match in re.finditer(pattern, row):
            results.append(match.group())
    total = 0
    use = 1
    for item in results:
        if "mul" in item:
            if use == 1:
                x,y = item.replace("mul(","").replace(")","").split(",")
                total += int(x) * int(y)
        elif "don't()" in item:
            use = 0
        elif "do()" in item:
            use = 1
    return total


if __name__ == "__main__":
    main()