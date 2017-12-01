import check_answers

output = []
file_name = 'cds'
current_file = check_answers.file_setup(file_name, False)
while True:
    cds_per_person = current_file.readline().rstrip().split()
    for element in range(len(cds_per_person)):
        cds_per_person[element] = int(cds_per_person[element])
    if cds_per_person[0] == 0 and cds_per_person[1] == 0:
        break
    Jack = []
    Jill = []
    for element in range(cds_per_person[0]):
        Jack.append(int(current_file.readline()))
    for element in range(cds_per_person[1]):
        Jill.append(int(current_file.readline()))
    same_cds = 0
    for element in Jack:
        if element in Jill:
            Jill.remove(element)
            same_cds += 1
    check_answers.special_print(same_cds, output)
check_answers.check(file_name, output)
