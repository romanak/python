import matplotlib.pylab as plt
import math

x = []
y = []
y2 = []
y3 = []
exp = []
loga = []
logl = []

for i in range(1, 31):
    x.append(i)
    y.append(i)
    y2.append(i**2)
    y3.append(i**3)
    exp.append(1.5**i)
    loga.append(math.log2(i))
    logl.append(i * math.log2(i))

plt.figure('A relationship between a linear and logarithmic functions')
plt.clf()
plt.xlabel('Abscissa')
plt.ylabel('Ordinate')
plt.title("Linear and logarithmic")
plt.ylim(0, 10)
plt.plot(x, y, 'b-', label = 'Linear', linewidth = 1.0)
plt.plot(x, loga, 'ro', label = 'Logarithmic', linewidth = 2.0)
plt.legend(loc = 'upper right')

plt.figure('A relationship between a log-linear and quadratic functions')
plt.clf()
plt.xlabel('Abscissa')
plt.ylabel('Ordinate')
plt.title("Log-linear and quadratic")
plt.ylim(0, 400)
plt.plot(x, logl, 'g^', label = 'Linear-Logarithmic', linewidth = 3.0)
plt.plot(x, y2, 'r--', label = 'Quadratic', linewidth = 4.0)
plt.legend(loc = 'upper left')

plt.figure('A relationship between a cubic and exponential functions')
plt.clf()
plt.xlabel('Abscissa')
plt.ylabel('Ordinate')
plt.title("Cubic and exponential")
#plt.ylim(0, 400)
plt.plot(x, y3, 'b-', label = 'Cubic', linewidth = 3.0)
plt.plot(x, exp, 'r--', label = 'Exponential', linewidth = 4.0)
plt.legend(loc = 'upper left')
plt.yscale('log')

plt.show()