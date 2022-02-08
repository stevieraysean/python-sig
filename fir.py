from numpy import pi
from element import summation, multiply, delay, sys_port, Element

class Fir():
    def __init__(self, coeffs=[]):
        self.coefficients = coeffs

        if (len(coeffs) < 2):
            return None #throw exception

        self.order = 0

        self.input0 = sys_port()
        self.mult0 = multiply(coeffs[0])

        self.fir_filter = {
            self.input0 : [self.mult0],
            self.mult0  : [None],
        }

        self.delays = []
        self.mults = []
        self.sums = []

        # create elements and store in lists
        for coeff in self.coefficients[1:]:
            self.order += 1
            self.delays.append(delay())
            self.mults.append(multiply(coeff))
            self.sums.append(summation())

        # assign routing
        for i in range(0, self.order):
            if i == 0:
                # inital connect output of input0 to first delat stage.
                self.fir_filter[self.input0].append(self.delays[i])

            # connect additional delay stages, to each other and each corresponing multiplier.
            if len(self.delays) > i+1 and self.delays[i+1] != None:
                self.fir_filter[self.delays[i]] = [self.mults[i], self.delays[i+1]]
            else:
                self.fir_filter[self.delays[i]] = [self.mults[i]]

            # connect multiplers to summation elements.
            self.fir_filter[self.mults[i]] = [self.sums[i]]

            # find the output of the previous stage and connect to summation element of this stage.
            for element in self.fir_filter.keys():
                if self.fir_filter.get(element) == [None]:
                    self.fir_filter[element] = [self.sums[i]]

            # set summation output to be the output of the filter, if no further stages added.
            self.fir_filter[self.sums[i]] = [None]


    def filter_data(self, y):
        y_filt = []

        for sample in y:
            # pass input sample in through input0, a fake element which acts as a input port.
            self.input0.set_input(sample)
            self.input0.clk()
            inputs = self.fir_filter.get(self.input0)

            # pass input sample in to first real elements in filter.
            for input_element in inputs:
                input_element.set_input(self.input0.output)

            # propogate sample along delay elements.
            for delay_element in self.delays:
                delay_outs = self.fir_filter.get(delay_element)
                for output in delay_outs:
                    output.set_input(delay_element.output)
                delay_element.clk()

            # multiply through coefficients.
            for multiplier_element in self.mults:
                multiplier_element.clk()
                mult_outs = self.fir_filter.get(multiplier_element)
                for output in mult_outs:
                    output.set_input(multiplier_element.output)     
            
            # sum all the multiplier outputs.
            for sum_element in self.sums:
                sum_element.clk()
                if self.fir_filter.get(sum_element) != [None]:
                    sum_outs = self.fir_filter.get(sum_element)
                    for output in sum_outs:
                        output.set_input(sum_element.output)
                else:
                    # output of the fir filter.
                    y_filt.append(sum_element.output)

        return y_filt


# initial prototype

# basic 3rd Order FIR
# input0 = sys_port()
# delay1 = delay()
# delay2 = delay()
# delay3 = delay()
# mult0 = multiply(0.2462)
# mult1 = multiply(0.0701)
# mult2 = multiply(0.0701)
# mult3 = multiply(0.2462)
# sum1 = summation()
# sum2 = summation()
# sum3 = summation()

# fir = {
#     input0 : [mult0, delay1],
#     mult0  : [sum1],
#     delay1 : [delay2, mult1],
#     mult1  : [sum1],
#     sum1   : [sum2],
#     delay2 : [delay3, mult2],
#     mult2  : [sum2],
#     sum2   : [sum3],
#     delay3 : [mult3],
#     mult3  : [sum3],
#     sum3   : [None]
# }

# fir = Fir([-0.0390, -0.0187, -0.0146, -0.0028, 0.0168, 
#            0.0433, 0.0736, 0.1039, 0.1298, 0.1472, 
#            0.1533, 0.1472, 0.1298, 0.1039, 0.0736, 
#            0.0433, 0.0168, -0.0028, -0.0146, -0.0187, -0.0390])
