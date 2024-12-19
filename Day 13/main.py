#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import numpy as np

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
    
    machines = []
    machine_number = 0
    for row in data:
        if "Button A" in row:
            machine_number += 1
            d_x, d_y = row[10:].split(", ")
            Ax = int(d_x[2:])
            Ay = int(d_y[2:])
        elif "Button B" in row:
            d_x, d_y = row[10:].split(", ")
            Bx = int(d_x[2:])
            By = int(d_y[2:])
        elif "Prize" in row:
            d_x, d_y = row[7:].split(", ")
            Px = int(d_x[2:])
            Py = int(d_y[2:])
        else:
            machines.append({"Number": machine_number, "A": (Ax, Ay), "B": (Bx, By), "Prize": (Px, Py)})
    return machines


def part1(machines):
    cost_list = []
    for machine in machines:
        # Coefficient matrix (A)
        A = np.array([[machine["A"][0], machine["B"][0]], 
                    [machine["A"][1], machine["B"][1]]]).astype(int)

        # Right-hand side vector (b)
        b = np.array([machine["Prize"][0], machine["Prize"][1]]).astype(int)

        # Solve for [a, b]
        solution = np.linalg.solve(A, b)

        # Extract results
        a, b = solution
        check_x_value = machine["A"][0]*a.round() + machine["B"][0]*b.round() == machine["Prize"][0]
        check_y_value = machine["A"][1]*a.round() + machine["B"][1]*b.round() == machine["Prize"][1]
        if check_x_value and check_y_value:
            cost = 3*a.round() + b.round()
            cost_list.append(cost)

    return sum(cost_list)


def part2(machines):
    cost_list = []
    for machine in machines:
        # Coefficient matrix (A)
        A = np.array([[machine["A"][0], machine["B"][0]], 
                    [machine["A"][1], machine["B"][1]]]).astype(int)

        # Right-hand side vector (b)
        b = np.array([machine["Prize"][0]+10000000000000, machine["Prize"][1]+10000000000000]).astype(int)

        # Solve for [a, b]
        solution = np.linalg.solve(A, b)

        # Extract results
        a, b = solution
        check_x_value = machine["A"][0]*a.round() + machine["B"][0]*b.round() == machine["Prize"][0]+10000000000000
        check_y_value = machine["A"][1]*a.round() + machine["B"][1]*b.round() == machine["Prize"][1]+10000000000000
        if check_x_value and check_y_value:
            cost = 3*a.round() + b.round()
            cost_list.append(cost)

    return sum(cost_list)


if __name__ == "__main__":
    main()