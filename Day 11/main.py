FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

# import time
# from functools import lru_cache

def main():

    data = parse_data()

    answer1 = part1(data)
    #answer2 = part2(data)

    print()
    print("--------Part 1 Answer-------------")
    print(answer1)
    print()
    print("--------Part 2 Answer-------------")
    # print(answer2)
    print()


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()
    line = [int(x) for x in data[0].split(" ")]
    return line


def part1(data):
    for x in range(25):
        data = change_stones(data)
        print(f"Iteration {x}: {len(data)}")
    return len(data)


def change_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone))//2 == len(str(stone))/2:
            length = len(str(stone))
            half = int(length/2)
            first = str(stone)[:half]
            second = str(stone)[half:].lstrip("0")
            if len(second) == 0:
                second = 0
            new_stones.append(int(first))
            new_stones.append(int(second))
        else:
            new_stones.append(stone*2024)
    return new_stones


def part2(data):

    # see main2.py



    total_stones = 0
    for i, stone in enumerate(data):
        for _ in range(25):
            stone = change_stones(stone)
            print(len(stone))
        total_stones += len(stone)
    return total_stones


# @lru_cache(maxsize=None)
def change_stone(stone):
    if stone == 0:
        new_stone = 1
    elif len(str(stone))//2 == len(str(stone))/2:
        length = len(str(stone))
        half = int(length/2)
        first = str(stone)[:half]
        second = str(stone)[half:]
        if str(second)[0] == 0:
            new_second = int(str(second)[1:])
        else:
            new_second = second
        new_stone = (int(first), int(new_second))
    else:
        new_stone = stone*2024
    return new_stone


if __name__ == "__main__":
    main()