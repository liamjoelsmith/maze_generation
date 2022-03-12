import matplotlib.pyplot as plt
import numpy as np
import os
import glob
from PIL import Image

# remove any .pngs from frames folder
files = glob.glob('frames/*')
for f in files:
    os.remove(f)

# maze dimensions
LENGTH = 21
WIDTH = 11

PAUSE_LENGTH = 0.001  # seconds

# create empty maze
the_map = np.zeros(LENGTH * WIDTH).reshape(LENGTH, WIDTH)

# interactive matplotlib plotting mode
frame = plt.gca()
plt.ion()
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([])

# generate maze
i = 0  # frame number, used to keep order of images when generating gif
for row in range(0, LENGTH, 2):
    for col in range(0, WIDTH, 2):
        the_map[row][col] += 1
        plt.imshow(the_map, cmap="Greys")
        plt.pause(PAUSE_LENGTH)

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
        plt.pause(PAUSE_LENGTH)

        chart = frame.get_figure()
        chart.savefig("frames/"+str(i))

        i += 1  # update frame number

# open frames
frames = []
imgs = glob.glob("frames/*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# create repeating GIF
frames[0].save('binary_tree_maze.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)

plt.ioff()
plt.imshow(the_map, cmap="Greys")
plt.show()
