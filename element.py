class Element(object):
    def __init__(self):
        self.input = 0.
        self.output = 0.

    def clk(self):
        self.output = self.input

    def set_input(self, values):
        self.input = values


class summation(Element):
    def __init__(self):
        self.input = 0.
        self.output = 0.
        self.input_count = 0

    def set_input(self, value):
        self.input = self.input + value

    def clk(self):
        self.output = self.input
        self.input = 0.


class multiply(Element):
    def __init__(self, coeff):
        self.input = 0.
        self.output = 0.
        self.coefficient = coeff

    def get_co(self):
        return self.coefficient

    def clk(self):
        #print(self.input, "*", self.coefficient, "=",self.input * self.coefficient) #TODO: delete debug
        self.output = self.input * self.coefficient


class delay(Element):
    def clk(self):
        self.output = self.input


class sys_port(Element):
    def clk(self):
        self.output = self.input


