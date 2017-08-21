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