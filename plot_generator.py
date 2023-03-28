import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import Axes3D

class PlotGenerator:
    def __init__(self, type, states):
        self.type = type
        self.states = states
        self.data = pd.concat([pd.read_csv(f'snow_csv_data/{state}_snow_data.csv') for state in states])
        self.unique_times = sorted(self.data['time_start'].unique())

        if self.type == '3d':
            self.fig = plt.figure(figsize=(12, 9))
            self.fig.subplots_adjust(top=0.85, bottom=0.15)
            self.ax = self.fig.add_subplot(111, projection='3d')
            self.ax.set_box_aspect([1, 1, None])
        
        elif self.type == 'contour':
            self.fig, self.ax = plt.subplots(figsize=(12, 9))
            self.ax.set_aspect('equal')

        # Create colorbar
        self.colorscale = [    
            (0, (0, 0, 0)),
            (0.008, (0, 1, 1)),
            (0.12, (0, 0, 1)),
            (0.24, (130/255, 0, 255/255)),
            (0.4, (1, 0, 1)),
            (0.5, (1, 0, 0)),
            (0.72, (1, 1, 0)),
            (1, (1, 1, 1))
        ]
        self.cmap = mcolors.LinearSegmentedColormap.from_list('custom', self.colorscale)
        self.sde_max = np.max(self.data['sde']) * 3.28084
        sm = mpl.cm.ScalarMappable(cmap=self.cmap, norm=mpl.colors.Normalize(vmin=0, vmax=self.sde_max))
        sm.set_array([])
        cbar = self.fig.colorbar(sm, shrink=0.3, aspect=10, pad=-0.03)
        cbar.ax.set_ylabel('Snow Depth (ft)')
        cbar.ax.yaxis.set_ticks_position('left')
        cbar.ax.yaxis.set_label_position('left')
        cbar.ax.tick_params(length=0)
        cbar.ax.set_position([0.75, 0.1, 0.03, 0.9])

    def update_3d(self, i):
        time = self.unique_times[i]
        subset = self.data[self.data['time_start'] == time]
        x, y, z = subset['longitude'], subset['latitude'], subset['sde'] * 3.28084
        dz = z / self.sde_max
        self.ax.clear()
        self.ax.bar3d(x, y, np.zeros(len(z)), dx=0.16, dy=0.16, dz=z, color=self.cmap(dz), edgecolor=None)
        self.ax.set_box_aspect([6, 4.5, 2])  # Set aspect ratio of x, y, z axes
        self.ax.set_title(pd.to_datetime(time, unit="s").strftime("%m/%d/%Y"), pad=-25, y=0.9)
        self.fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
        self.ax.axis('off')
        self.ax.view_init(elev=60, azim=-90)
        self.ax.set_zlim(0, self.sde_max)
    
    def update_contour(self, i):
        time = self.unique_times[i]
        subset = self.data[self.data['time_start'] == time]
        x, y, z = subset['longitude'], subset['latitude'], subset['sde'] * 3.28084
        dz = z / self.sde_max
        self.ax.clear()
        contour = self.ax.tricontourf(x, y, z, cmap=self.cmap)
        self.ax.set_aspect('equal')
        self.ax.set_title(pd.to_datetime(time, unit="s").strftime("%m/%d/%Y"), pad=-20, y=0.9)
        self.fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
        self.ax.set_xlabel('Longitude')
        self.ax.set_ylabel('Latitude')
        self.fig.colorbar(contour, ax=self.ax)

    def generate_plot(self):
        if self.type == '3d':
            # self.update_3d(130)
            # plt.show()

            ani = animation.FuncAnimation(self.fig, self.update_3d, frames=len(self.unique_times))
            # ani.save(f"snow_depth_gifs/{'_'.join(self.states)}_snow_depth_3d.gif", writer='pillow')
            ani.save(f"snow_depth_gifs/conus_snow_depth_3d.gif", writer='pillow')
        
        if self.type == 'contour':
            self.update_contour(140)
            plt.show()

            # ani = animation.FuncAnimation(self.fig, self.update_contour, frames=len(self.unique_times))
            # ani.save(f"snow_depth_gifs/{'_'.join(self.states)}_snow_depth_contour.gif", writer='pillow')



plot = PlotGenerator('3d', ['alabama', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new_hampshire', 'new_jersey', 'new_mexico', 'new_york', 'north_carolina', 'north_dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhode_island', 'south_carolina', 'south_dakota', 'tennessee', 'tx_east', 'tx_west', 'utah', 'vermont', 'virginia', 'washington', 'west_virginia', 'wisconsin', 'wyoming'])

plot.generate_plot()

