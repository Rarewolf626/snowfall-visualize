import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

import matplotlib.colors as mcolors

colorscale = [
    (0, (0, 0, 0)),
    (0.01, (0, 1, 1)),
    (0.4, (0, 0, 1)),
    (0.6, (130/255, 0, 255/255)),
    (0.8, (1, 0, 1)),
    (1, (1, 1, 1))
]

cmap = mcolors.LinearSegmentedColormap.from_list('custom', colorscale)


# create a figure with a colorbar
fig, ax = plt.subplots(figsize=(6, 1))
cb = plt.colorbar(plt.imshow(np.linspace(0, 1, 256).reshape(1, -1), cmap=cmap), cax=ax, orientation='horizontal')

# set the colorbar labels and tick locations
cb.set_label('Colorscale Label')
cb.set_ticks([color[0] for color in colorscale])
cb.set_ticklabels(['{:.2f}'.format(color[0]) for color in colorscale])

# remove the x and y axes from the colorbar
cb.ax.xaxis.set_ticks_position('bottom')
cb.outline.set_visible(False)
cb.ax.xaxis.set_tick_params(width=0)

plt.show()
