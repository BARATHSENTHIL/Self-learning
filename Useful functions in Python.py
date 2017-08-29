#-------------unpacking lists and tuples-----------------
''' list = ['Aug 28', 'Bauget', 0.49]  -> the list contains purchase date, item name and price.
To access each, we may use list[0] or list[1] etc. Alternatively it can be done as
'''

date, name, price = ['Aug 28', 'Bauget', 0.49]
print name

'''
Similarly to access only the elements excluding the first and last elements it can be given as

first, *middle, last = [53, 68, 89, 75, 65, 32]. So *middle has [68, 89, 75, 65].

The expression *middle is supported only at python versions > 3.0
'''

#-------------------zip function-----------------
# The zip function is used to bundel each element from the list with elements in other list provided both lists
# are of same length

first_name = ['Senthil', 'Poornima', 'Barath', 'Krishna', 'Febi']
last_name = ['Natesan', 'Pandarinathan','senthil', 'senthil', 'kullan']

name = zip(first_name, last_name)

for ind in name:
    print ind

#---------------------------------------------
# Dictionary - Keys and values

car_model = {'AUDI A7':' as EGO car', 'BMW X1':' as Rear traffic', 'MAN Semi-trailer':' as Front traffic'}

for key,value in car_model.items():
    print (key + value)

#---------------------------Lambda function---------------------
'''
The lambda function is a short and quick nameless function. It is used when certain functionality has to be done 
only once. The following code shows the use of lambda function
'''

result = lambda input_parameter: input_parameter + 50
print(result(10))

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

#--------------Struct--------------
# Struct is used to represent the user data into equivalent byte format

from struct import *

# pack function is used to transform numerical data into bytes of the specified format like integer, integer, float
packed_data = pack('iif', 20, 54, 45.32)
print (packed_data)

# unpack function restores bytes from specified format to numerical value
unpacked_data = unpack('iif', packed_data)
print (unpacked_data)

#---------------Map function ---------------
# map function is used to perform certain calculation or function on lists

data = [20, 56, 78]

def squared_output (data):
    return data * data

# Map function has two paramaters:
# > first parameter denotes the function to be performed on the list
# > second parameter denotes the data or list on which the function is applied
print (list(map (squared_output, data)))
