#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

def main():

    list1, list2 = parse_data()

    answer1 = part1(list1, list2)
    answer2 = part2(list1, list2)

    print()
    print("--------Part 1 Answer-------------")
    print(answer1)
    print()
    print("--------Part 2 Answer-------------")
    print(answer2)
    print()


def parse_data():
    with open(FILENAME, "r") as f:
        raw_data = f.readlines()
    list1 = []
    list2 = []
    for row in raw_data:
        one, two = row.split("   ")
        list1.append(int(one))
        list2.append(int(two))
    return list1, list2


def part1(list1, list2):
    list1.sort()
    list2.sort()
    total = 0
    for i in range(len(list1)):
        diff = abs(list1[i] - list2[i])
        total += diff
    return total



def part2(list1, list2):
    dict = {}
    for row in list2:
        try:
            dict[row] += 1
        except KeyError:
            dict[row] = 1 
    similarity = 0
    for row in list1:
        try:
            product = row * dict[row]
        except KeyError:
            product = 0
        similarity += product
        
    return similarity


if __name__ == "__main__":
    main()