import check_answers

f = check_answers.file_setup('gender_race', True)
f.readline()
racers = []


def printRacer():
    for element in racers[0]:
        print(element, end=" ")
    print()
    for element in racers[1]:
        print(element, end=" ")
    print()


for line in f:
    line = line.split()
    racers.append(line)
racers.sort(key=lambda x: x[1])
printRacer()
racers.sort(key=lambda x: x[2])
printRacer()
racers.sort(key=lambda x: x[2], reverse=True)

printRacer()
