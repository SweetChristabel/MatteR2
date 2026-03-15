import numpy as np
import matplotlib.pyplot as plt
#y' = 10-y^0.5
def f(y):
    return 10 - np.sqrt(y)

n = 200 #antall punkter
x = np.zeros(n)
y = np.zeros(n)
dx = (4-2)/n #steglengde i intervallet mellom x=2 og x=4
x[0] = 2 # x til startpunktet
y[0] = 5 # y til startpunktet

for i in range (n-1):
    x[i+1] = x[i] + dx
    y[i+1] = y[i] + f(y[i])

plt.plot(x,y)
plt.show()
