filename = "Data/StudentData/factorial.dat "
filename = "Data/JudgesData/factorial.dat "
file = open(filename, 'r')
factorialNumber = int(file.readline())
factorial = 1
for x in range(factorialNumber, 1, -1):
    factorial *= x
print(factorial)
file.close()
