class Student:

      # The variable University is Class variable which remains same for all objects of the class
      University = 'Technische Hochschule Ingolstadt'

      def __init__(self, name):

          # The variable student name is known as Instance variable which is unique for each object the class
          self.studentname = name


stud1 = Student('Barath')
stud2 = Student('Karthik')

print stud1.studentname,  stud1.University
print stud2.studentname,  stud2.University

