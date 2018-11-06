import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

fig = plt.figure()

ax = plt.axes()

ax = ax.set(xlabel='x', ylabel='f(x) = x^3 + x^2 - 10')

x = np.linspace(-20, 20, 1000)

plt.axis([-20, 20, -20, 20])

plt.plot(x, ((x * x * x) + (4 * x * x) - 10), color = '0.75')

plt.plot(x, x-x)

plt.plot(y, y-y)

plt.title("Analyse numerique : TP1")

plt.show()

