class Course:

    def __init__(self, cc='unknown', d='unknown'):
        self.course_code = cc
        self.description = d

    def __str__(self):
        return self.course_code + ',' + self.description

    def input(self):
        self.course_code = input('Enter course code:')
        self.description = input('Enter description:')
        
    def display(self):
        print('Course code: ' + self.course_code)
        print('Description: ' + self.description)