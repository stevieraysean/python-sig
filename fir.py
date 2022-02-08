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



        #create elements and store in lists
        for coeff in self.coefficients[1:]:
            self.order += 1
            self.delays.append(delay())
            self.mults.append(multiply(coeff))
            self.sums.append(summation())

        # print(self.delays)
        # print(self.mults)
        # print(self.sums)

        #assign routing
        for i in range(0, self.order):
            if i == 0:
                self.fir_filter[self.input0].append(self.delays[i])

            if len(self.delays) > i+1 and self.delays[i+1] != None:
                self.fir_filter[self.delays[i]] = [self.mults[i], self.delays[i+1]]
            else:
                self.fir_filter[self.delays[i]] = [self.mults[i]]

            self.fir_filter[self.mults[i]] = [self.sums[i]]

            for element in self.fir_filter.keys():
                if self.fir_filter.get(element) == [None]:
                    self.fir_filter[element] = [self.sums[i]]

            self.fir_filter[self.sums[i]] = [None]


        print("filter=")
        for element in self.fir_filter.keys():
            if isinstance(element, multiply):
                print("multiply = ", element.get_co(), element,self.fir_filter.get(element))
            else:
                print(element, self.fir_filter.get(element))



    def filter_data(self, y):
        y_filt = []

        for sample in y:
            self.input0.set_input(sample)

            for input_element in self.fir_filter.keys():
                output_elements = self.fir_filter.get(input_element)        
            
                for element in output_elements:
                    if element != None:
                        element.set_input(input_element.output)
                    else:
                        y_filt.append(input_element.output)

            for element in self.fir_filter.keys():
                element.clk()

        return y_filt


# # basic 3rd Order FIR
# input0 = sys_port()
# mult0 = multiply(0.2462)


# delay1 = delay()
# delay2 = delay()
# delay3 = delay()

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
