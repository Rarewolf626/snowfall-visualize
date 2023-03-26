import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# define the colors for the colormap
colors = np.array([
    [0.2, 0.0, 0.6],  # dark purple
    [0.4, 0.0, 1.0],  # light purple
    [0.3, 0.0, 1.0],  # medium purple
    [0.2, 0.0, 1.0],  # lighter blue-purple
    [0.1, 0.0, 1.0],  # light blue
    [0.0, 0.0, 1.0],  # blue
    [0.0, 0.5, 1.0],  # light blue-green
    [0.0, 1.0, 1.0],  # cyan
    [0.5, 1.0, 0.5],  # light green
    [1.0, 1.0, 0.0],  # yellow
    [1.0, 0.5, 0.0],  # orange
    [1.0, 0.0, 0.0],  # red
])

# create the colormap with a smooth gradient
cmap = LinearSegmentedColormap.from_list('my_colormap', colors, N=256)

# plot a sample image using the colormap
data = np.random.rand(10, 10)
plt.imshow(data, cmap=cmap)

# add a smooth colorbar
plt.colorbar()

plt.show()
