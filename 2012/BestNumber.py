filename = "Data/StudentData/bestnumber.dat "
filename = "Data/JudgesData/bestnumber.dat "
file = open(filename, "r")
file.readline()
list = []
goal = (file.readline()).rstrip()
for line in file:
    list.append(float(line.rstrip()))
list.sort();
if goal == "biggest":
    biggest = 1
    divisions = []
    for element in list:
        if 1 > element > 0:
            divisions.append(element)
            list.remove(element)
    biggest = 1
    for number in list:
        biggest *= number
    for div in divisions:
        biggest /= div
    print(biggest)
if goal == "smallest":
    multiplications = []
    for number in list:
        if 0 < number < 1:
            multiplications.append(number)
            list.remove(number)
    smallest = list[0]
    for number in list[1:]:
        smallest /= number
    for multi in multiplications:
        smallest *= multi
    print(smallest)
file.close()
