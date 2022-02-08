import matplotlib as mpl
import matplotlib.pyplot as plt

from numpy import pi, sin, cos, linspace
from element import summation, multiply, delay, sys_port
from fir import Fir

freq = 1000
freq2 = 10000
freq3 = 23000

# 1/10th of second at 100kHz
x = linspace(0, 0.1, 10000)
y = sin(2*pi*freq*x) + 0.1*cos(2*pi*freq2*x) + 0.3*cos(2*pi*freq3*x)

# MATLAB Parks-McClellan optimal equiripple FIR filter
# n = 50;                      % Filter order
# f = [0 0.05 0.15 1];         % Frequency band edges
# a = [1  1  0 0];             % Amplitudes
# b = firpm(n,f,a);

fir = Fir([    0.0031,    0.0021,    0.0024,    0.0023,    0.0017,    0.0004,   -0.0015,   -0.0039,   -0.0066,   -0.0094,   \
              -0.0118,   -0.0132,   -0.0133,   -0.0115,   -0.0074,   -0.0009,    0.0080,    0.0191,    0.0320,    0.0458,   \
               0.0598,    0.0730,    0.0846,    0.0935,    0.0991,    0.1010,    0.0991,    0.0935,    0.0846,    0.0730,   \
               0.0598,    0.0458,    0.0320,    0.0191,    0.0080,   -0.0009,   -0.0074,   -0.0115,   -0.0133,   -0.0132,   \
              -0.0118,   -0.0094,   -0.0066,   -0.0039,   -0.0015,    0.0004,    0.0017,    0.0023,    0.0024,    0.0021,   \
               0.0031])

y_filt = fir.filter_data(y)
    
plt.plot(x, y, x, y_filt)
plt.show()




