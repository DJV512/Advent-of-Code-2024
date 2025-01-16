#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

from collections import deque
import time
import json

def main():
    start = time.time()

    wire_values, instructions = parse_data()
    parse_time = time.time()

    part2instructions = instructions.copy()

    answer1, binary = part1(wire_values, instructions)
    part1_time = time.time()
    answer2 = part2(wire_values, part2instructions, binary)
    part2_time = time.time()

    print("------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time:  {1000*(parse_time - start):.3f} ms")
    print(f"Part 1 Execution Time:      {1000*(part1_time - parse_time):.3f} ms")
    print(f"Part 2 Execution Time:      {1000*(part2_time - part1_time):.3f} ms")
    print(f"Total Execution Time:       {1000*(part2_time - start):.3f} ms")
    print("------------------------------------")



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

    return wire_values, instructions


def part1(wire_values, instructions):

    while instructions:
        next = instructions.popleft()
        if next[0] in wire_values and next[1] in wire_values:
            in1 = wire_values[next[0]]
            in2 = wire_values[next[1]]
            out_wire = next[2]
            op = next[3]
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
            instructions.append(next)

    sorted_wires = {key: wire_values[key] for key in sorted(wire_values)}
    zs = []
    for wire in sorted_wires:      
        if wire.startswith("z"):
            zs.append(wire)
    
    binary = "".join([wire_values[x] for x in zs[::-1]])
    return int(binary,2), binary

def build_tree(instructions, start_bit):
        
        if start_bit.startswith("x") or start_bit.startswith("y"):
            return {"name": start_bit, "operation": None, "inputs": []}

        for first, second, output, operation in instructions:
            if start_bit == output:
                first_branch = build_tree(instructions, first)
                second_branch = build_tree(instructions, second)

                return {
                "name": start_bit,
                "operation": operation,
                "inputs": [first_branch, second_branch]
            }
        
        return {"name": start_bit, "operation": None, "inputs": []}

    




def part2(wire_values, instructions, part1answer):
    sorted_wires = {key: wire_values[key] for key in sorted(wire_values)}
    xs = []
    ys = []
    for wire in sorted_wires:      
        if wire.startswith("x"):
            xs.append(wire)
        if wire.startswith("y"):
            ys.append(wire)

    binaryx = "".join([wire_values[x] for x in xs[::-1]])     
    binaryy = "".join([wire_values[x] for x in ys[::-1]])

    decimal_x = int(binaryx, 2)
    decimal_y = int(binaryy, 2)
    expected_z = decimal_x + decimal_y
    print(f"Expected z: {expected_z}")
    print(f"Actual   z: {int(part1answer,2)}")
    print()
    binary_expected_z = bin(expected_z)[2:]
    print(f"Expected binary z: {binary_expected_z}")
    print(f"Actual binary   z: {part1answer}")
    print()
    
    binary_length = len(part1answer)

    wrong_bits = []
    for i, bit in enumerate(binary_expected_z):
        if part1answer[i] != bit:
            wrong_bits.append("z" + (2-len(str(binary_length-i-1)))*"0" + str(binary_length-i-1))
    
    print(f"{wrong_bits=}")
    print()

    map = {}
    for bit in wrong_bits:
        path = build_tree(instructions, bit)
        map[bit] = path

    # output_file = "circuit_tree.json"
    # with open(output_file, "w") as file:
    #     json.dump(map["z33"], file, indent=4)


    return None


if __name__ == "__main__":
    main()




# bgs,pqc,rjm,swt,wsv,z07,z13,z31 - Final correct answer
# Visualized the input with this awesome tool https://lukas.fyi/day24/
# the code for part 2 above does not come close to solving the problem