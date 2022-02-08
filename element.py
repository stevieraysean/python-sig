class Element(object):
    def __init__(self):
        self.input = 0.
        self.output = 0.

    def clk(self):
        pass

    def set_input(self, values):
        self.input = values


class summation(Element):
    def set_input(self, value):
        self.input = self.input + value

    def clk(self):
        self.output = self.input
        self.input = 0.

class multiply(Element):
    #def set_coeff(self, coeff):
    def __init__(self, coeff):
        self.input = 0.
        self.output = 0.
        self.coefficient = coeff

    def get_co(self):
        return self.coefficient

    def clk(self):
        self.output = self.input * self.coefficient

class delay(Element):
    def clk(self):
        self.output = self.input

class sys_port(Element):
    def clk(self):
        self.output = self.input


