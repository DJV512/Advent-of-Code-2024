FILENAME = "sample3.txt"
#FILENAME = "sample2.txt"
#FILENAME = "sample_input.txt"
#FILENAME = "input.txt"


# Tried to solve this with recursion, and even went back and forth with ChatGPT.
# However, I never could get it to work. But I saw a solution on reddit that didn't
# involve recursion, and rewrote my code to use that algorithm. That's in main2.py
# and worked beautifully.


def main():

    data, directions = parse_data()

    answer1 = part1(data, directions)
    answer2 = part2(data, directions)

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

    return new_map, go_to


def part1(data, directions):

    def move(data, robot, direction):
        print(f"Move called with robot position {robot}, direction {direction}.")
        next_pos = (robot[0] + direction[0], robot[1] + direction[1])

        # If next position is a wall, no movement
        if data[next_pos[0]][next_pos[1]] == "#":
            return robot

        # If next position is a box, check if all boxes can move
        if data[next_pos[0]][next_pos[1]] == "O":
            print(f"Box found at {next_pos}")
            box_next_pos = (next_pos[0] + direction[0], next_pos[1] + direction[1])
            print(f"Checking {box_next_pos}")

            # Check if the box can move
            if data[box_next_pos[0]][box_next_pos[1]] == ".":  # Empty space
                # Recursively move the box
                box_moved = move(data, next_pos, direction)
                
                # If the recursive call confirms the box moved, move this box and the robot
                if box_moved == next_pos:  # If box successfully moved
                    data[box_next_pos[0]][box_next_pos[1]] = "O"  # Move the box
                    data[next_pos[0]][next_pos[1]] = "@"          # Move robot to box's old position
                    data[robot[0]][robot[1]] = "."               # Clear robot's old position
                    return next_pos
                else:
                    return robot  # If box can't move, robot doesn't move

        # If next position is empty, check if all boxes have been moved first
        if data[next_pos[0]][next_pos[1]] == ".":
            print("Empty space")
            # Ensure this happens only after recursion (i.e., all boxes are pushed)
            data[next_pos[0]][next_pos[1]] = "@"  # Move robot to new position
            data[robot[0]][robot[1]] = "."       # Clear old position
            return next_pos

        # Default: no movement
        return robot
            


    for y, row in enumerate(data):
        for x,position in enumerate(row):
            if position == "@":
                robot = (y,x)
    
    for x, next_move in enumerate(directions):
        print(f"Move number {x + 1}, direction is {next_move}:")
        if next_move == "<":
            robot = move(data, robot, (0, -1))
        elif next_move == "^":
            robot = move(data, robot, (-1, 0))
        elif next_move == ">":
            robot = move(data, robot, (0, 1))
        elif next_move == "v":
            robot = move(data, robot, (1, 0))

        # Print feedback for the current move
        print(f"Robot position: {robot}")
        for row in data:
            print("".join(row))
        print()


    
        
    return None


def part2(data, directions):
    return None


if __name__ == "__main__":
    main()