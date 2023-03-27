import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import Axes3D

class PlotGenerator:
    def __init__(self, states):
        self.states = states
        self.data = pd.concat([pd.read_csv(f'snow_csv_data/{state}_snow_data.csv') for state in states])
        self.unique_times = sorted(self.data['time_start'].unique())

        self.fig = plt.figure(figsize=(12, 9))
        self.fig.subplots_adjust(top=0.85, bottom=0.15)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_box_aspect([1, 1, None])
        # Create colorbar
        self.colorscale = [
            (0, (0, 0, 0)),
            (0.01, (0, 1, 1)),
            (0.2, (0, 0, 1)),
            (0.4, (130/255, 0, 255/255)),
            (0.6, (1, 0, 1)),
            (0.8, (1, 1, 0)),
            (1, (1, 1, 1))
        ]
        self.cmap = mcolors.LinearSegmentedColormap.from_list('custom', self.colorscale)
        self.sde_max = np.max(self.data['sde']) * 3.28084
        sm = mpl.cm.ScalarMappable(cmap=self.cmap, norm=mpl.colors.Normalize(vmin=0, vmax=self.sde_max))
        sm.set_array([])
        cbar = self.fig.colorbar(sm, shrink=0.5, aspect=10, pad=-0.17)
        cbar.ax.set_ylabel('Snow Depth (ft)')
        cbar.ax.yaxis.set_ticks_position('left')
        cbar.ax.yaxis.set_label_position('left')
        cbar.ax.tick_params(length=0)
        cbar.ax.set_position([0.75, 0.1, 0.03, 0.9])

    def update(self, i):
        print(f'{i} of {len(self.unique_times)}')
        time = self.unique_times[i]
        subset = self.data[self.data['time_start'] == time]
        x, y, z = subset['longitude'], subset['latitude'], subset['sde'] * 3.28084
        dz = z / self.sde_max
        self.ax.clear()
        self.ax.bar3d(x, y, np.zeros(len(z)), dx=0.16, dy=0.16, dz=dz, color=self.cmap(dz), edgecolor=None)
        self.ax.set_box_aspect([0.6, 1, 1])  # Set aspect ratio of x, y, z axes
        self.ax.set_title(pd.to_datetime(time, unit="s").strftime("%m/%d/%Y"), pad=-20, y=0.96)
        self.fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
        self.ax.axis('off')
        self.ax.view_init(elev=80, azim=-90)
        self.ax.set_zlim(0, self.sde_max)

    def generate_plot(self):
        # self.update(10)
        # plt.show()

        ani = animation.FuncAnimation(self.fig, self.update, frames=len(self.unique_times))
        ani.save(f"snow_depth_gifs/{'_'.join(self.states)}_snow_depth.gif", writer='pillow')



plot = PlotGenerator(['oregon', 'washington', 'california'])
plot.generate_plot()