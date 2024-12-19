#FILENAME = "sample3.txt"
#FILENAME = "sample2.txt"
FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

def main():

    data, directions, part2_map = parse_data()

    answer1 = part1(data, directions)
    answer2 = part2(part2_map, directions)

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
    directions = []
    for row in data:
        if row[0] == "#":
            map.append(row.strip())
        elif row[0] == "\n":
            continue
        else:
            directions.append(row)
    
    new_map = []
    for row in map:
        new_list = []
        for item in row:
            new_list.append(item)
        new_map.append(new_list)
        
    go_to = ""
    for row in directions:
        go_to += row.strip()


    part2_map = []
    for row in new_map:
        new_row = []
        for item in row:
            if item == "#":
                new_row.append("#")
                new_row.append("#")
            elif item == ".":
                new_row.append(".")
                new_row.append(".")
            elif item == "O":
                new_row.append("[")
                new_row.append("]")
            elif item == "@":
                new_row.append("@")
                new_row.append(".")
        part2_map.append(new_row)

    return new_map, go_to, part2_map


def part1(data, directions):
    walls = set()
    boxes = set()
    for y, row in enumerate(data):
        for x, position in enumerate(row):
            if position == "@":
                robot = (y,x)
            elif position == "#":
                walls.add((y,x))
            elif position == "O":
                boxes.add((y,x))
    
    for x, next_move in enumerate(directions):
        # Print starting position before the current move
        # print(f"Robot position: {robot}")
        # for row in data:
        #     print("".join(row))
        # print()
        # print(f"Move number {x + 1}, direction is {next_move}:")
        
        if next_move == "<":
            next_pos = (robot[0], robot[1]-1)
            # print(f"Next_pos = {next_pos}")
            first_pos = next_pos
            if data[next_pos[0]][next_pos[1]] == ".":
                # print("next_pos is '.'")
                data[robot[0]][robot[1]] = "."
                robot = next_pos
                data[next_pos[0]][next_pos[1]] = "@"
                continue
            elif data[next_pos[0]][next_pos[1]] == "#":
                # print("next_pos is a wall")
                continue

            while next_pos in boxes:
                # print("Found box!")
                next_pos = (next_pos[0], next_pos[1]-1)
                # print(f"Next_pos: {next_pos}")
            if data[next_pos[0]][next_pos[1]] == "#":
                # print("Found wall after boxes!")
                continue
            elif data[next_pos[0]][next_pos[1]] == ".":
                # print("Found empty space after boxes!")
                data[next_pos[0]][next_pos[1]] = "O"
                boxes.add(next_pos)
                data[first_pos[0]][first_pos[1]] = "@"
                boxes.remove(first_pos)
                data[robot[0]][robot[1]] = "."
                robot = first_pos

        elif next_move == "^":
            next_pos = (robot[0]-1, robot[1])
            # print(f"Next_pos = {next_pos}")
            first_pos = next_pos
            if data[next_pos[0]][next_pos[1]] == ".":
                # print("next_pos is '.'")
                data[robot[0]][robot[1]] = "."
                robot = next_pos
                data[next_pos[0]][next_pos[1]] = "@"
                continue
            elif data[next_pos[0]][next_pos[1]] == "#":
                # print("next_pos is a wall")
                continue

            while next_pos in boxes:
                # print("Found box!")
                next_pos = (next_pos[0]-1, next_pos[1])
                # print(f"Next_pos: {next_pos}")
            if data[next_pos[0]][next_pos[1]] == "#":
                # print("Found wall after boxes!")
                continue
            elif data[next_pos[0]][next_pos[1]] == ".":
                # print("Found empty space after boxes!")
                data[next_pos[0]][next_pos[1]] = "O"
                boxes.add(next_pos)
                data[first_pos[0]][first_pos[1]] = "@"
                boxes.remove(first_pos)
                data[robot[0]][robot[1]] = "."
                robot = first_pos
        elif next_move == "v":
            next_pos = (robot[0]+1, robot[1])
            # print(f"Next_pos = {next_pos}")
            first_pos = next_pos
            if data[next_pos[0]][next_pos[1]] == ".":
                # print("next_pos is '.'")
                data[robot[0]][robot[1]] = "."
                robot = next_pos
                data[next_pos[0]][next_pos[1]] = "@"
                continue
            elif data[next_pos[0]][next_pos[1]] == "#":
                # print("next_pos is a wall")
                continue

            while next_pos in boxes:
                # print("Found box!")
                next_pos = (next_pos[0]+1, next_pos[1])
                # print(f"Next_pos: {next_pos}")
            if data[next_pos[0]][next_pos[1]] == "#":
                # print("Found wall after boxes!")
                continue
            elif data[next_pos[0]][next_pos[1]] == ".":
                # print("Found empty space after boxes!")
                data[next_pos[0]][next_pos[1]] = "O"
                boxes.add(next_pos)
                data[first_pos[0]][first_pos[1]] = "@"
                boxes.remove(first_pos)
                data[robot[0]][robot[1]] = "."
                robot = first_pos
        elif next_move == ">":
            next_pos = (robot[0], robot[1]+1)
            # print(f"Next_pos = {next_pos}")
            first_pos = next_pos
            if data[next_pos[0]][next_pos[1]] == ".":
                # print("next_pos is '.'")
                data[robot[0]][robot[1]] = "."
                robot = next_pos
                data[next_pos[0]][next_pos[1]] = "@"
                continue
            elif data[next_pos[0]][next_pos[1]] == "#":
                # print("next_pos is a wall")
                continue

            while next_pos in boxes:
                # print("Found box!")
                next_pos = (next_pos[0], next_pos[1]+1)
                # print(f"Next_pos: {next_pos}")
            if data[next_pos[0]][next_pos[1]] == "#":
                # print("Found wall after boxes!")
                continue
            elif data[next_pos[0]][next_pos[1]] == ".":
                # print("Found empty space after boxes!")
                data[next_pos[0]][next_pos[1]] = "O"
                boxes.add(next_pos)
                data[first_pos[0]][first_pos[1]] = "@"
                boxes.remove(first_pos)
                data[robot[0]][robot[1]] = "."
                robot = first_pos

    # print(f"Robot position: {robot}")
    # for row in data:
    #     print("".join(row))
    # print()

    total = 0
    for box in boxes:
        total += 100*box[0]+ box[1]
    return total


def part2(part2_map, directions):
    walls = set()
    boxes = set()
    for y, row in enumerate(part2_map):
        for x, position in enumerate(row):
            if position == "@":
                robot = (y,x)
            elif position == "#":
                walls.add((y,x))
            elif position == "[":
                boxes.add((y,x))

    for x, next_move in enumerate(directions):

        if next_move == "<":
            next_pos = (robot[0], robot[1]-1)
            # print(f"Next_pos = {next_pos}")
            first_pos = next_pos
            if part2_map[next_pos[0]][next_pos[1]] == ".":
                # print("next_pos is '.'")
                part2_map[robot[0]][robot[1]] = "."
                robot = next_pos
                part2_map[next_pos[0]][next_pos[1]] = "@"
                continue
            elif part2_map[next_pos[0]][next_pos[1]] == "#":
                # print("next_pos is a wall")
                continue

### start fixing for part 2 here
            while next_pos or (next_pos[0], next_pos[1]-1) in boxes:
                # print("Found box!")
                next_pos = (next_pos[0], next_pos[1]-1)
                # print(f"Next_pos: {next_pos}")
            if part2_map[next_pos[0]][next_pos[1]] == "#":
                # print("Found wall after boxes!")
                continue
            elif part2_map[next_pos[0]][next_pos[1]] == ".":
                # print("Found empty space after boxes!")
                part2_map[next_pos[0]][next_pos[1]] = "O"
                boxes.add(next_pos)
                part2_map[first_pos[0]][first_pos[1]] = "@"
                boxes.remove(first_pos)
                part2_map[robot[0]][robot[1]] = "."
                robot = first_pos
    
    # for row in part2_map:
    #     print("".join(row))
    # print()

    return None


if __name__ == "__main__":
    main()