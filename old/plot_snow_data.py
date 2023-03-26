import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = pd.read_csv('data_final.csv').query('time_start > 1667250000')

unique_times = sorted(data['time_start'].unique())

fig = plt.figure()
fig.subplots_adjust(top=0.9)
ax = fig.add_subplot(111, projection='3d')

# Create colorbar
sde_max = np.max(data['sde']) * 3.28084
sm = mpl.cm.ScalarMappable(cmap='inferno', norm=mpl.colors.Normalize(vmin=0, vmax=0.8 * sde_max))
sm.set_array([])
cbar = fig.colorbar(sm, shrink=0.5, aspect=10, pad=0.05)
cbar.ax.set_ylabel('Snow Depth (ft)')
cbar.ax.yaxis.set_ticks_position('left')
cbar.ax.yaxis.set_label_position('left')
cbar.ax.tick_params(length=0)
cbar.ax.set_position([0.75, 0.1, 0.03, 0.9])

def update(i):
    time = unique_times[i]
    subset = data[data['time_start'] == time]
    x, y, z = subset['longitude'], subset['latitude'], subset['sde'] * 3.28084
    ax.clear()
    ax.bar3d(x, y, np.zeros(len(z)), dx=0.15, dy=0.15, dz=z, color=plt.cm.inferno(z / (0.8 * sde_max)), edgecolor=None)
    ax.set_title(pd.to_datetime(time, unit="s").strftime("%m/%d/%Y"))
    ax.title.set_position([0.5, 0.01])
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
    ax.axis('off')
    ax.view_init(elev=60, azim=-90)
    
update(120)
plt.show()

# # Create animation
# ani = animation.FuncAnimation(fig, update, frames=len(unique_times))

# # Save animation to gif
# ani.save('snow_depth_gifssnow_depth.gif', writer='imagemagick')
