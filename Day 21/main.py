# Input is so short this time I didn't bother to parse it, but just typed it in manually.
input_codes = ["029A", "980A", "179A", "456A", "379A"] #sample input numbers
# input_codes = ["780A", "539A", "341A", "189A", "682A"] #real input numbers

import time
from functools import lru_cache

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

number_of_robots = 2

def main():

    answer1 = part1()
    answer2 = part2()

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
    # print(f"End position: {end_position}")
    while position != end_position:
        # print(f"Starting while loop with position {position}.")
        change_y = end_position[0]-position[0]
        change_x = end_position[1]-position[1]
        # print(f"Change in y is {change_y} and change in x is {change_x}")
        if change_x > 0:
            next_position = (position[0], position[1]+1)
            key_moves += ">"
        elif change_y > 0:
            next_position = (position[0]+1, position[1])
            key_moves += "v"
        elif change_y < 0:
            next_position = (position[0]-1, position[1])
            key_moves += "^"
        elif change_x < 0:
            next_position = (position[0], position[1]-1)
            key_moves += "<"
        position = next_position
    return key_moves, end_position

@lru_cache
def directional_move(position, end_position):
    key_moves = ""
    end_position = directional_pad[end_position]
    print(f"End position: {end_position}")
    while position != end_position:
        print(f"Starting while loop with position {position}.")
        change_y = end_position[0]-position[0]
        change_x = end_position[1]-position[1]
        print(f"Change in y is {change_y} and change in x is {change_x}")
        if change_x > 0:
            next_position = (position[0], position[1]+1)
            key_moves += ">"
        elif change_y > 0:
            next_position = (position[0]+1, position[1])
            key_moves += "v"
        elif change_x < 0:
            next_position = (position[0], position[1]-1)
            key_moves += "<"
        elif change_y < 0:
            next_position = (position[0]-1, position[1])
            key_moves += "^"
        
        position = next_position

    return key_moves, end_position

def part1():
    
#### Key insight: Don't need to keep the entirety of the sequence in memory. Each move, for instance
#### "v>vA" is independent of other moves, and there are a very limited number of moves possible.
#### Thus, just keep a count of how many times each move is needed at every level.


    all_moves = {}
    new_moves = []
    for code in input_codes:
        move_list = ""
        position = (3,2)
        for i, char in enumerate(code):
            new_moves_list, position = keypad_move(position, char)
            move_list += new_moves_list + "A"
            # print(f"{move_list=}")
            # print()   
        new_moves.append(move_list)
    all_moves["list0"] = new_moves

    print("FINISHED FIRST ROBOT")

    for i in range(number_of_robots):
        print(f"Starting robot number {i+2}")
        new_moves = []
        for move in all_moves[f"list{i}"]:
            move_list = ""
            position = (0,2)
            for char in move:
                new_move_list, position = directional_move(position, char)
                move_list += new_move_list + "A"
                # print(f"{move_list=}")
                # print()
            new_moves.append(move_list)   

        print(f"{new_moves=}")
        all_moves[f"list{i+1}"] = new_moves

  

    complexity = 0
    for i, move in enumerate(all_moves[f"list{number_of_robots}"]):
        complexity += len(move) * int(input_codes[i][0:-1])
        print(f"Move is {move}.")
        print(f"Input = {input_codes[i]} and length of moves = {len(move)}.")
        print(f"Complexity adds {int(input_codes[i][0:-1])} * {len(move)} = {int(input_codes[i][0:-1]) * len(move)}.")
        print(f"Total complexity = {complexity}.")
        print()
        
    
    
    return complexity


def part2():
    return None


if __name__ == "__main__":
    main()