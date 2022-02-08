n = 51;                         % Filter order
f = [0 0.05 0.15 1];         % Frequency band edges
a = [1  1  0 0];               % Amplitudes
b = firpm(n,f,a);
bb = firls(n,f,a);
fvtool(b,1)
b



