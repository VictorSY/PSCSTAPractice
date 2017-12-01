def check(file_name, text):
    file = open("Data/JudgesData/" + file_name + ".out", 'r')
    list_element = 0
    all_good = True
    for line in file:
        if not (line.rstrip() == str(text[list_element])):
            print("Wrong output on line %s, you got %s should be %s" % (
                list_element + 1, text[list_element], line.rstrip()))
            all_good = False
        list_element += 1
    if all_good:
        print("All good, nice work!")


def file_setup(filename, is_student):
    if is_student:
        current_file = open("Data/StudentData/" + filename + ".dat", 'r')
    else:
        current_file = open("Data/JudgesData/" + filename + ".dat", 'r')
    return current_file


def special_print(text, list):
    print(text)
    list.append(text)
