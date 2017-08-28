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

#------------Sorting a Dictionary---------------
Stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

# The zip function is used to sort the dictionary

# Min and Max values in dictionary
print(min(zip(Stocks.values(), Stocks.keys())))

print(max(zip(Stocks.values(), Stocks.keys())))

# Sorting the elements in dictionary based on values
print(sorted(zip(Stocks.values(), Stocks.keys())))

# Sorting the elements in dictionary based on keys
print(sorted(zip(Stocks.keys(), Stocks.values())))