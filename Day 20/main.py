#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

from collections import deque
import time

# Note that this took over 10 minutes to run, but did produce the two correct answers. Must be a better way to do it!!

def main():
    start = time.time()

    data = parse_data()

    answer1, path, distance_to_end = part1(data)
    answer2 = part2(path, distance_to_end)

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
        new_list=[]
        for item in row.strip():
            new_list.append(item)
        map.append(new_list)

    return map

def print_map(map):
    for row in map:
        for item in row:
            print(item, end="")
        print()

def part1(data):
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "S":
                start = (y,x)
            elif item == "E":
                end = (y,x)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    position = start
    traveled = 0
    path = [(start,traveled)]
    visited = set()
    while position != end:
        for direction in directions:
            new_position = (position[0]+direction[0], position[1]+direction[1])
            if data[new_position[0]][new_position[1]] in [".", "E"] and new_position not in visited:
                traveled += 1
                visited.add(new_position)
                path.append((new_position, traveled))
                position = new_position
                break

    possible_cheats = []
    positions_only = [pos for pos,_ in path]
    for position, _ in path:
        for direction in directions:
            new_position1 = (position[0]+direction[0], position[1]+direction[1])
            new_position2 = (position[0]+(2*direction[0]), position[1]+(2*direction[1]))
            if new_position1 not in positions_only and new_position2 in positions_only:
                if (new_position2, position) not in possible_cheats:
                    possible_cheats.append((position, new_position2))

    total_distance = len(path)-1
    distance_to_end = {}
    for position, step in path:
        distance_to_end[position] = total_distance-step

    big_save_cheats = 0
    cutoff = 99
    for start_cheat, end_cheat in possible_cheats:
        savings = distance_to_end[start_cheat]-distance_to_end[end_cheat]-2
        if savings>cutoff:
            big_save_cheats += 1
        
    return big_save_cheats, path, distance_to_end


def part2(path, distance_to_end):
    cutoff = 99
    possible_cheats = set()
    positions_only = [pos for pos,_ in path]
    for position in positions_only:
        for y in range(21):
            for x in range(21):
                if y+x >20:
                    break

                landing_position1 = (position[0]+y, position[1]+x)
                landing_position2 = (position[0]+y, position[1]-x)
                landing_position3 = (position[0]-y, position[1]+x)
                landing_position4 = (position[0]-y, position[1]-x)

                if landing_position1 in positions_only:
                    savings = distance_to_end[position] - distance_to_end[landing_position1] - y - x
                    if savings > cutoff:
                        possible_cheats.add(((position, landing_position1), savings))
                
                if landing_position2 in positions_only:
                    savings = distance_to_end[position] - distance_to_end[landing_position2] - y - x
                    if savings > cutoff:
                        possible_cheats.add(((position, landing_position2), savings))

                if landing_position3 in positions_only:
                    savings = distance_to_end[position] - distance_to_end[landing_position3] - y - x
                    if savings > cutoff:
                        possible_cheats.add(((position, landing_position3), savings))

                if landing_position4 in positions_only:
                    savings = distance_to_end[position] - distance_to_end[landing_position4] - y - x
                    if savings > cutoff:
                        possible_cheats.add(((position, landing_position4), savings))


    return len(possible_cheats)



if __name__ == "__main__":
    main()