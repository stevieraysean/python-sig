import matplotlib as mpl
import matplotlib.pyplot as plt

from numpy import pi, sin, cos, linspace
from element import summation, multiply, delay, sys_port
from fir import Fir


freq = 40000
freq2 = 1500

x = linspace(0, 0.1,10000)
y = sin(2*pi*freq*x)# + 0.1 * cos(2*pi*freq2*x)




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


fir = Fir([0.0027,    0.0021,    0.0025,    0.0025,    0.0021,    0.0011,   -0.0006,   -0.0028,   -0.0055,   -0.0083,\
          -0.0109,   -0.0128,   -0.0136,   -0.0127,   -0.0097,   -0.0043,    0.0034,    0.0135,    0.0256,    0.0390,\
           0.0530,    0.0666,    0.0790,    0.0893,    0.0966,    0.1003,    0.1003,    0.0966,    0.0893,    0.0790,\
           0.0666,    0.0530,    0.0390,    0.0256,    0.0135,    0.0034,   -0.0043,   -0.0097,   -0.0127,   -0.0136,\
          -0.0128,   -0.0109,   -0.0083,   -0.0055,   -0.0028,   -0.0006,    0.0011,    0.0021,    0.0025,    0.0025,\
           0.0021,    0.0027])



#print(fir.fir_filter)


y_filt = fir.filter_data(y)

# for sample in y:
#     input0.set_input(sample)

#     for input_element in fir.keys():
#         output_elements = fir.get(input_element)        
	
#         for element in output_elements:
#             if element != None:
#                 element.set_input(input_element.output)
#             else:
#                 y_filt.append(input_element.output)

#     for element in fir.keys():
#         element.clk()

    
plt.plot(x, y, x, y_filt)
plt.show()




