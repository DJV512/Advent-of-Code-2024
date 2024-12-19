#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time

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
    start1 = time.time()
    with open(FILENAME, "r") as f:
        data = f.readlines()
    values = {}
    for row in data:
        total, numbers = row.split(":")
        total = int(total)
        number_list = numbers.strip().split(" ")
        values[total] = [int(x) for x in number_list]
    print("Parse: ", 1000*(time.time() - start1), "ms")
    return values


def part1(data):
    start2 = time.time()
    def calculate_all_expressions(numbers, index, current_value, results):
        # Base case: All numbers are processed
        if index == len(numbers):
            results.add(current_value)  # Store the final result
            return

        # Get the next number in the list
        next_number = numbers[index]

        # Recursive step: Try addition and multiplication
        calculate_all_expressions(numbers, index + 1, current_value + next_number, results)
        calculate_all_expressions(numbers, index + 1, current_value * next_number, results)

    def find_all_results(numbers):
        # Wrapper function initializes the recursion
        if not numbers:
            return set()  # Return an empty set if input list is empty

        results = set()  # This will store all unique results
        calculate_all_expressions(numbers, 1, numbers[0], results)
        return results

    # Example usage
    total_calibration = 0
    for key in data:
        possibles = find_all_results(data[key])
        if key in possibles:
            total_calibration += key
    print("Part 1: ", 1000*(time.time() - start2), "ms")
    return total_calibration


def part2(data):
    start3 = time.time()
    def calculate_all_expressions(numbers, index, current_value, results):
        # Base case: All numbers are processed
        if index == len(numbers):
            results.add(current_value)  # Store the final result
            return

        # Get the next number in the list
        next_number = numbers[index]

        # Recursive step: Try addition and multiplication and concatenation
        calculate_all_expressions(numbers, index + 1, current_value + next_number, results)
        calculate_all_expressions(numbers, index + 1, current_value * next_number, results)
        calculate_all_expressions(numbers, index + 1, concat(current_value, next_number), results)

    def find_all_results(numbers):
        # Wrapper function initializes the recursion
        if not numbers:
            return set()  # Return an empty set if input list is empty

        results = set()  # This will store all unique results
        calculate_all_expressions(numbers, 1, numbers[0], results)
        return results

    def concat(a,b):
        return int(f"{a}{b}")

    # Example usage
    total_calibration = 0
    for key in data:
        possibles = find_all_results(data[key])
        if key in possibles:
            total_calibration += key
    print("Part 2: ", 1000*(time.time() - start3), "ms")
    return total_calibration


if __name__ == "__main__":
    main()