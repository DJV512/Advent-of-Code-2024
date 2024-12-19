#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

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
    safes = 0
    safe_list=[]
    for x, row in enumerate(data):
        levels = row.split(" ")
        diff = int(levels[1]) - int(levels[0])

        if 0 < diff < 4:
            direction = "up"
        elif -4 < diff < 0:
            direction = "down"
        else:
            continue

        flag = 0
        last_level = int(levels[1])
        for next_level in levels[2:]:
            diff = int(next_level) - last_level
            if direction == "up":
                if 0 < diff < 4:
                    last_level = int(next_level)
                else:
                    flag = 1
                    continue
            else:
                if -4 < diff < 0:
                    last_level = int(next_level)
                else:
                    flag = 1
                    continue
        if flag == 0:
            safes += 1
            safe_list.append(x)
    # print(safe_list)
    # print(len(safe_list))
    return safes




def part2(data):
    safes = 0
    safe_list=[]
    for x, row in enumerate(data):
        levels = row.split(" ")
        diff = int(levels[1]) - int(levels[0])

        flag = 0

        if 0 < diff < 4:
            direction = "up"
        elif -4 < diff < 0:
            direction = "down"
        else:
            flag = 1

        last_level = int(levels[1])
        for next_level in levels[2:]:
            diff = int(next_level) - last_level
            if direction == "up":
                if 0 < diff < 4:
                    last_level = int(next_level)
                else:
                    flag = 1
                    continue
            else:
                if -4 < diff < 0:
                    last_level = int(next_level)
                else:
                    flag = 1
                    continue
        if flag == 0:
            safes += 1
            safe_list.append(x)
        else:
            print(x)
            for i in range(len(levels)):
                modified_levels = levels.copy()
                modified_levels.pop(i)

                diff = int(modified_levels[1]) - int(modified_levels[0])

                if 0 < diff < 4:
                    direction = "up"
                elif -4 < diff < 0:
                    direction = "down"
                else:
                    continue

                flag = 0
                last_level = int(modified_levels[1])
                for next_level in modified_levels[2:]:
                    diff = int(next_level) - last_level
                    if direction == "up":
                        if 0 < diff < 4:
                            last_level = int(next_level)
                        else:
                            flag = 1
                            continue
                    else:
                        if -4 < diff < 0:
                            last_level = int(next_level)
                        else:
                            flag = 1
                            continue
                if flag == 0:
                    safes += 1
                    safe_list.append(x)
                    break
    # print(safe_list)
    return safes


if __name__ == "__main__":
    main()