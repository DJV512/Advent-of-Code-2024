#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

# Commented out code is my solution for part 1. For part 2, learned about networkx.
# Solved part 2 with networkx, then went back and rewrote part 1 using networkx.

from collections import defaultdict
import networkx as nx

def main():

    graph = parse_data()

    answer1 = part1(graph)
    answer2 = part2(graph)

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
    graph = nx.Graph([row.strip().split("-") for row in data])
    # network = defaultdict(list)
    # for row in data:
    #     one, two = row.strip().split("-")
    #     network[one] += [two]
    #     network[two] += [one]
    return graph


def part1(data):
    # networks = set()
    # networks_with_t = set()
    # for key in data:
    #     connected_comps = data[key]
    #     for comp in connected_comps:
    #         second_comps = data[comp]
    #         for second_comp in second_comps:
    #             if second_comp == key:
    #                 continue
    #             if key in data[second_comp]:
    #                 new_network = tuple(sorted((key, comp, second_comp)))
    #                 networks.add(new_network)
    #                 if new_network[0][0] == "t" or new_network[1][0] == "t" or new_network[2][0] == "t":
    #                     networks_with_t.add(new_network)

    result = nx.enumerate_all_cliques(data)
    total = 0
    for group in result:
        if len(group) == 3:
            for node in group:
                if node.startswith("t"):
                    total += 1
                    break
    return total


def part2(data):
    result = nx.find_cliques(data)
    max_result = max(result, key=len)
    return (",".join(sorted(max_result)))


if __name__ == "__main__":
    main()