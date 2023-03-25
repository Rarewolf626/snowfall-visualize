import pandas as pd
import plotly.graph_objects as go

# Load data from CSV file
data = pd.read_csv('ca_snow_data.csv')

# Create 3D surface plot
fig = go.Figure(data=[go.Surface(x=data['longitude'], y=data['latitude'], z=data['sde'], colorscale='Blues')])

# Add slider for time
fig.update_layout(
    sliders=[{
        'currentvalue': {'prefix': 'Time: '},
        'steps': [
            {'label': str(time), 'method': 'update', 'args': 
                [{'visible': [time == t for t in data['time_start']]}]
            } for time in data['time_start'].unique()
        ]
    }]
)

fig.show()
