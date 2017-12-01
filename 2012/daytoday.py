import datetime

import check_answers

current_file = check_answers.file_setup("daytoday", True)
current_file.readline()
for line in current_file:
    line = line.split()
    Date1 = datetime.date(int(line[2]), int(line[0]), int(line[1]))
    Date2 = datetime.date(int(line[5]), int(line[3]), int(line[4]))
    difference = Date2 - Date1
    days = difference.days
    print(days - 1)
