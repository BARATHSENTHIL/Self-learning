class Calculator:

    # The init method is similar to constructor of a class which is used to initialize the member variables
    def __init__(self, x, y):
        self.operand1 = x
        self.operand2 = y

    def add(self):
        print self.operand1 + self.operand2

    def mul(self):
        print self.operand1 * self.operand2

cal_1 = Calculator(10, 20)
cal_1.add()

cal_2 = Calculator(110, 230)
cal_2.mul()
