class Parent():

    def print_family_name(self):
        print ('VKN')

class Child(Parent):   # This syntax denotes that child class has inherited the Parent class

    def print_first_name(self):
        print ('Barath')

    def print_family_name(self):  # Override from Child class for Parent class method
        print ('Senthil')

B = Child()

B.print_first_name()
B.print_family_name()