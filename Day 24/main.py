#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

from collections import deque
import time

def main():

    wire_values, instructions = parse_data()

    part2instructions = instructions.copy()

    answer1, binary = part1(wire_values, instructions)
    answer2 = part2(wire_values, part2instructions, binary)

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

    wire_values = {}
    instructions = deque()
    for row in data:
        if len(row.strip()) == 0:
            continue
        elif len(row.strip()) == 6:
            wire, value = row.strip().split(": ")
            wire_values[wire] = value
        else:
            first, operation, second, _, output = row.strip().split(" ")
            instructions.append((first, second, output, operation))
    
    # print(wire_values)
    # print()
    # print(instructions)

    return wire_values, instructions


def part1(wire_values, instructions):

    while instructions:
        next = instructions.popleft()
        if next[0] in wire_values and next[1] in wire_values:
            in1 = wire_values[next[0]]
            in2 = wire_values[next[1]]
            out_wire = next[2]
            op = next[3]
            # print(f"{in1=}, {in2=}, both in wire_values")
            if op == "AND":
                if in1 == "1" and in2 == "1":
                    out = "1"
                else:
                    out = "0"
            elif op == "OR":
                if in1 == "1" or in2 == "1":
                    out = "1"
                else:
                    out = "0"
            else:
                if in1 != in2:
                    out = "1"
                else:
                    out = "0"
            wire_values[out_wire] = out
        else:
            # print(f"{next=}")
            instructions.append(next)
        
        # print(f"{wire_values=}")
        # print()
        # print(f"{instructions=}")
        # print()
        # print()

    sorted_wires = {key: wire_values[key] for key in sorted(wire_values)}
    zs = []
    for wire in sorted_wires:      
        if wire.startswith("z"):
            zs.append(wire)
    
    # print(f"{sorted_wires=}")
    # print(f"{zs=}")
    
    binary = "".join([wire_values[x] for x in zs[::-1]])
    # print(binary)
    return int(binary,2), binary


def part2(wire_values, instructions, part1answer):
    sorted_wires = {key: wire_values[key] for key in sorted(wire_values)}
    xs = []
    for wire in sorted_wires:      
        if wire.startswith("x"):
            xs.append(wire)
    binaryx = "".join([wire_values[x] for x in xs[::-1]])

    ys = []
    for wire in sorted_wires:      
        if wire.startswith("y"):
            ys.append(wire)
    binaryy = "".join([wire_values[x] for x in ys[::-1]])

    decimal_x = int(binaryx, 2)
    decimal_y = int(binaryy, 2)
    expected_z = decimal_x + decimal_y
    print(f"Expected z: {expected_z}")
    print(f"Actual   z: {int(part1answer,2)}")
    print()
    binary_expected_z = bin(expected_z)[2:]
    print(f"Expected binary z: {binary_expected_z}")
    print(f"Part 1 answer   z: {part1answer}")
    print()
    
    binary_length = len(part1answer)

    wrong_bits = []
    for i, bit in enumerate(binary_expected_z):
        if part1answer[i] != bit:
            wrong_bits.append((binary_length-i-1, bit, part1answer[i]))
    
    print(f"{wrong_bits=}")
    print()

    potentials = []
    for wrong_bit, expected_bit, part1bit in wrong_bits:
        for instruction in instructions:
            if instruction[2] == "z" + str(wrong_bit) or instruction[2] == "z0" + str(wrong_bit):
                potentials.append((instruction, expected_bit, part1bit))

    print(potentials)
    print()

    for instruction, expected_bit, part1bit in potentials[::-1]:
        print(f"{instruction=}")
        print(f"{expected_bit=}")
        print(f"{part1bit=}")
        print()

    return None


if __name__ == "__main__":
    main()