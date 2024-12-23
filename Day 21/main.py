FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time

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

input_numbers = [29, 980, 179, 456, 379]


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
    codes = []
    for row in data:
        new_line = []
        for item in row.strip():
            new_line.append(item)
        codes.append(new_line)
    return codes


def part1(data):

    robot1_start = (3,2)
    position = robot1_start

    at_keypad_move = []
    for code in data:
        key_moves = ""
        for key in code:
            # print(f"Key = {key}")
            end_position = keypad[key]
            # print(f"End position: {end_position}")
            while position != end_position:
                # print(f"Starting while loop with position {position}.")
                change_y = end_position[0]-position[0]
                change_x = end_position[1]-position[1]
                # print(f"Change in y is {change_y} and change in x is {change_x}")
                if change_y < 0:
                    next_position = (position[0]-1, position[1])
                    key_moves += "^"
                elif change_x > 0:
                    next_position = (position[0], position[1]+1)
                    key_moves += ">"
                elif change_y > 0:
                    next_position = (position[0]+1, position[1])
                    key_moves += "v"
                elif change_x < 0:
                    next_position = (position[0], position[1]-1)
                    key_moves += "<"
                
                position = next_position
                # print(f"Current list of moves: {key_moves}")
            key_moves += "A"
            # print(f"Current list of moves: {key_moves}")
        at_keypad_move.append(key_moves)

    print(at_keypad_move[0])


    robot2_start = (0,2)
    position = robot2_start

    second_robot_moves = []
    for move in at_keypad_move:
        key_moves = ""
        for char in move:
            print(f"Key = {key}")
            end_position = directional_pad[char]
            print(f"End position: {end_position}")
            while position != end_position:
                print(f"Starting while loop with position {position}.")
                change_y = end_position[0]-position[0]
                change_x = end_position[1]-position[1]
                print(f"Change in y is {change_y} and change in x is {change_x}")
                if change_y > 0:
                    next_position = (position[0]+1, position[1])
                    key_moves += "v"
                elif change_x > 0:
                    next_position = (position[0], position[1]+1)
                    key_moves += ">"
                elif change_x < 0:
                    next_position = (position[0], position[1]-1)
                    key_moves += "<"
                elif change_y < 0:
                    next_position = (position[0]-1, position[1])
                    key_moves += "^"
                
                position = next_position
                print(f"Current list of moves: {key_moves}")
            key_moves += "A"
            print(f"Current list of moves: {key_moves}")
        second_robot_moves.append(key_moves)
        
    print(second_robot_moves[0])    
    
    me_start = (0,2)
    position = me_start
    me_moves = []
    for move in second_robot_moves:
        key_moves = ""
        for char in move:
            end_position = directional_pad[char]
            while position != end_position:
                change_y = end_position[0]-position[0]
                change_x = end_position[1]-position[1]
                if change_y > 0:
                    next_position = (position[0]+1, position[1])
                    key_moves += "v"
                elif change_x > 0:
                    next_position = (position[0], position[1]+1)
                    key_moves += ">"
                elif change_x < 0:
                    next_position = (position[0], position[1]-1)
                    key_moves += "<"
                elif change_y < 0:
                    next_position = (position[0]-1, position[1])
                    key_moves += "^"
                
                position = next_position
            key_moves += "A"
        me_moves.append(key_moves)
    
    print(me_moves[0])
    print()
    print()

    complexity = 0
    for i, move in enumerate(me_moves):
        print(f"Move is {move}.")
        print(f"Input = {input_numbers[i]} and length of me_moves = {len(move)}.")
        print()
        complexity += len(move) * input_numbers[i]
    
    return complexity


def part2(data):
    return None


if __name__ == "__main__":
    main()