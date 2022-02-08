import matplotlib as mpl
import matplotlib.pyplot as plt

from numpy import pi, sin, cos, linspace
from element import summation, multiply, delay, sys_port
from fir import Fir

freq = 1000
freq2 = 10000
freq3 = 23000

#1/100th of second at 100kHz
x = linspace(0, 0.1,10000)
y = sin(2*pi*freq*x) + 0.1 * cos(2*pi*freq2*x) * cos(2*pi*freq3*x)

fir = Fir([0.0027,    0.0021,    0.0025,    0.0025,    0.0021,    0.0011,   -0.0006,   -0.0028,   -0.0055,   -0.0083,\
          -0.0109,   -0.0128,   -0.0136,   -0.0127,   -0.0097,   -0.0043,    0.0034,    0.0135,    0.0256,    0.0390,\
           0.0530,    0.0666,    0.0790,    0.0893,    0.0966,    0.1003,    0.1003,    0.0966,    0.0893,    0.0790,\
           0.0666,    0.0530,    0.0390,    0.0256,    0.0135,    0.0034,   -0.0043,   -0.0097,   -0.0127,   -0.0136,\
          -0.0128,   -0.0109,   -0.0083,   -0.0055,   -0.0028,   -0.0006,    0.0011,    0.0021,    0.0025,    0.0025,\
           0.0021,    0.0027])

y_filt = fir.filter_data(y)
    
plt.plot(x, y, x, y_filt)
plt.show()




