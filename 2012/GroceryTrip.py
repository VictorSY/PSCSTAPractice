filename = "Data/StudentData/grocery.dat"
filename = "Data/JudgesData/grocery2.dat"  # grocery1 or 2
file = open(filename, 'r')
listLength = int(file.readline())
Suman = []
for x in range(listLength):
    Suman.append(file.readline().rstrip())
listLength = int(file.readline())
Rajesh = []
for x in range(listLength):
    Rajesh.append(file.readline().rstrip())
common = set(Suman) & set(Rajesh)
if len(common) > 0:
    print("Tomatoes for youza!")
else:
    print("No tomatoes for youza!")
