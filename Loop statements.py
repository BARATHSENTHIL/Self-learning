# if...elif...else statement
age = 25

if age < 18:
    print("Not eligible to marry")
elif age > 30:
    print ("Too old to marry")
else:
    print age

# for loop
myfamily = ['Senthil', 'Poornima', 'Barath', 'Krishna','Febi']

for mem in myfamily:
    print (mem)
    print (len(mem))

#Range

for x in range(10):
    print(x)

for y in range(5,10):
    print (y)

for x in range (10,20,2):
    print(x)

# While loop
temp = 5
while temp < 10:
    print (temp)
    temp += 1 # increment statement

# Break statement
Magicnumber = 25

for n in range(10,100):
    if n is Magicnumber:
      print(n, "is the magic number")    # This statement is used to print number and string together
      break
    else:
      print(n)

oddnumbers = [3, 5, 7, 9]

for m in range(1,10):
    if m in oddnumbers:
        continue
    print (m)

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