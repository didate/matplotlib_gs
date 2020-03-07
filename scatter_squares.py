import matplotlib.pyplot as pyplot

x_values = list(range(1, 1001))

y_values = [x**2 for x in x_values]

pyplot.scatter(x_values, y_values, c=y_values,
               cmap=pyplot.cm.Blues, edgecolors='none', s=4)

# set chart title and label axes.
pyplot.title("Squares Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
pyplot.axis([0, 1100, 0, 1100000])
pyplot.ticklabel_format(useOffset=False, style='plain')

pyplot.savefig('squares_plot.png', bbox_inches='tight')
