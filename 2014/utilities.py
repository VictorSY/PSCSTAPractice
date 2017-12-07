class Utilities:
    def __init__(self, name, is_student):
        self.output = []
        if is_student:
            self.input_file = open('student_data/%s.dat' % name, 'r')
        else:
            self.input_file = open('judges_data/%s.dat', 'r')

    def print(self, values, end='\n'):
        print(values, end=end)
        self.output.append('%s%s' % (values, end))
