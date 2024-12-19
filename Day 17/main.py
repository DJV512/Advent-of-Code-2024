#FILENAME = "sample2.txt"
#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import copy

def main():

    a, b, c, program = parse_data()

    answer1 = part1(a, b, c, program)
    answer2 = part2(program)

    print()
    print("--------Part 1 Answer-------------")
    final_answer1 = ""
    for item in answer1:
        final_answer1 += str(item) + ","
    print(final_answer1[0:-1])

    print()
    print("--------Part 2 Answer-------------")
    print(answer2)
    print()

def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    for row in data:
        if "Register A" in row:
            _, _, a = row.split(" ")
        a = int(a)
        if "Program" in row:
            _, program = row.split(" ")
            program = [int(x) for x in program.split(",")]
    b = 0
    c = 0
            
    return a, b, c, program


def part1(a, b, c, program):
    result = run_code(a, b, c, program)
    return result

def run_code(a, b, c, program):
    position = 0
    output = []
    while position < len(program):
        opcode = program[position]
        operand = program[position + 1]
        if opcode == 0:
            combo = make_combo(a, b, c, operand)
            a = a//(2**combo)
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = make_combo(a, b, c, operand) % 8
        elif opcode == 3:
            if a == 0:
                position += 2
                continue
            else:
                position = operand
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            output.append(make_combo(a, b, c, operand) % 8)
        elif opcode == 6:
            combo = make_combo(a, b, c, operand)
            b = a//(2**combo)
        elif opcode == 7:
            combo = make_combo(a, b, c, operand)
            c = a//(2**combo)
        position += 2
    return output

def make_combo(a, b, c, operand):
    if operand in [0,1,2,3]:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    elif operand == 7:
        raise Exception("Invalid program")

def find_solutions(a, program, values, results, level):
    if len(values) == 0:
        return
    val = values.pop()
    candidates = set()
    for i in range (0,8):
        print(f"Running code with a = {a+i}.")
        test = run_code(a+i, 0, 0, program)
        print(f"Output is {test}")
        if test[0] == val:
            candidates.add(i)
            if level == len(program):
                results.append(a+i)
                print(f"WE HAVE A WINNER!!!!!!!!: {a+i}")
    print(f"Candidates: {candidates}")
    for candidate in candidates:
        print(f"Current Candidate: {candidate}")
        _values = copy.deepcopy(values)
        find_solutions((a+candidate)*8, program, _values, results, level+1)
    
    return results

def part2(program):
    values = copy.deepcopy(program)
    results=[]
    print(f"Values: {values}")
    return find_solutions(0, program, values, results, 1)





if __name__ == "__main__":
    main()