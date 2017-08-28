import threading

# Threads are used to execute multiple process concurrently
# It is used for applications where the process are independent of each other

class Messenger(threading.Thread):
    def run(self):
# the underscore denotes the looping variable. This syntax is used when it is not used for further calculations
        for _ in range(10):
            print (threading.currentThread().getName())

person1 = Messenger(name = 'Sending message')
person2 = Messenger(name = 'Receiving message')

# The function start() calls the run method to execute the thread
person1.start()
person2.start()