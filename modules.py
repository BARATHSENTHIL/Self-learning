#-------------------main----------------------
# calling the function
import Functions

Functions.greetings()
Functions.eurtoinr(150)

salary_in_hand = Functions.netsalary(4000)
print "The salary i would get every month", salary_in_hand, "euros"

Functions.get_gender('m')
Functions.get_gender()

Functions.dumb_sentence()
Functions.dumb_sentence(action = 'weds', item = 'Radhika')

Functions.calculate_total(32)
Functions.calculate_total(35,658, 89)

''' Unpacking the arguments - Here the arguments are passed as values list and the (*) sign in the function parameter 
unpacks each value in the list and assigns to the corresponding variable in the function definition '''

values = [25, 'Barath', 'male']
Functions.personal_details(*values)

#---------------------------Lambda function---------------------
'''
The lambda function is a short and quick nameless function. It is used when certain functionality has to be done 
only once. The following code shows the use of lambda function
'''

result = lambda input_parameter: input_parameter + 50
print(result(10))
