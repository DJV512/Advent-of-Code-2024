#FILENAME = "sample10.txt"
#FILENAME = "sample9.txt"
#FILENAME = "sample8.txt"
#FILENAME = "sample7.txt"
#FILENAME = "sample6.txt"
#FILENAME = "sample5.txt"
#FILENAME = "sample4.txt"
#FILENAME = "sample3.txt"
#FILENAME = "sample2.txt"
#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time

def main():
    start = time.time()

    part1_map, directions, part2_map = parse_data()

    answer1 = part1(part1_map, directions)
    answer2 = part2(part2_map, directions)

    print()
    print("--------Part 1 Answer-------------")
    print(answer1)
    print()
    print("--------Part 2 Answer-------------")
    print(answer2)
    print()
    print(f"Execution took {1000*(time.time()-start)} ms.")
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

def printmap(map):
    for row in map:
        for position in row:
            print(position, end="")
        print()
    print()

def part1(data, directions):
    boxes = set()
    for y, row in enumerate(data):
        for x, position in enumerate(row):
            if position == "@":
                robot = (y,x)
            elif position == "O":
                boxes.add((y,x))
    
    printmap(data)
    
    for next_move in directions:
        
        if next_move == "<":
            next_pos = (robot[0], robot[1]-1)
            first_pos = next_pos
            if data[next_pos[0]][next_pos[1]] == ".":
                data[robot[0]][robot[1]] = "."
                robot = next_pos
                data[next_pos[0]][next_pos[1]] = "@"
                continue
            elif data[next_pos[0]][next_pos[1]] == "#":
                continue

            while next_pos in boxes:
                next_pos = (next_pos[0], next_pos[1]-1)
            if data[next_pos[0]][next_pos[1]] == "#":
                continue
            elif data[next_pos[0]][next_pos[1]] == ".":
                data[next_pos[0]][next_pos[1]] = "O"
                boxes.add(next_pos)
                data[first_pos[0]][first_pos[1]] = "@"
                boxes.remove(first_pos)
                data[robot[0]][robot[1]] = "."
                robot = first_pos

        elif next_move == "^":
            next_pos = (robot[0]-1, robot[1])
            first_pos = next_pos
            if data[next_pos[0]][next_pos[1]] == ".":
                data[robot[0]][robot[1]] = "."
                robot = next_pos
                data[next_pos[0]][next_pos[1]] = "@"
                continue
            elif data[next_pos[0]][next_pos[1]] == "#":
                continue

            while next_pos in boxes:
                next_pos = (next_pos[0]-1, next_pos[1])
            if data[next_pos[0]][next_pos[1]] == "#":
                continue
            elif data[next_pos[0]][next_pos[1]] == ".":
                data[next_pos[0]][next_pos[1]] = "O"
                boxes.add(next_pos)
                data[first_pos[0]][first_pos[1]] = "@"
                boxes.remove(first_pos)
                data[robot[0]][robot[1]] = "."
                robot = first_pos

        elif next_move == "v":
            next_pos = (robot[0]+1, robot[1])
            first_pos = next_pos
            if data[next_pos[0]][next_pos[1]] == ".":
                data[robot[0]][robot[1]] = "."
                robot = next_pos
                data[next_pos[0]][next_pos[1]] = "@"
                continue
            elif data[next_pos[0]][next_pos[1]] == "#":
                continue

            while next_pos in boxes:
                next_pos = (next_pos[0]+1, next_pos[1])
            if data[next_pos[0]][next_pos[1]] == "#":
                continue
            elif data[next_pos[0]][next_pos[1]] == ".":
                data[next_pos[0]][next_pos[1]] = "O"
                boxes.add(next_pos)
                data[first_pos[0]][first_pos[1]] = "@"
                boxes.remove(first_pos)
                data[robot[0]][robot[1]] = "."
                robot = first_pos

        elif next_move == ">":
            next_pos = (robot[0], robot[1]+1)
            first_pos = next_pos
            if data[next_pos[0]][next_pos[1]] == ".":
                data[robot[0]][robot[1]] = "."
                robot = next_pos
                data[next_pos[0]][next_pos[1]] = "@"
                continue
            elif data[next_pos[0]][next_pos[1]] == "#":
                continue

            while next_pos in boxes:
                next_pos = (next_pos[0], next_pos[1]+1)
            if data[next_pos[0]][next_pos[1]] == "#":
                continue
            elif data[next_pos[0]][next_pos[1]] == ".":
                data[next_pos[0]][next_pos[1]] = "O"
                boxes.add(next_pos)
                data[first_pos[0]][first_pos[1]] = "@"
                boxes.remove(first_pos)
                data[robot[0]][robot[1]] = "."
                robot = first_pos

    printmap(data)

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

    printmap(part2_map)

    for next_move in directions:
        if next_move == "<":
            next_pos = (robot[0], robot[1]-1)
            first_pos = next_pos
            if part2_map[next_pos[0]][next_pos[1]] == ".":
                part2_map[robot[0]][robot[1]] = "."
                robot = next_pos
                part2_map[next_pos[0]][next_pos[1]] = "@"
                continue
            elif part2_map[next_pos[0]][next_pos[1]] == "#":
                continue

            while next_pos in boxes or (next_pos[0], next_pos[1]-1) in boxes:
                next_pos = (next_pos[0], next_pos[1]-1)
            if part2_map[next_pos[0]][next_pos[1]] == "#":
                continue
            elif part2_map[next_pos[0]][next_pos[1]] == ".":
                move_dist = next_pos[1]-first_pos[1]
                for q in range(0,abs(move_dist),2):
                    part2_map[next_pos[0]][next_pos[1]+q] = "["
                    boxes.add((next_pos[0],next_pos[1]+q))
                for q in range(1,abs(move_dist)+1,2):
                    part2_map[next_pos[0]][next_pos[1]+q] = "]"
                    boxes.remove((next_pos[0],next_pos[1]+q))
                part2_map[first_pos[0]][first_pos[1]] = "@"
                part2_map[robot[0]][robot[1]]="."
                robot = first_pos
        
        elif next_move == ">":
            next_pos = (robot[0], robot[1]+1)
            first_pos = next_pos
            if part2_map[next_pos[0]][next_pos[1]] == ".":
                part2_map[robot[0]][robot[1]] = "."
                robot = next_pos
                part2_map[next_pos[0]][next_pos[1]] = "@"
                continue
            elif part2_map[next_pos[0]][next_pos[1]] == "#":
                continue

            while next_pos in boxes or (next_pos[0], next_pos[1]-1) in boxes:
                next_pos = (next_pos[0], next_pos[1]+1)
            if part2_map[next_pos[0]][next_pos[1]] == "#":
                continue
            elif part2_map[next_pos[0]][next_pos[1]] == ".":
                move_dist = next_pos[1]-first_pos[1]
                for q in range(1,abs(move_dist),2):
                    part2_map[next_pos[0]][next_pos[1]-q] = "["
                    boxes.add((next_pos[0],next_pos[1]-q))
                for q in range(0,abs(move_dist),2):
                    part2_map[next_pos[0]][next_pos[1]-q] = "]"
                    boxes.remove((next_pos[0],next_pos[1]-2-q))
                part2_map[first_pos[0]][first_pos[1]] = "@"
                part2_map[robot[0]][robot[1]]="."
                robot = first_pos

        elif next_move == "^":
            next_pos = (robot[0]-1, robot[1])
            first_pos = next_pos
            if part2_map[next_pos[0]][next_pos[1]] == ".":
                part2_map[robot[0]][robot[1]] = "."
                robot = next_pos
                part2_map[next_pos[0]][next_pos[1]] = "@"
                continue
            elif part2_map[next_pos[0]][next_pos[1]] == "#":
                continue

            if next_pos in boxes or (next_pos[0], next_pos[1]-1) in boxes:
                box_positions = []
                stack = set()
                if next_pos in boxes:
                    stack.add(next_pos)
                    stack.add((next_pos[0], next_pos[1]+1))
                    box_positions.append(next_pos)
                if (next_pos[0], next_pos[1]-1) in boxes:
                    stack.add((next_pos[0], next_pos[1]-1))
                    stack.add(next_pos)
                    box_positions.append((next_pos[0], next_pos[1]-1))
                moving = True
                while stack:
                    current_pos = stack.pop()
                    north_of_current = (current_pos[0]-1, current_pos[1])
                    if part2_map[north_of_current[0]][north_of_current[1]] == "#":
                        moving = False
                        break
                    if part2_map[north_of_current[0]][north_of_current[1]] == ".":
                        continue
                    if (north_of_current[0], north_of_current[1]) in boxes:
                        stack.add((north_of_current[0], north_of_current[1]))
                        stack.add((north_of_current[0], north_of_current[1]+1))
                        if ((north_of_current[0], north_of_current[1])) not in box_positions:
                            box_positions.append((north_of_current[0], north_of_current[1]))
                    if (north_of_current[0], north_of_current[1]-1) in boxes:
                        stack.add((north_of_current[0], north_of_current[1]))
                        stack.add((north_of_current[0], north_of_current[1]-1))
                        if ((north_of_current[0], north_of_current[1]-1)) not in box_positions:
                            box_positions.append((north_of_current[0], north_of_current[1]-1))
                
                if moving:
                    boxes_to_move = sorted(box_positions, key=lambda t: (t[0], t[1]))
                    for box in boxes_to_move:
                        part2_map[box[0]][box[1]]="."
                        part2_map[box[0]][box[1]+1]="."
                        part2_map[box[0]-1][box[1]]="["
                        part2_map[box[0]-1][box[1]+1]="]"
                        boxes.remove(box)
                        boxes.add((box[0]-1, box[1]))
                    
                    part2_map[first_pos[0]][first_pos[1]] = "@"
                    part2_map[robot[0]][robot[1]]="."
                    robot = first_pos
        
        elif next_move == "v":
            next_pos = (robot[0]+1, robot[1])
            first_pos = next_pos
            if part2_map[next_pos[0]][next_pos[1]] == ".":
                part2_map[robot[0]][robot[1]] = "."
                robot = next_pos
                part2_map[next_pos[0]][next_pos[1]] = "@"
                continue
            elif part2_map[next_pos[0]][next_pos[1]] == "#":
                continue


            if next_pos in boxes or (next_pos[0], next_pos[1]-1) in boxes:
                box_positions = []
                stack = set()
                if next_pos in boxes:
                    stack.add(next_pos)
                    stack.add((next_pos[0], next_pos[1]+1))
                    box_positions.append(next_pos)
                if (next_pos[0], next_pos[1]-1) in boxes:
                    stack.add((next_pos[0], next_pos[1]-1))
                    stack.add(next_pos)
                    box_positions.append((next_pos[0], next_pos[1]-1))
                moving = True
                while stack:
                    current_pos = stack.pop()
                    south_of_current = (current_pos[0]+1, current_pos[1])
                    if part2_map[south_of_current[0]][south_of_current[1]] == "#":
                        moving = False
                        break
                    if part2_map[south_of_current[0]][south_of_current[1]] == ".":
                        continue
                    if (south_of_current[0], south_of_current[1]) in boxes:
                        stack.add((south_of_current[0], south_of_current[1]))
                        stack.add((south_of_current[0], south_of_current[1]+1))
                        if ((south_of_current[0], south_of_current[1])) not in box_positions:
                            box_positions.append((south_of_current[0], south_of_current[1]))
                    if (south_of_current[0], south_of_current[1]-1) in boxes:
                        stack.add((south_of_current[0], south_of_current[1]))
                        stack.add((south_of_current[0], south_of_current[1]-1))
                        if ((south_of_current[0], south_of_current[1]-1)) not in box_positions:
                            box_positions.append((south_of_current[0], south_of_current[1]-1))
                
                if moving:
                    boxes_to_move = sorted(box_positions, key=lambda t: (t[0], t[1]))
                    for box in boxes_to_move[::-1]:
                        part2_map[box[0]][box[1]]="."
                        part2_map[box[0]][box[1]+1]="."
                        part2_map[box[0]+1][box[1]]="["
                        part2_map[box[0]+1][box[1]+1]="]"
                        boxes.remove(box)
                        boxes.add((box[0]+1, box[1]))
                    
                    part2_map[first_pos[0]][first_pos[1]] = "@"
                    part2_map[robot[0]][robot[1]]="."
                    robot = first_pos   

    printmap(part2_map)

    total = 0
    for box in boxes:
        total += (100*box[0] + box[1])
    return total


if __name__ == "__main__":
    main()