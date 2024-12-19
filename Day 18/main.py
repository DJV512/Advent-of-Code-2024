#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

from collections import deque
import time

grid_side = 71
number_of_drops = 1024

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
    drops = []
    for row in data:
        x, y = row.strip().split(",")
        drops.append((int(y),int(x)))
    return drops

def make_map(drops):
    map = {}
    for i in range(grid_side):
        for j in range(grid_side):
            map[(i,j)] = "."
    
    for i in range(number_of_drops):
        map[(drops[i][0],drops[i][1])] = "#"

    return map

def print_map(map):
    for i in range(grid_side):
        for j in range(grid_side):
            print(map[(i,j)], end="")
        print()

# def move(map, position, end, total_moves, visited, shortest):
#     if total_moves > shortest[0]:
#         return
    
#     if position == end:
#         shortest[0] = total_moves
#         return

#     for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         new_position = (position[0]+direction[0], position[1]+direction[1])

#         if 0 > new_position[0] or new_position[0] >= grid_side or 0 > new_position[1] or  new_position[1] >= grid_side:
#             continue

#         if map[(new_position[1], new_position[0])] == "#" or new_position in visited:
#             continue
        
#         visited.add(new_position)
#         move(map, new_position, end, total_moves + 1, visited, shortest)

#         visited.remove(new_position)
#     return


def solve_maze(map):
    start = (0,0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    visited.add(start)
    end = (grid_side-1, grid_side-1)
    queue = deque([(start,0)])

    while queue:
        position, distance = queue.popleft()

        if position == end:
            return distance
    
        for direction in directions:
            new_position = (position[0]+direction[0], position[1]+direction[1])

            if 0 > new_position[0] or new_position[0] >= grid_side or 0 > new_position[1] or  new_position[1] >= grid_side:
                continue

            if map[(new_position[0], new_position[1])] == "#" or new_position in visited:
                continue

            visited.add(new_position)
            queue.append((new_position, distance + 1))
    
    return -1

def part1(drops):
    map = make_map(drops)
    print_map(map)
    solve_maze(map)

    ## This was my first attempt at a recurisve solution that used depth first search, but that
    ## took way too long on the large input. Other code is breadth-first search, as suggested
    ## by ChatGPT

    # position = (0,0)
    # end = (grid_side-1, grid_side-1)
    # visited = set()
    # visited.add(position)
    # shortest = [1000000000]
    
    # move(map, position, end, 0, visited, shortest)



def part2(drops):
    map = make_map(drops)
    for q in range(1024, 3450):
        map[(drops[q][0],drops[q][1])] = "#"
        result = solve_maze(map)
        if result == -1:
            return q



if __name__ == "__main__":
    main()