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

def move(results, score, map, visited, start, end, position, next_direction, current_direction, path):
    new_position = (position[0] + next_direction[0], position[1] + next_direction[1])
    
    if next_direction == current_direction:
        score += 1
    else:
        score += 1001
    # print(f"New position: {new_position}, score: {score}")

    if new_position[0] < 0 or new_position[0] >= len(map[0]) or new_position[1] < 0 or new_position[1] >= len(map):
        # print("Off the map.")
        return
    
    if new_position in visited:
        # print("Already been here.")
        return
        
    if map[new_position[0]][new_position[1]]=="#":
        # print("Lookout! Wall!")
        return

    path.append(new_position)

    if new_position == end:
        results.append((score, path.copy()))
        # print("FOUND THE EXIT")
        # print(f"Path to exit: {path}")
        path.pop()
        return results

    visited.add(new_position)
    move(results, score, map, visited, start, end, new_position, (0,1), next_direction, path)
    move(results, score, map, visited, start, end, new_position, (1,0), next_direction, path)
    move(results, score, map, visited, start, end, new_position, (0,-1), next_direction, path)
    move(results, score, map, visited, start, end, new_position, (-1,0), next_direction, path)

    # print(f"Backtracking from {new_position}.")
    # print(f"Path before backtracking: {path}")
    visited.remove(new_position)
    path.pop()
    # print(f"Path after backtracking: {path}")
    if next_direction == current_direction:
        score -= 1
    else:
        score -= 1001

    return results
    
    


def part1(data):
    print_map(data)
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == "S":
                start = (y,x)
            elif item == "E":
                end = (y,x)
    
    # print(f"Start: {start}")
    # print(f"End: {end}")
    
    visited = set()
    visited.add(start)
    total = move([], 0, data, visited, start, end, start, (0, 1), (0, 1), [])
    visited = set()
    visited.add(start)
    total2 = move([], 1000, data, visited, start, end, start, (-1, 0), (-1, 0), [])

    # print("Total")
    # for row in total:
    #     print(row)
    #     print()
    #     print()

    # print("Total2")
    # for row in total2:
    #     print(row)
    #     print()
    #     print()

    lowest_score = 100000000000
    try:
        for score, path in total:
            if score < lowest_score:
                lowest_score = score
                final_path = path
    except TypeError:
        pass
    try:
        for score, path in total2:
            if score < lowest_score:
                lowest_score = score
                final_path = path
    except:
        pass
    answer = [lowest_score, final_path]
    # print(len(answer[1]))
    return answer


def part2(data):
    return None


if __name__ == "__main__":
    main()