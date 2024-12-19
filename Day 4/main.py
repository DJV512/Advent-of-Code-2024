FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

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
    return data

def part1(data):
    matrix = []
    for row in data:
        width = len(row)
        matrix.append(row)
    length = len(matrix)

    shifts = [-1,0,1]
    total = 0
    for i in range(width):
        for j in range(length):
            if matrix[i][j] != "X":
                continue
            else:
                for x in shifts:
                    if i+x < 0 or i+x >= width:
                         continue
                    for y in shifts:
                        if j+y < 0 or j+y >= length:
                            continue
                        if matrix[i+x][j+y] != "M":
                            continue
                        else:
                            if i+x+x < 0 or i+x+x >= width or j+y+y < 0 or j+y+y > length:
                                continue
                            if matrix[i+x+x][j+y+y] != "A":
                                continue
                            else:
                                if i+x+x+x < 0 or i+x+x+x >= width or j+y+y+y < 0 or j+y+y+y > length:
                                    continue
                                if matrix[i+x+x+x][j+y+y+y] != "S":
                                    continue
                                else:
                                    total += 1
            
    return total


def part2(data):
    matrix = []
    for row in data:
        width = len(row)
        matrix.append(row)
    length = len(matrix)

    total = 0
    for i in range(width):
        if i<1 or i == width-1:
            continue
        for j in range(length):
            if j<1 or j == length-1:
                continue
            if matrix[i][j] != "A":
                continue
            else:
                if matrix[i+1][j+1] not in ["M", "S"]:
                    continue
                else:
                    if matrix[i+1][j+1] == "M":
                        if matrix[i-1][j-1] == "S":
                            if matrix[i+1][j-1] in ["M", "S"]:
                                if matrix[i+1][j-1] == "M":
                                    if matrix[i-1][j+1] == "S":
                                        total += 1
                                elif matrix[i+1][j-1] == "S":
                                    if matrix[i-1][j+1] == "M":
                                        total += 1
                    elif matrix[i+1][j+1] == "S":
                        if matrix[i-1][j-1] == "M":
                            if matrix[i+1][j-1] in ["M", "S"]:
                                if matrix[i+1][j-1] == "M":
                                    if matrix[i-1][j+1] == "S":
                                        total += 1
                                elif matrix[i+1][j-1] == "S":
                                    if matrix[i-1][j+1] == "M":
                                        total += 1                
    return total


if __name__ == "__main__":
    main()