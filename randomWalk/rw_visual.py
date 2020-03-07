import matplotlib.pyplot as pyplot

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
# while True:

# Make a random walk, and plot the points
rw = RandomWalk(50000)
rw.fill_walk()
# Set the size of the plotting window.
pyplot.figure(figsize=(10, 6))

point_numbers = list(range(rw.num_points))
pyplot.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=pyplot.cm.Blues, edgecolors='none', s=1)

# Emphasize the first and last points
pyplot.scatter(0, 0, c='green', edgecolors='none', s=5)
pyplot.scatter(rw.x_values[-1], rw.y_values[-1],
               c='red', edgecolors='none', s=5)

# Remove the axes.
pyplot.axes().get_xaxis().set_visible(False)
pyplot.axes().get_yaxis().set_visible(False)

# Show plot
pyplot.show()

# keep_running = input("Make another walk ? (y/n): ")
# if keep_running == 'n':
#     break
