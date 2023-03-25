import pandas as pd
import plotly.graph_objects as go

# Load data from CSV file
data = pd.read_csv('data_final.csv')

# Filter data to include only the desired time point
time_point = 1675652400
data = data[data['time_start'] == time_point]

print(data.head(5))

# Create 3D surface plot
fig = go.Figure(data=[go.Scatter3d(x=data['longitude'], y=data['latitude'], z=data['sde'], 
                                   mode='markers', marker=dict(color=data['sde'], colorscale='inferno'))])

# Set axis ranges
fig.update_layout(scene=dict(xaxis=dict(range=[data['longitude'].min(), data['longitude'].max()]),
                             yaxis=dict(range=[data['latitude'].min(), data['latitude'].max()]),
                             zaxis=dict(range=[data['sde'].min(), data['sde'].max()])))


fig.show()
