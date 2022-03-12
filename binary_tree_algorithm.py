import matplotlib.pyplot as plt
import numpy as np

# maze dimensions
width = 21
length = 11

# create empty maze
the_map = np.zeros(width*length).reshape(width, length)

plt.ion()

# generate maze
for row in range(0, width+1, 2):
    for col in range(0, length+1, 2):
        the_map[row][col] += 1
        plt.imshow(the_map, cmap="Greys")
        plt.pause(0.05)

        # if both neighbours above and to the left exist
        # pick random one to connect with
        if the_map[row-2][col] > 0 and the_map[row][col-2] > 0:
            choice = np.random.choice(2)
            if choice:
                the_map[row - 1][col] += 1
            else:
                the_map[row][col - 1] += 1
        # if only neighbour is above, connect with this
        elif the_map[row - 2][col] > 0:
            the_map[row - 1][col] += 1
        # if only neighbour is to the left, connect with this
        elif the_map[row][col - 2] > 0:
            the_map[row][col - 1] += 1

        plt.imshow(the_map, cmap="Greys")
        plt.pause(0.05)

print(the_map)

plt.imshow(the_map, cmap="Greys")
plt.show()
