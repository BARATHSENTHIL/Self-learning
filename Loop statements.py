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