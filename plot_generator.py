import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from shapely.wkt import loads


class PlotGenerator:
    def __init__(self, state):
        self.state = state
        self.data = pd.read_csv(f'snow_csv_data/{state}_snow_data.csv')
        self.unique_times = sorted(self.data['time_start'].unique())

        self.fig = plt.figure()
        self.fig.subplots_adjust(top=0.9)
        self.ax = self.fig.add_subplot(211, projection='3d')
        self.ax.set_box_aspect([1, 1, 0.5])

        # Create colorbar
        self.sde_max = np.max(self.data['sde']) * 3.28084
        cmap = mpl.cm.bone
        cmap.set_bad(color='white')
        sm = mpl.cm.ScalarMappable(cmap=cmap, norm=mpl.colors.Normalize(vmin=0, vmax=0.8 * self.sde_max))
        sm.set_array([])
        cbar = self.fig.colorbar(sm, shrink=0.5, aspect=10, pad=0.05)
        cbar.ax.set_ylabel('Snow Depth (ft)')
        cbar.ax.yaxis.set_ticks_position('left')
        cbar.ax.yaxis.set_label_position('left')
        cbar.ax.tick_params(length=0)
        cbar.ax.set_position([0.75, 0.5, 0.03, 0.4])

        # Add 2D line plot of state polygon
        self.ax2 = self.fig.add_subplot(212)
        with open(f'state_wkt_files/{self.state}.wkt', 'r') as f:
            state_wkt = f.read()
        state_polygon = loads(state_wkt)
        x, y = state_polygon.exterior.xy
        self.ax2.plot(x, y, color='black')
        self.ax2.set_aspect('equal')
        self.ax2.axis('off')
        self.ax2.set_title(f'{self.state.upper()} State Outline')

    def update(self, i):
        time = self.unique_times[i]
        subset = self.data[self.data['time_start'] == time]
        x, y, z = subset['longitude'], subset['latitude'], subset['sde'] * 3.28084
        self.ax.clear()
        self.ax.bar3d(x, y, np.zeros(len(z)), dx=0.15, dy=0.15, dz=z, color=plt.cm.bone(z / (0.8 * self.sde_max)), edgecolor=None)
        self.ax.set_box_aspect([0.75, 1, 0.4])  # Set aspect ratio of x, y, z axes
        self.ax.set_title(pd.to_datetime(time, unit="s").strftime("%m/%d/%Y"))
        self.ax.title.set_position([0.5, 0.01])
        self.fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
        self.ax.axis('off')
        self.ax.view_init(elev=60, azim=-90)

    def generate_plot(self):
        # self.update(0)
        # plt.show()

        # Create animation
        ani = animation.FuncAnimation(self.fig, self.update, frames=len(self.unique


        # Save animation to gif
        ani.save(f'snow_depth_gifs/{self.state}_snow_depth.gif', writer='imagemagick')



plot = PlotGenerator('utah')
plot.generate_plot()