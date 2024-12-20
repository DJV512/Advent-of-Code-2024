FILENAME = "input.txt"

#my recursive solution in main.py took way too long to run and never finished
#ChatGPT provided this program, which runs fast and appears to solve the maze,
#but doesn't get the right answer

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
    
    map = []
    for row in data:
        new_list = []
        row = row.strip()
        for item in row:
            new_list.append(item)
        map.append(new_list)
    return map

def print_map(map):
    for row in map:
        for item in row:
            print(item, end="")
        print()

def iterative_maze_solver(data, start, end):
    stack = [(start, 0, [], None)]  # (position, score, path, previous_direction)
    visited = set()
    results = []

    while stack:
        position, score, path, current_direction = stack.pop()
        if position in visited:
            continue
        visited.add(position)

        if position == end:
            results.append((score, path))
            continue

        for next_direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            new_position = (position[0] + next_direction[0], position[1] + next_direction[1])

            if (
                0 <= new_position[0] < len(data)
                and 0 <= new_position[1] < len(data[0])
                and new_position not in visited
                and data[new_position[0]][new_position[1]] != "#"
            ):
                new_path = path + [new_position]
                new_score = score + (1 if next_direction == current_direction else 1001)
                stack.append((new_position, new_score, new_path, next_direction))

    # Find the best path
    if results:
        lowest_score, best_path = min(results, key=lambda x: x[0])
        return lowest_score, best_path
    else:
        return None  # No solution

def part1(data):
    print_map(data)
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "S":
                start = (y,x)
            elif item == "E":
                end = (y,x)
    
    result = iterative_maze_solver(data, start, end)
    print(len(result[1]))
    return result


def part2(data):
    return None


if __name__ == "__main__":
    main()