import check_answers

f = check_answers.file_setup('trees', True)
f.readline()
opinion = []
for line in f:
    line = line.split()
    opinion.append([int(line[0]), int(line[1])])
opinion.sort(key=lambda x: x[1])
''''key=lambda x: x[1]'''
tree = 101
total = 0
print(opinion)
same = 1
for person in opinion:
    if person[1] == tree:
        same += 1
    elif same > 1:
        total += same
        same = 1
    tree = person[1]
print(total)
