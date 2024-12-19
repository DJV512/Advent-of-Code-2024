#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

from collections import defaultdict
import time
from PIL import Image

def main():

    data = parse_data()

    # answer1 = part1(data)
    answer2 = part2(data)

    print()
    print("--------Part 1 Answer-------------")
    # print(answer1)
    print()
    print("--------Part 2 Answer-------------")
    print(answer2)
    print()


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()
    robots = []
    robot_number = 0
    for row in data:
        robot_number += 1
        p, v = row.split(" ")
        px, py = p[2:].split(",")
        vx, vy = v[2:].split(",")
        robots.append({"Number": robot_number, "Current_x": int(px), "Current_y": int(py), "Vel_x": int(vx), "Vel_y": int(vy)})
    return robots


def part1(data):
    grid_x = 101
    grid_y = 103
    positions = defaultdict(int)
    for row in data:
        total_x_move = 100*row["Vel_x"]
        relative_x_move = total_x_move%grid_x
        final_x_pos = (row["Start_x"] + relative_x_move)%grid_x
        total_y_move = 100*row["Vel_y"]
        relative_y_move = total_y_move%grid_y
        final_y_pos = (row["Start_y"] + relative_y_move)%grid_y
        positions[(final_x_pos, final_y_pos)] += 1

    quadrants = defaultdict(int)
    for position in positions:
        if position[0]!= grid_x//2 and position[1]!=grid_y//2:
            if 0 <= position[0] < grid_x//2 and 0 <= position[1] < grid_y//2:
                quadrants["1"] += positions[position]
                # print(f"One: {position[0], position[1]}")
            elif grid_x//2 < position[0] < grid_x and 0 <= position[1] < grid_y//2:
                quadrants["2"] += positions[position]
                # print(f"Two: {position[0], position[1]}")
            elif 0 <= position[0] < grid_x//2 and grid_y//2 < position[1] < grid_y:
                quadrants["3"] += positions[position]
                # print(f"Three: {position[0], position[1]}")
            elif grid_x//2 < position[0] < grid_x and grid_y//2 < position[1] < grid_y:
                quadrants["4"] += positions[position]
                # print(f"Four: {position[0], position[1]}")

    total = quadrants["1"]*quadrants["2"]*quadrants["3"]*quadrants["4"]
    return total


def part2(data):
    grid_x = 101
    grid_y = 103
    for seconds in range(10500):
        positions = defaultdict(int)
        for row in data:
            new_x_pos = (row["Current_x"] + row["Vel_x"])%grid_x
            new_y_pos = (row["Current_y"] + row["Vel_y"])%grid_y
            positions[(new_x_pos, new_y_pos)] += 1
            row["Current_x"] = new_x_pos
            row["Current_y"] = new_y_pos
        map = ["."*grid_x for _ in range(grid_y)]
        for position in positions:
            map[position[1]] = map[position[1]][:position[0]] + "X" + map[position[1]][position[0]+1:]
        

        # Create a new black and white (1-bit) image
        img = Image.new("1", (grid_x, grid_y))  # "1" mode for 1-bit pixels (black and white)

        # Convert the string data into pixel data
        pixels = []
        for row in map:
            # Convert each character in the row to a pixel (1 for white, 0 for black)
            pixels.extend([1 if char == "X" else 0 for char in row])

        # Update the image with the pixel data
        img.putdata(pixels)

        # Save the image as a BMP file
        img.save(f"output{seconds+1}.bmp")



        # if seconds >=100:
        #     print(f"In {seconds+1} seconds, the map will look like:")
        #     for row in map:
        #         print(row)
        #     time.sleep(1)

    return None


if __name__ == "__main__":
    main()