import matplotlib as mpl
import matplotlib.pyplot as plt

from numpy import pi, sin, cos, linspace
import abc


freq = 20

x = linspace(0, 2*pi*freq,48000)
y = sin(x) + 0.2 * cos(x*100) + 0.7 * sin(x*27)


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

    def clk(self):
        self.output = self.input * self.coefficient

class delay(Element):
    def clk(self):
        self.output = self.input

class sys_port(Element):
    def clk(self):
        self.output = self.input

input0 = sys_port()
delay0 = delay()
delay1 = delay()
delay2 = delay()
mult0 = multiply(0.25)
mult1 = multiply(0.25)
mult2 = multiply(0.25)
mult3 = multiply(0.25)
sum1 = summation()
sum2 = summation()
sum3 = summation()


fir = {
    input0 : [delay0, mult0],	
    delay0 : [delay1, mult1],
    mult0  : [sum1],
    delay1 : [delay2, mult2],
    mult1  : [sum1],
    sum1   : [sum2],
    delay2 : [mult3],
    mult3  : [sum3],
    sum2   : [sum3],
    sum3   : [None]
}


y_filt = []

for sample in y:
    input0.set_input(sample)

    for input_element in fir.keys():
        output_elements = fir.get(input_element)        
	
        for element in output_elements:
            if element != None:
                element.set_input(input_element.output)
            else:
                y_filt.append(input_element.output)

    for element in fir.keys():
        element.clk()
    
    #for element in fir.keys():
    #    print(element.output)

    #print('--------')
    
plt.plot(x, y, x, y_filt)
plt.show()




