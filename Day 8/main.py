#FILENAME = "sample_input.txt"
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
        map.append(row)
    return map


def part1(data):
    antennas = {}
    length = len(data)
    for y, row in enumerate(data):
        width = len(row)
        for x, item in enumerate(row):
            if item != "." and item!= "\n":
                if item not in antennas.keys():
                    antennas[item] = [(y,x)]
                else:
                    antennas[item].append((y,x))
    # print(antennas)
    # print()
    antinodes=[]
    for antenna in antennas:
        for z, node1 in enumerate(antennas[antenna]):
            for node2 in antennas[antenna][(z+1):]:
                # print(node1, node2)
                y_dist = node1[0] - node2[0]
                x_dist = node1[1] - node2[1]
                anti_y1 = node1[0] + y_dist
                anti_x1 = node1[1] + x_dist
                anti_y2 = node2[0] - y_dist
                anti_x2 = node2[1] - x_dist
                if anti_y1 >= 0 and anti_y1 < length and anti_x1 >= 0 and anti_x1 < width:
                    antinode1 = (anti_y1, anti_x1)
                    # print("Antinode: ", antinode1)
                    if antinode1 not in antinodes:
                        antinodes.append(antinode1)
                
                if anti_y2 >= 0 and anti_y2 < length and anti_x2 >= 0 and anti_x2 < width:
                    antinode2 = (anti_y2, anti_x2)
                    # print("Antinode: ", antinode2)
                    if antinode2 not in antinodes:
                        antinodes.append(antinode2)
    # print(antinodes)
    return len(antinodes)


def part2(data):
    antennas = {}
    length = len(data)
    for y, row in enumerate(data):
        width = len(row)
        for x, item in enumerate(row):
            if item != "." and item!= "\n":
                if item not in antennas.keys():
                    antennas[item] = [(y,x)]
                else:
                    antennas[item].append((y,x))
    print(antennas)
    print()
    antinodes=[]
    for antenna in antennas:
        for z, node1 in enumerate(antennas[antenna]):
            for node2 in antennas[antenna][(z+1):]:
                print(node1, node2)
                if node1 not in antinodes:
                    antinodes.append(node1)
                if node2 not in antinodes:
                    antinodes.append(node2)
                y_dist = node1[0] - node2[0]
                x_dist = node1[1] - node2[1]
                anti_y1 = node1[0] + y_dist
                anti_x1 = node1[1] + x_dist
                while anti_y1 >= 0 and anti_y1 < length and anti_x1 >= 0 and anti_x1 < width:
                    antinode1 = (anti_y1, anti_x1)
                    if antinode1 not in antinodes:
                        print("Antinode: ", antinode1)
                        antinodes.append(antinode1)
                    anti_y1 += y_dist
                    anti_x1 += x_dist

                anti_y2 = node2[0] - y_dist
                anti_x2 = node2[1] - x_dist
                while anti_y2 >= 0 and anti_y2 < length and anti_x2 >= 0 and anti_x2 < width:
                    antinode2 = (anti_y2, anti_x2)
                    if antinode2 not in antinodes:
                        print("Antinode: ", antinode2)
                        antinodes.append(antinode2)
                    anti_y2 -= y_dist
                    anti_x2 -= x_dist
    return len(antinodes)


if __name__ == "__main__":
    main()