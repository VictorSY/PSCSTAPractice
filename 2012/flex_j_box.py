import check_answers

f = check_answers.file_setup('flexjbox', True)
f.readline()
for line in f:
    line = line.split()
    total_y = int(line[0])
    total_x = int(line[1])
    y_pos = int(line[2])
    x_pos = int(line[3])
    for y in range(total_y):
        for x in range(total_x):
            if x == x_pos and y == y_pos:
                print("J", end="")
            else:
                print("*", end="")
        print("")
    print("")
