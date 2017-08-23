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



#-------------------main----------------------
# calling the function
greetings()
eurtoinr(150)

salary_in_hand = netsalary(4000)
print "The salary i would get every month", salary_in_hand, "euros"

get_gender('m')
get_gender('f')
get_gender()