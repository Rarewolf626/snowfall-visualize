# Snow Visualization
This projects aims to visualize different states' snow depth data over time. It was designed as a practice to get more comfortable with Python data manipulation and MatPlotLib.

The project is broken down into two classes:
- The DataExtractor class queries the AWS MySQL weather database I created for a [previous project](https://github.com/stars/esaltzm/lists/weather-visualization) (a full-stack web application to visualize all sorts of weather data). It extracts snow depth data and writes to a CSV file (selecting by the border of the state of interest)
- The PlotGenerator class leverages MatPlotLib's animation methods to create a moving GIF, showing snow accumulation over time

Here are some examples I have generated so far:

### Washington

![ezgif-4-f2e753b483](https://user-images.githubusercontent.com/99096893/227790115-d2439b04-4c97-4a37-8a30-46907ee6d2b1.gif)

### California

![ezgif-4-b3440d9a54](https://user-images.githubusercontent.com/99096893/227790478-5998ad3d-9a91-444c-848a-5d61e5c0c533.gif)

### Utah

![ezgif-5-ae6ff943c9](https://user-images.githubusercontent.com/99096893/227790148-fc747bdb-eb68-4c6c-98f9-2ed629cd78e2.gif)

### Colorado

![ezgif-1-84831d033b](https://user-images.githubusercontent.com/99096893/227790492-529130b1-1d06-49a6-8d88-9fa84f98f796.gif)

