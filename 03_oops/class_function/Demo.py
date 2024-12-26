class Student:
    def profile(self):
        print('name : ', 'Python', '\nsemester : ', 8, '\nstream : ', 'IT')

sub = Student()

print('<------Method calling using object------>')
sub.profile()
print('<------Method calling using passing object as parameter------>')
# self is object
Student.profile(sub)