fname = "pacdude.dat"
f = open(fname, 'r')


def pacMan(x, y):
    maze = []
    fruit = []
    for line in range(0,y,1):
        maze_line = f.readline().rstrip()
        maze_line_list = []
        for character in range(0,y,1):
            new_char = maze_line[character:character+1]
            maze_line_list.append(new_char)
            if new_char == 'X':
                fruit = [line,character]
        maze.append(maze_line_list)
        print(maze_line_list)
    print(fruit)


mazes = int(f.readline())

for x in range(0, mazes, 1):
    dimensions = f.readline().split()
    print(dimensions)
    pacMan(int(dimensions[0]), int(dimensions[1]))
