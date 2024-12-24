#FILENAME = "sample_input.txt"
FILENAME = "input.txt"
#FILENAME = "sample2.txt"

import time
from collections import defaultdict

def main():
    start = time.time()
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
    print(f"Total time: {time.time()-start}")


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()
    first_numbers = [int(row.strip()) for row in data]
    return first_numbers


def part1(data):
    two_thousands = []
    for x in data:
        for _ in range(2000):
            first = x * 64
            x = (first ^ x) % 16777216
            second = x // 32
            x = (second ^ x) % 16777216
            third = x * 2048
            x = (third ^ x) % 16777216
        two_thousands.append(x)

    return sum(two_thousands)


def part2(data):
    counter = defaultdict(int)
    for x in data:
        changes = []
        seen_keys = set()
        for i in range(2000):
            start_price = int(str(x)[-1])
            first = x * 64
            x = (first ^ x) % 16777216
            second = x // 32
            x = (second ^ x) % 16777216
            third = x * 2048
            x = (third ^ x) % 16777216
            end_price = int(str(x)[-1])
            changes.append((end_price-start_price))
            if i > 2:
                if (changes[-4], changes[-3], changes[-2], changes[-1]) not in seen_keys:
                    counter[(changes[-4], changes[-3], changes[-2], changes[-1])] += end_price
                    seen_keys.add((changes[-4], changes[-3], changes[-2], changes[-1]))


    return max(counter.values())


if __name__ == "__main__":
    main()