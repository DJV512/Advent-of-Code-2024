#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

from collections import deque

def main():

    data = parse_data()

    grid_side = len(data)

    answer1, path, distance_to_end = part1(data)
    answer2 = part2(path, distance_to_end, grid_side)

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
    # print_map(data)
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "S":
                start = (y,x)
            elif item == "E":
                end = (y,x)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    position = start
    # print(start)
    # print(end)
    traveled = 0
    path = [(start,traveled)]
    visited = set()
    while position != end:
        # print(f"Position: {position}. End: {end}")
        for direction in directions:
            new_position = (position[0]+direction[0], position[1]+direction[1])
            # print(f"New_position: {new_position}")
            if data[new_position[0]][new_position[1]] in [".", "E"] and new_position not in visited:
                traveled += 1
                visited.add(new_position)
                path.append((new_position, traveled))
                position = new_position
                break

    # print("PATH")
    # print(path)
    # print()

    possible_cheats = []
    positions_only = [pos for pos,_ in path]
    for position, _ in path:
        for direction in directions:
            new_position1 = (position[0]+direction[0], position[1]+direction[1])
            new_position2 = (position[0]+(2*direction[0]), position[1]+(2*direction[1]))
            if new_position1 not in positions_only and new_position2 in positions_only:
                if (new_position2, position) not in possible_cheats:
                    possible_cheats.append((position, new_position2))

    # print("POSSIBLE CHEATS")
    # print(possible_cheats)
    # print(len(possible_cheats))
    # print()

    total_distance = len(path)-1
    distance_to_end = {}
    for position, step in path:
        distance_to_end[position] = total_distance-step

    # print("DISTANCE TO END")
    # print(distance_to_end)
    # print()

    big_save_cheats = 0
    cutoff = 0
    for start_cheat, end_cheat in possible_cheats:
        savings = distance_to_end[start_cheat]-distance_to_end[end_cheat]-2
        if savings>cutoff:
            big_save_cheats += 1
            # print(f"Big save cheat!! {start_cheat, end_cheat} saves {savings}!")
        

    return big_save_cheats, path, distance_to_end


def part2(path, distance_to_end, grid_side):
    print("Start part 2")
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    possible_cheats = []
    positions_only = [pos for pos,_ in path]
    for position in positions_only:
        best_cheat = 0
        # print(f"Position on path to cheat from: {position}")
        visited = set()
        queue = deque([(position, 0)])
        while queue:
            next_position, distance = queue.popleft()
            # print(f"Next position: {position}, with distance {distance}.")
            
            if distance > 20:
                continue
        
            for direction in directions:
                new_position = (next_position[0]+direction[0], next_position[1]+direction[1])

                if 0 > new_position[0] or new_position[0] >= grid_side or 0 > new_position[1] or  new_position[1] >= grid_side:
                    continue
                    
                if new_position in visited:
                    continue
            
                if new_position in positions_only:
                    if (new_position, position) not in possible_cheats:
                        cheat_distance = abs(new_position[0]-position[0])+abs(new_position[1]-position[1])
                        if cheat_distance > best_cheat:
                            best_cheat = cheat_distance
                            possible_cheats.append((position, new_position))

                
                visited.add(new_position)
                queue.append((new_position, distance + 1))



    # print("POSSIBLE CHEATS")
    # print(possible_cheats)
    print(f"Total possible cheats: {len(possible_cheats)}.")
    # print()

    big_save_cheats = 0
    cutoff = 49
    for start_cheat, end_cheat in possible_cheats:
        cheat_distance = abs(start_cheat[0]-end_cheat[0])+abs(start_cheat[1]-end_cheat[1])
        savings = distance_to_end[start_cheat]-distance_to_end[end_cheat] - cheat_distance
        # print(f"Start cheat: {start_cheat}, end cheat: {end_cheat}, cheat distance: {cheat_distance}, savings {savings}.")
        if savings>cutoff:
            big_save_cheats += 1
            # print(f"Big save cheat!! {start_cheat, end_cheat} saves {savings}!")

    return big_save_cheats



if __name__ == "__main__":
    main()