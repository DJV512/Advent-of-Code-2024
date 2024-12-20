FILENAME = "input.txt"

#ChatGPT's second attempt, which gives the correct answer

import heapq

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

def score_based_maze_solver(data, start, end):
    # Priority queue: (score, position, path, current_direction)
    pq = []
    heapq.heappush(pq, (0, start, [], None))  # Initial score, position, path, direction
    visited = set()

    best_score = float('inf')
    best_path = []

    while pq:
        score, position, path, current_direction = heapq.heappop(pq)

        # Skip if we've visited with a better score
        if (position, current_direction) in visited:
            continue
        visited.add((position, current_direction))

        # Add to path
        new_path = path + [position]

        # If we reach the end, update best solution
        if position == end:
            if score < best_score:
                best_score = score
                best_path = new_path
            continue

        # Explore all directions
        for next_direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            new_position = (position[0] + next_direction[0], position[1] + next_direction[1])

            # Check bounds and obstacles
            if (
                0 <= new_position[0] < len(data)
                and 0 <= new_position[1] < len(data[0])
                and data[new_position[0]][new_position[1]] != "#"
            ):
                # Calculate new score
                new_score = score + (1 if next_direction == current_direction else 1001)

                # Push to priority queue
                heapq.heappush(pq, (new_score, new_position, new_path, next_direction))

    return best_score, best_path

def part1(data):
    # print_map(data)
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "S":
                start = (y,x)
            elif item == "E":
                end = (y,x)
    
    result = score_based_maze_solver(data, start, end)
    print(len(result[1]))
    return result


def part2(data):
    return None


if __name__ == "__main__":
    main()