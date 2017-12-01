import check_answers

output = []
file_name = 'conversions'
current_file = check_answers.file_setup(file_name, False)
current_file.readline()
output = []


def crash(numbers):
    ans = numbers[0] / 4 + 7 * numbers[1]
    check_answers.special_print(("%.2f" % ans), output)


def dash(numbers):
    ans = (numbers[0] + numbers[1] ** 2) / (numbers[0] + 1 / numbers[1]) + numbers[0] / numbers[1]
    check_answers.special_print(("%.2f" % ans), output)


def mash(numbers):
    ans = 1 / (1 / numbers[0] - 1 / numbers[1])
    check_answers.special_print(("%.2f" % ans), output)


def trash(numbers):
    ans = (4 / (numbers[0] / numbers[1])) * ((1 + (5 / (numbers[2] + numbers[3]))) / (numbers[0])) ** .5 \
          - numbers[0] / (numbers[2] + numbers[3])
    check_answers.special_print(("%.2f" % ans), output)


for line in current_file:
    line = line.split()
    for x in xrange(len(line)):
        line[x] = float(line[x])
    crash(line)
    dash(line)
    mash(line)
    trash(line)
    check_answers.special_print((""), output)
check_answers.check(file_name, output)
