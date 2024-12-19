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
    harddrive=[]
    filenumber=0
    for i, x in enumerate(data[0]):
        if i/2 == i//2:
            for _ in range(int(x)):
                harddrive.append(filenumber)
            filenumber += 1
        else:
            for _ in range(int(x)):
                harddrive.append(".")
    return harddrive

def part1(data):
    first_empty = 0
    last_full = 0
    length = len(data)
    while True:
        for i, x in enumerate(data):
            if x == ".":
                first_empty = i
                break
        for j, y in enumerate(data[::-1]):
            if y != ".":
                last_full = length - j
                break
        if first_empty >= last_full:
            break
        else:
            data[first_empty] = y
            data[last_full-1] = "."
    total = 0
    for i,x in enumerate(data):
        if x!= ".":
            total += i*x
    return total


def part2(data):
    first_position = True
    space_map = {}
    empty_space_length = 1
    first_position_index = 0
    in_empty_space = False
    for i, x in enumerate(data):
        if x == ".":
            if first_position:
                first_position_index = i
                first_position = False
                in_empty_space = True
            else:
                empty_space_length += 1
        else:
            if in_empty_space:
                space_map[first_position_index] = empty_space_length
                first_position = True
                empty_space_length = 1
                in_empty_space = False
    current_file = data[-1]
    file_length = 0
    length = len(data)
    file_position = length-1
    in_file = True
    while current_file >= 0:
        for x in data[file_position::-1]:
            if x == current_file:
                in_file = True
                file_length += 1
            else:
                if in_file:
                    break
            file_position-=1
        for key in sorted(space_map):
            if space_map[key] >= file_length and key < file_position:
                for i in range(file_length):
                    data[key+i] = current_file
                for i in range(file_length):
                    data[file_position+1+i] = "."
                
                # Remake the space_map after the move
                first_position = True
                space_map = {}
                empty_space_length = 1
                first_position_index = 0
                in_empty_space = False
                for i, x in enumerate(data):
                    if x == ".":
                        if first_position:
                            first_position_index = i
                            first_position = False
                            in_empty_space = True
                        else:
                            empty_space_length += 1
                    else:
                        if in_empty_space:
                            space_map[first_position_index] = empty_space_length
                            first_position = True
                            empty_space_length = 1
                            in_empty_space = False

                break
                
        current_file -= 1
        file_length = 0
        in_file = False   

    # calculate the total once all moves are made         
    total = 0
    for i,x in enumerate(data):
        if x!= ".":
            total += i*x
    return total


if __name__ == "__main__":
    main()