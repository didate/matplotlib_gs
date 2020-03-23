import numpy as np
import matplotlib.pyplot as pyplot

# datas
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
c = np.cos(x)


fig = pyplot.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.grid(True)

pyplot.plot(x, y, 'r', label='A=sin(x)')
pyplot.plot(x, 2*y, 'b', label='B=2sin(x)')
pyplot.plot(x, c, 'c', label='C=cos(x)')
pyplot.plot(x, 2*c, 'y', label='D=2cos(x)')


pyplot.legend(loc='upper left')

pyplot.show()
