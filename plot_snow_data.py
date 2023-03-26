import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Load data from CSV file
data = pd.read_csv('data_final.csv')
# Get unique times in data
unique_times = sorted(data['time_start'].unique())

# Create figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define colors for snow depth values
color_scale = plt.cm.get_cmap('Blues')

# Create function to update plot for each time step
def update(i):
    time = unique_times[i]
    subset = data[data['time_start'] == time]
    x, y, z = subset['longitude'], subset['latitude'], subset['sde']
    color_scale = plt.colormaps['inferno']
    surf = ax.scatter(x, y, z, c=z, cmap=color_scale, vmin=0, vmax=np.max(data['sde']))
    ax.set_title(f'Snow Depth for Time: {time}')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(unique_times))

# Save animation to gif
ani.save('snow_depth.gif', writer='imagemagick')