#FILENAME = "sample_input.txt"
FILENAME = "input.txt"
#FILENAME = "sample2.txt"

import time

def main():

    map = parse_data()

    answer1, visited = part1(map)
    answer2 = part2(map, visited)

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
    map = []
    for row in data:
        map.append(row)
    return map


def part1(map):
    for row in map:
        if "^" in row:
            y_pos = map.index(row)
            x_pos = row.index("^")
            break
    direction = "up"
    on_map = True
    visited = []
    visited.append((y_pos, x_pos))
    while on_map == True:
        try:
            if direction == "up":
                if y_pos - 1 >= 0:
                    if map[y_pos-1][x_pos] == "#":
                        direction = "right"
                    else:
                        y_pos -= 1
                        if (y_pos, x_pos) not in visited:
                            visited.append((y_pos, x_pos))
                else:
                    on_map = False
            elif direction == "right":
                if map[y_pos][x_pos+1] == "#":
                    direction = "down"
                else:
                    x_pos += 1
                    if (y_pos, x_pos) not in visited:
                        visited.append((y_pos, x_pos))
            elif direction == "down":
                if map[y_pos+1][x_pos] == "#":
                    direction = "left"
                else:
                    y_pos += 1
                    if (y_pos, x_pos) not in visited:
                        visited.append((y_pos, x_pos))
            elif direction == "left":
                if x_pos - 1 >= 0:
                    if map[y_pos][x_pos-1] == "#":
                        direction = "up"
                    else:
                        x_pos -= 1
                        if (y_pos, x_pos) not in visited:
                            visited.append((y_pos, x_pos))
                else:
                    on_map = False
        except IndexError:
            on_map = False
    return len(visited), visited


def part2(map, visited):
    start_time = time.time()
    for row in map:
        if "^" in row:
            y_pos_start = map.index(row)
            x_pos_start = row.index("^")
            break
    loop_list = []
    for (new_y, new_x) in visited[1:]:
        direction = "up"
        x_pos = x_pos_start
        y_pos = y_pos_start
        on_map = True
        new_path = []
        count = 0
        while on_map == True:
            try:
                if direction == "up":
                    if y_pos - 1 >= 0:
                        if map[y_pos-1][x_pos] == "#" or (y_pos-1, x_pos) == (new_y, new_x):
                            direction = "right"
                        else:
                            y_pos -= 1
                            if (y_pos, x_pos) not in new_path:
                                new_path.append((y_pos, x_pos))
                                count = 0
                            else:
                                count += 1
                    else:
                        on_map = False
                elif direction == "right":
                    if map[y_pos][x_pos+1] == "#"or (y_pos, x_pos+1) == (new_y, new_x):
                        direction = "down"
                    else:
                        x_pos += 1
                        if (y_pos, x_pos) not in new_path:
                            new_path.append((y_pos, x_pos))
                            count = 0
                        else:
                            count += 1
                elif direction == "down":
                    if map[y_pos+1][x_pos] == "#"or (y_pos+1, x_pos) == (new_y, new_x):
                        direction = "left"
                    else:
                        y_pos += 1
                        if (y_pos, x_pos) not in new_path:
                            new_path.append((y_pos, x_pos))
                            count = 0
                        else:
                            count += 1
                elif direction == "left":
                    if x_pos - 1 >= 0:
                        if map[y_pos][x_pos-1] == "#"or (y_pos, x_pos-1) == (new_y, new_x):
                            direction = "up"
                        else:
                            x_pos -= 1
                            if (y_pos, x_pos) not in new_path:
                                new_path.append((y_pos, x_pos))
                                count = 0
                            else:
                                count += 1
                    else:
                        on_map = False
            except IndexError:
                on_map = False
            if count > 500:
                loop_list.append((new_y, new_x))
                break
    print(time.time() - start_time)
    return len(loop_list)


if __name__ == "__main__":
    main()