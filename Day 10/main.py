#FILENAME = "sample_input.txt"
#FILENAME = "sample2.txt"
#FILENAME = "sample3.txt"
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
    map = []
    for row in data:
        map.append(row.strip())
    return map


def part1(data):
    trailheads = []
    for y, item in enumerate(data):
        for x, position in enumerate(item):
            if position == '0':
                trailheads.append((y,x))
    # print(trailheads)
    length = len(data)
    width = len(data[0])
    results = set()
    final_results = []
    path_count = [0]
    for trailhead in trailheads:
        check_for_trail(data, trailhead, -1, trailhead[0], trailhead[1], set(), results, length, width, path_count)
        final_results.append(results)
    return path_count[0]


def check_for_trail(data, trailhead, current_height, current_y, current_x, visited, results, length, width, path_count):
    # print(f"Entering check_for_trail: {current_y}, {current_x}, Current Height: {current_height}, Visited: {visited}")
    # print()
    
    if (current_y, current_x) in visited:
        # print(f"Already visited: ({current_y}, {current_x})")
        # print()
        return
    
    if current_y < 0 or current_y >= length or current_x < 0 or current_x >= width:
        # print(f"Out of bounds ({current_y}, {current_x})")
        # print()
        return

    if current_height == -1:
        expected_height = 0
    else:
        expected_height = current_height + 1

    try:
        if int(data[current_y][current_x]) != expected_height:
            # print(f"Invalid height: ({current_y}, {current_x}), Expected: {expected_height}, Found: {data[current_y][current_x]}")
            # print()
            return
        # else:
            # print(f"Correct height found: ({current_y}, {current_x}), Expected: {expected_height}, Found: {data[current_y][current_x]}")
            # print()
    except ValueError:
        return


    visited.add((current_y, current_x))
    # print(f"Currently visiting: ({current_y}, {current_x}), Visited: {visited}")
    # print()

    if expected_height == 9:
        # print(f"WE'VE REACHED THE TOP! Trailhead: {trailhead}, Nine Position: ({current_y}, {current_x})")
        # print()
        results.add((current_y, current_x))
        path_count[0] += 1
        return

    check_for_trail(data, trailhead, current_height + 1, current_y + 1, current_x, visited, results, length, width, path_count)
    check_for_trail(data, trailhead, current_height + 1, current_y, current_x + 1, visited, results, length, width, path_count)
    check_for_trail(data, trailhead, current_height + 1, current_y - 1, current_x, visited, results, length, width, path_count)
    check_for_trail(data, trailhead, current_height + 1, current_y, current_x - 1, visited, results, length, width, path_count)

    visited.remove((current_y, current_x))
    # print(f"Backtracking from: ({current_y}, {current_x})")
    # print()

def part2(data):
    trailheads = []
    for y, item in enumerate(data):
        for x, position in enumerate(item):
            if position == '0':
                trailheads.append((y,x))
    # print(trailheads)
    length = len(data)
    width = len(data[0])
    results = set()
    final_results = []
    path_count = [0]
    for trailhead in trailheads:
        check_for_trail2(data, trailhead, -1, trailhead[0], trailhead[1], set(), results, length, width, path_count)
        final_results.append(results)
    return path_count[0]


def check_for_trail2(data, trailhead, current_height, current_y, current_x, visited, results, length, width, path_count):
    # print(f"Entering check_for_trail: {current_y}, {current_x}, Current Height: {current_height}, Visited: {visited}")
    # print()
    
    if (current_y, current_x) in visited:
        # print(f"Already visited: ({current_y}, {current_x})")
        # print()
        return
    
    if current_y < 0 or current_y >= length or current_x < 0 or current_x >= width:
        # print(f"Out of bounds ({current_y}, {current_x})")
        # print()
        return

    if current_height == -1:
        expected_height = 0
    else:
        expected_height = current_height + 1

    try:
        if int(data[current_y][current_x]) != expected_height:
            # print(f"Invalid height: ({current_y}, {current_x}), Expected: {expected_height}, Found: {data[current_y][current_x]}")
            # print()
            return
        # else:
            # print(f"Correct height found: ({current_y}, {current_x}), Expected: {expected_height}, Found: {data[current_y][current_x]}")
            # print()
    except ValueError:
        return


    visited.add((current_y, current_x))
    # print(f"Currently visiting: ({current_y}, {current_x}), Visited: {visited}")
    # print()

    if expected_height == 9:
        # print(f"WE'VE REACHED THE TOP! Trailhead: {trailhead}, Nine Position: ({current_y}, {current_x})")
        # print()
        results.add((current_y, current_x))
        path_count[0] += 1
        visited.remove((current_y, current_x))
        # print(f"Removing 9 from visited: ({current_y}, {current_x})")
        # print()
        return

    check_for_trail2(data, trailhead, current_height + 1, current_y + 1, current_x, visited, results, length, width, path_count)
    check_for_trail2(data, trailhead, current_height + 1, current_y, current_x + 1, visited, results, length, width, path_count)
    check_for_trail2(data, trailhead, current_height + 1, current_y - 1, current_x, visited, results, length, width, path_count)
    check_for_trail2(data, trailhead, current_height + 1, current_y, current_x - 1, visited, results, length, width, path_count)

    visited.remove((current_y, current_x))
    # print(f"Backtracking from: ({current_y}, {current_x})")
    # print()
    return None


if __name__ == "__main__":
    main()