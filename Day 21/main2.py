# Input is so short this time I didn't bother to parse it, but just typed it in manually.
#input_codes = ["029A", "980A", "179A", "456A", "379A"] #sample input numbers
input_codes = ["780A", "539A", "341A", "189A", "682A"] #real input numbers

# Copied main.py to this to make big edits but still have the originally "working"
# version in main.py.

import time
from functools import lru_cache
from collections import defaultdict

keypad = {
        "7": (0,0),
        "8": (0,1), 
        "9": (0,2),
        "4": (1,0),
        "5": (1,1),
        "6": (1,2),
        "1": (2,0),
        "2": (2,1),
        "3": (2,2),
        "0": (3,1),
        "A": (3,2),
    }

directional_pad = {
        "^": (0,1),
        "A": (0,2),
        "<": (1,0),
        "v": (1,1),
        ">": (1,2),
    }

def main():

    answer1 = find_complexity(2)
    answer2 = find_complexity(25)

    print()
    print("--------Part 1 Answer-------------")
    print(answer1)
    print()
    print("--------Part 2 Answer-------------")
    print(answer2)
    print()

def keypad_move(position, end_position):
    key_moves = ""
    end_position = keypad[end_position]
    change_y = end_position[0]-position[0]
    change_x = end_position[1]-position[1]
    if change_x > 0:
        key_moves += change_x * ">"
    if change_y > 0:
        key_moves += change_y * "v"
    if change_y < 0:
        key_moves += abs(change_y) * "^" 
    if change_x < 0:
        key_moves += abs(change_x) * "<"

    return key_moves+"A", end_position

@lru_cache
def directional_move(position, end_position):
    key_moves = ""
    end_position = directional_pad[end_position]
    change_y = end_position[0]-position[0]
    change_x = end_position[1]-position[1]
    if change_x > 0:
        key_moves += change_x * ">"
    if change_y > 0:
        key_moves += change_y * "v"
    if change_x < 0:
        key_moves += abs(change_x) * "<"
    if change_y < 0:
        key_moves += abs(change_y) * "^" 

    return key_moves+"A", end_position

def find_complexity(number_of_robots):
    
#### Key insight: Don't need to keep the entirety of the sequence in memory. Each move, for instance
#### "v>vA" is independent of other moves, and there are a very limited number of moves possible.
#### Thus, just keep a count of how many times each move is needed at every level.

#### Next insight: I can't keep all moves together in one dictionary because at the end each code
#### has to have it's own particular length. So I need a counter for each code.



    all_moves = {}
    print(f"Starting robot number 1")
    for code in input_codes:
        all_moves[code] = defaultdict(int)
        position = (3,2)
        for i, char in enumerate(code):
            new_move, position = keypad_move(position, char)
            all_moves[code][new_move] += 1

    # print(all_moves)

    # print("FINISHED FIRST ROBOT")

    for i in range(number_of_robots):
        print(f"Starting robot number {i+2}")
        newest_moves = {}
        for code in all_moves:
            newest_moves[code] = defaultdict(int)
            for move in all_moves[code]:
                position = (0,2)
                for char in move:
                    # print(f"Getting move for robot {i+2}, code {code}, move {move}, and char {char}.")
                    new_move, position = directional_move(position, char)
                    newest_moves[code][new_move] += all_moves[code][move] 
            all_moves[code] = newest_moves[code]
        # print(all_moves)

  

    complexity = 0
    for code in all_moves:
        length = 0
        for move in all_moves[code]:
            length += len(move)*all_moves[code][move]
        complexity += length * int(code[0:-1])
        print(f"Input = {code} and length of moves = {length}.")
        print(f"Complexity adds {int(code[0:-1])} * {length} = {int(code[0:-1]) * length}.")
        print(f"Total complexity = {complexity}.")
        print()
          
    return complexity


if __name__ == "__main__":
    main()