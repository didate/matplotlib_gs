import matplotlib.pyplot as pyplot

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
pyplot.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
pyplot.title("Square Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
pyplot.tick_params(axis='both', labelsize=14)

pyplot.show()
