import numpy as np
import matplotlib.pyplot as pyplot

# datas
x = np.linspace(-5, 5, 100)
y = [i**3 for i in x]

fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.grid(True)

pyplot.plot(x, y, 'b', label='f(x)=x^3')
pyplot.text(3.2, 25, 'f(x)')
pyplot.legend(loc='upper left')

pyplot.show()
