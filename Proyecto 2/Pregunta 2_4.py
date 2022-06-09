from numpy import log10, abs
import matplotlib.pyplot as plt

I_n = [(-0.05016317138743477), (0.01907311891587814), (0.23967006174524833), (-0.05879611592057261), (-7.690834928867627e-05),
(0.03147392648042156), (-0.07210022973446586), (0.006380455088201409), (-0.37572177776273086), (0.0005974985486188796)]
I = 0
L = []
for i in I_n:
    log_I = log10(abs(I - i))
    L.append(log_I)
print(L)

LN = [10,50,100,500,1000,5000,10000,50000,100000,500000]
LogN = []
for i in LN:
    log_N = log10(i)
    LogN.append(log_N)
print(LogN)

plt.plot(LogN, L, label="Diferencia")
plt.legend()
plt.show()