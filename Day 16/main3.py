FILENAME = "input.txt"
#FILENAME = "sample_input.txt"
#FILENAME = "sample2.txt"

#ChatGPT's second attempt, which gives the correct answer

import heapq
import time

def main():
    start = time.time()

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
    print(f"Execution took {1000*(time.time()-start)} ms.")
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

def print_visited(map, visited):
    visited_cells=set()
    for cell, _ in visited:
        visited_cells.add(cell)

    missed_cells = []
    for y, row in enumerate(map):
        for x, item in enumerate(row):
            if (y, x) not in visited_cells:
                if item == "#":
                    print("\u2588", end="")
                elif item == ".":
                    print(" ", end="")
                    missed_cells.append((y,x))
            else:
                print("O", end="")
        print()

def print_map_with_path_to_file(map, path):
    with open("solved_maze.txt", "w") as f:
        for y, row in enumerate(map):
            for x, item in enumerate(row):
                if (y, x) not in path:
                    if item == "#":
                        f.write("\u2588")
                    elif item == ".":
                        f.write(" ")
                else:
                    f.write("O")
            f.write("\n")

def print_map_with_path(map, path):
    for y, row in enumerate(map):
        for x, item in enumerate(row):
            if (y, x) not in path:
                if item == "#":
                    print("\u2588", end="")
                elif item == ".":
                    print(" ", end="")
            else:
                print("O", end="")
        print()

def score_based_maze_solver(data, start, end):
    pq = []
    heapq.heappush(pq, (0, start, [], (0,1))) 
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


def find_all_optimal_paths(data, start, end):
    pq = []
    heapq.heappush(pq, (0, start, [], (0,1)))  
    visited = {}  
    best_score = float('inf')
    optimal_paths = []  

    while pq:
        score, position, path, current_direction = heapq.heappop(pq)

        # If this path exceeds the current best score, skip it
        if score > best_score:
            continue

        # Allow revisits for equal scores
        if (position, current_direction) in visited:
            if visited[(position, current_direction)] < score:
                continue
        visited[(position, current_direction)] = score

        # Update the current path
        new_path = path + [position]

        # If the endpoint is reached
        if position == end:
            if score < best_score:
                # Found a better score, reset the optimal paths
                best_score = score
                optimal_paths = [(best_score, new_path)]
            elif score == best_score:
                # Found another path with the same best score
                optimal_paths.append((best_score, new_path))
            continue

        # Explore all possible directions
        for next_direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_position = (position[0] + next_direction[0], position[1] + next_direction[1])

            # Check if the new position is valid
            if (
                0 <= new_position[0] < len(data)
                and 0 <= new_position[1] < len(data[0])
                and data[new_position[0]][new_position[1]] != "#"
            ):
                # Calculate the new score
                new_score = score + (1 if next_direction == current_direction else 1001)
                heapq.heappush(pq, (new_score, new_position, new_path, next_direction))

    # for z, (score, path) in enumerate(optimal_paths):
    #     print(f"Path: {z+1}, Score: {score}, Path Length: {len(path)}")

    return best_score, optimal_paths

def part1(data):
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "S":
                start = (y,x)
            elif item == "E":
                end = (y,x)
    
    result, _ = score_based_maze_solver(data, start, end)
    return result


def part2(data):
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "S":
                start = (y,x)
            elif item == "E":
                end = (y,x)
    _, optimal_paths = find_all_optimal_paths(data, start, end)

    unique_cells = set()
    for _, path in optimal_paths:
        unique_cells.update(path)
    total_unique = len(unique_cells)

    # print_map_with_path(data, unique_cells)

    return total_unique


if __name__ == "__main__":
    main()