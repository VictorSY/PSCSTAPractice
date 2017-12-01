import check_answers

filedat = 'average'
filename = ("Data/StudentData/%s.dat" % filedat)
filename = ("Data/JudgesData/%s.dat" % filedat)
file = open(filename, 'r')
file.readline()
output = []
for line in file:
    line = line.split(" ")
    length = float(line[0])
    del line[0]
    average = 0
    for element in range(0, int(length), 1):
        line[element] = int(line[element].rstrip())
    average = sum(line) / length
    above_average = 0
    for element in line:
        if element > average:
            above_average += 1
    above_average /= length / 100
    will_print = ("%.3f%s" % (above_average, '%'))
    print(will_print)
    output.append(will_print)
check_answers.check(filedat, output)
