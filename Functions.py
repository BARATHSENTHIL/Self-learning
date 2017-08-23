# function definition
def greetings():
    print("Hey, I am Barath")

def eurtoinr(euros):
    rupees = euros * 75
    print (rupees)

# function with return values
def netsalary (monthlygross):
    tax = monthlygross * 0.40
    netamount = monthlygross - tax
    return netamount

# function with default arguments
def get_gender(sex = 'Unknown'):
    if sex is 'm':
        sex = 'male'
    elif sex is 'f':
        sex = 'female'
    print (sex)

''' Keyword arguments for a fuction -> It is mainly used to pass limited no of arguments to the function and 
also change the order of the arguments 

 - Here name, action and item are the keywords arguments that take some values
 - using this keyword arguments the values and the order of arguments to the function can be changed
'''

def dumb_sentence(name = 'Barath', action = 'eats', item = 'chicken'):
    print name, action, item

''' Function to take flexible number of arguments 
 - In the function the parameter *args denotes in short as a list to hold multiple arguments. 
 The list can be used within the function to define what to do with each argument value
'''
def calculate_total(*args):
    total = 0
    for i in args:
        total += i
    print total


def personal_details(age = 0, name = '', sex = ''):
    print name, age, sex

#-------------------main----------------------
# calling the function

greetings()
eurtoinr(150)

salary_in_hand = netsalary(4000)
print "The salary i would get every month", salary_in_hand, "euros"

get_gender('m')
get_gender()

dumb_sentence()
dumb_sentence(action = 'marries', item = 'Radhika')

calculate_total(32)
calculate_total(35,658, 89)

''' Unpacking the arguments - Here the arguments are passed as values list and the (*) sign in the function parameter 
unpacks each value in the list and assigns to the corresponding variable in the function definition '''

values = [25, 'Barath', 'male']
personal_details(*values)