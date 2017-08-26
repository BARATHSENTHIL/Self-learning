class Parent():

    def print_family_name(self):
        print ('VKN')

class Child():   # This syntax denotes that child class has inherited the Parent class

    def print_first_name(self):
        print ('Barath')

# The class Myname inherits the properties from both parent and child class
class Myname(Parent,Child):
    pass # Pass is keyword that simply executes the existing functionality

B = Myname()

B.print_first_name()
B.print_family_name()