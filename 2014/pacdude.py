from enum import Enum


def test_if_possible(maze, new_position, past_positions):

    maze_position = maze[new_position[1]][new_position[0]]
    if maze_position is "#":
        return False
    if new_position in past_positions[len(past_positions)-3-1:]:
        return False
    '''if new_position in past_positions:
        return False'''
    return True


class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    NONE = (0, 0)


possible_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def decide_where_to_go(maze, current_position, past_positions, direction):

    new_position = [current_position[0] + direction[1], current_position[1] + direction[0]]
    if test_if_possible(maze, new_position, past_positions):
        print("New position " + str(new_position))
        return new_position, direction
    #if current_position[1]
    for direc in range(4):
        new_position = [current_position[0] + possible_directions[direc][1],
                        current_position[1] + possible_directions[direc][0]]
        if test_if_possible(maze, new_position, past_positions):
            print("New position " + str(new_position))
            return new_position, possible_directions[direc]
    return current_position, [0, 0]


def solve_maze(maze, current_position, fruit):

    past_positions = [current_position]
    direction = (0, 0)
    print("Direction: ", end="")
    print(direction)
    print(current_position)
    print(fruit)
    while current_position != fruit:
        current_position, direction = decide_where_to_go(maze, current_position, past_positions, direction)
        if current_position is past_positions[-1]:
            break

        past_positions.append(current_position)
    print("Done")


with open('student_data/pacdude.dat', 'r') as file:

    mazes = int(file.readline())
    print(mazes)

    for problem in range(mazes):
        dimensions = (file.readline().rstrip()).split()
        maze = []
        O_position = []
        X_position = []

        for line in range(int(dimensions[1])):
            new_line = file.readline().rstrip()
            row = []
            print(new_line)
            for character in range(len(new_line)):
                new_character = new_line[character:character+1]
                if new_character is 'X':
                    X_position = [character, line]
                elif new_character is "O":
                    O_position = [character, line]
                elif new_character is 'G':
                    new_character = '#'
                row.append(new_character)
            maze.append(row)
        print()
        solve_maze(maze, O_position, X_position)

#https://github.com/neilzxu/pscstawinter2014/blob/master/src/pscstawinter2014/PacDude.java