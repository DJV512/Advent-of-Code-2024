#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

def main():

    rules, pages = parse_data()

    answer1, incorrect = part1(rules,pages)
    answer2 = part2(rules,incorrect)

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
    rules = {}
    pages = []
    for row in data:
        if len(row) == 6:
            x, y = row.strip().split("|")
            x=int(x)
            y=int(y)
            if x not in rules:
                rules[x] = [y]
            else:
                rules[x].append(y)
        elif len(row) == 1:
            continue
        else:
            page_order = row.strip().split(",")
            pages.append([int(x) for x in page_order])
    return rules,pages


def part1(rules,pages):
    correct = []
    incorrect = []
    for page in pages:
        good = 1
        for i, x in enumerate(page):
            if good == 1:
                if x not in rules:
                    continue
                need_be_after = rules[x]
                for y in need_be_after:
                    if y in page:
                        position = page.index(y)
                        if position <= i:
                            good = 0
        if good == 1:
            correct.append(page)
        else:
            incorrect.append(page)
    total = 0
    for i in correct:
        length = len(i)
        total += i[length//2]
    return total, incorrect


def part2(rules,incorrect):
    # print(rules)
    # print(incorrect)
    fixed = []
    for page in incorrect:
        wrong = True
        page_copy = page.copy()
        # print("Page copy: ", page_copy)
        while wrong == True:
            change = False
            for i, x in enumerate(page_copy):
                # print("I,X: ", i,x)
                try:
                    need_be_after = rules[x]
                    for y in need_be_after:
                        if y in page:
                            position = page_copy.index(y)
                            if position <= i:
                                # print("Before: ", page_copy)
                                a, b = page_copy[i], page_copy[position]
                                # print("A, B: ", a,b)
                                page_copy[position], page_copy[i] = a, b
                                # print("After: ", page_copy)
                                change = True
                except KeyError:
                    continue
                
            if change == False:
                wrong = False
        # print("Fixed: ", page_copy, "\n")
        fixed.append(page_copy)
        total = 0
        for i in fixed:
            length = len(i)
            total += i[length//2]

    return total


if __name__ == "__main__":
    main()