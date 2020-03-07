import matplotlib.pyplot as pyplot

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:

    # Make a random walk, and plot the points
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    pyplot.scatter(rw.x_values, rw.y_values, c=point_numbers,
                   cmap=pyplot.cm.Blues, edgecolors='none', s=4)

    pyplot.show()

    keep_running = input("Make another walk ? (y/n): ")
    if keep_running == 'n':
        break
