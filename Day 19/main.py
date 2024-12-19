#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

from collections import defaultdict

def main():

    towels, patterns = parse_data()

    answer1 = part1(towels, patterns)
    answer2 = part2(towels, patterns)

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
    towels = []
    for row in data:
        if "," in row:
            patterns = row.strip().split(", ")
        elif len(row)>2:
            towels.append(row.strip())
    return towels, patterns


def part1(towels, patterns):
    possible = 0
    for towel in towels:
        queue = set()
        queue.add(towel)
        while queue:
            new_pattern = queue.pop()
            for pattern in patterns:
                if pattern == new_pattern[0:len(pattern)]:
                    next_pattern = new_pattern[len(pattern):]
                    if len(next_pattern) == 0:
                        possible += 1
                        queue = []
                        break
                    queue.add(next_pattern)
    return possible


def part2(towels, patterns):
    possible = 0
    for towel in towels:
        queue = defaultdict(int)
        queue[towel] = 1
        while queue:
            new_pattern = next(iter(queue))
            total = queue.pop(new_pattern)
            for pattern in patterns:
                if pattern == new_pattern[0:len(pattern)]:
                    next_pattern = new_pattern[len(pattern):]
                    if len(next_pattern) == 0:
                        possible += total
                        continue
                    queue[next_pattern]+= total
    return possible


if __name__ == "__main__":
    main()