#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

def main():

    keys, locks = parse_data()

    answer1 = part1(keys, locks)
    answer2 = part2(keys, locks)

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
    keys = []
    locks = []
    for i, row in enumerate(data):
        # print(f"{i=}")
        if i % 8 == 0:
            # print("Start of new lock or key")
            if "#" in row:
                # print("Start of new lock")
                new_lock = []
                for x in range(i, i+7):
                    # print(f"{x=}")
                    # print(f"{data[x]=}")
                    new_lock.append(data[x].strip())
                locks.append(new_lock)
            else:
                # print("Start of new key")
                new_key = []
                for x in range(i, i+7):
                    # print(f"{x=}")
                    # print(f"{data[x]=}")
                    new_key.append(data[x].strip())
                keys.append(new_key)

    key_list = []
    for key in keys:
        one = -1
        two = -1
        three = -1
        four = -1
        five = -1
        for row in key:
            if row[0] == "#":
                one += 1
            if row[1] == "#":
                two += 1
            if row[2] == "#":
                three += 1
            if row[3] == "#":
                four += 1
            if row[4] == "#":
                five += 1
        key_list.append((one, two, three, four, five))
    

    lock_list = []
    for lock in locks:
        one = -1
        two = -1
        three = -1
        four = -1
        five = -1
        for row in lock:
            if row[0] == "#":
                one += 1
            if row[1] == "#":
                two += 1
            if row[2] == "#":
                three += 1
            if row[3] == "#":
                four += 1
            if row[4] == "#":
                five += 1
        lock_list.append((one, two, three, four, five))

    # print(key_list)
    # print()
    # print(lock_list)
    
    return key_list, lock_list


def part1(keys, locks):
    work_count = 0
    for lock in locks:
        for key in keys:
            one = lock[0] + key[0]
            two = lock[1] + key[1]
            three = lock[2] + key[2]
            four = lock[3] + key[3]
            five = lock[4] + key[4]
            # print((one, two, three, four, five))
            if one < 6 and two < 6 and three < 6 and four < 6 and five < 6:
                work_count += 1
    return work_count


def part2(keys, locks):
    return None


if __name__ == "__main__":
    main()