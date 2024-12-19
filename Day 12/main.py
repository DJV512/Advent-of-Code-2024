#FILENAME = "sample_input.txt"
FILENAME = "input.txt"
#FILENAME = "sample2.txt"

def main():

    data = parse_data()

    answer1, regions = part1(data)
    answer2 = part2(data, regions)

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
    length = len(data)
    width = len(data[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(width)] for _ in range(length)]

    def is_valid(y, x, char):
        #Check whether the given cell is on the map, and is part of the current "char" region
        return 0 <= x < width and 0 <= y < length and not visited[y][x] and data[y][x] == char
    
    def build_region(y, x, char):
        stack = [(y,x)]
        region = []
        while stack:
            current_y, current_x = stack.pop()
            if visited[current_y][current_x]:
                continue
            visited[current_y][current_x] = True
            region.append((current_y, current_x))

            #Check all four directions
            for dy, dx in directions:
                new_y, new_x = current_y + dy, current_x + dx
                if is_valid(new_y, new_x, char):
                    stack.append((new_y, new_x))
        return region

    regions = []
    for i in range(length):
        for j in range(width):
            if not visited[i][j]:
                #Start a new region
                char = data[i][j]
                region = build_region(i, j, char)
                if region:
                    regions.append({"char": char, "area": len(region), "cells": region})
     
    for region in regions:
        region["perimeter"] = 0
        for y, x in region["cells"]:
            for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < length and 0 <= nx < width:
                        if data[ny][nx] != region["char"]:
                            region["perimeter"] += 1
                    else:
                        region["perimeter"] += 1

    total_sides = 0
    for region in regions:
        total_sides += region["area"] * region["perimeter"]
    
    return total_sides, regions


def part2(data, regions):
    length = len(data)
    width = len(data[0])
    diag_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def is_outside(y, x):
        """Check if a cell is outside the region or out of bounds."""
        return x < 0 or y < 0 or x >= width or y >= length or (y, x) not in region_set

    for region in regions:
        region_set = set(region["cells"])
        region["corners"] = 0

        for y, x in region_set:
            # print(f"Cell: {y,x}")
            for ddx, ddy in diag_directions:
                diag_x, diag_y = x + ddx, y + ddy
                if is_outside(diag_y, diag_x):  # Check the diagonal neighbor
                    # Check the two orthogonal neighbors that bracket the diagonal
                    # print(f"Diagonal Cell: {diag_y, diag_x}")
                    ortho1_x, ortho1_y = x + ddx, y
                    ortho2_x, ortho2_y = x, y + ddy
                    ortho1_inside = not is_outside(ortho1_y, ortho1_x)
                    ortho2_inside = not is_outside(ortho2_y, ortho2_x)
            
                    # Case 1: Inside Corner
                    if ortho1_inside and ortho2_inside:
                        # print(f"Inside Corner: {ortho1_y, ortho1_x} and diagonal {diag_y, diag_x} and {ortho2_y, ortho2_x}")
                        region["corners"] += 1
                    
                    # Case 2: Outside Corner
                    if not ortho1_inside and not ortho2_inside:
                        # print(f"Outside Corner: {ortho1_y, ortho1_x} and diagonal {diag_y, diag_x} and {ortho2_y, ortho2_x}")
                        region["corners"] += 1

                else:
                    ortho1_x, ortho1_y = x + ddx, y
                    ortho2_x, ortho2_y = x, y + ddy
                    ortho1_inside = is_outside(ortho1_y, ortho1_x)
                    ortho2_inside = is_outside(ortho2_y, ortho2_x)

                    # Case 3: Mobius Corner
                    if ortho1_inside and ortho2_inside:
                        # print(f"Mobius Corner: {ortho1_y, ortho1_x} and diagonal {diag_y, diag_x} and {ortho2_y, ortho2_x}")
                        region["corners"] += 1


    total_sides = 0
    for region in regions:
        print(region)
        total_sides += region["area"] * region["corners"]
    return total_sides


if __name__ == "__main__":
    main()