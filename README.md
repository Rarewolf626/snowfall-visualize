# Snow Visualization
This projects aims to visualize different states' snow depth data over time. It was designed as a practice to get more comfortable with Python data manipulation and MatPlotLib.

The project is broken down into two classes:
- The DataExtractor class queries the AWS MySQL weather database I created for a [previous project](https://github.com/stars/esaltzm/lists/weather-visualization) (a full-stack web application to visualize all sorts of weather data). It extracts snow depth data and writes to a CSV file (selecting by the border of the state(s) of interest)
- The PlotGenerator class leverages MatPlotLib's animation methods to create a moving GIF, showing snow accumulation over time

Here are some examples I have generated so far:



### Multi-state plot of California, Oregon, Washington (with custom color scale)
![ezgif-5-659240f391](https://user-images.githubusercontent.com/99096893/228103899-d0fa2573-13ad-48cc-9821-b3c8d9fda87d.gif)

### Utah

![ezgif-5-ae6ff943c9](https://user-images.githubusercontent.com/99096893/227790148-fc747bdb-eb68-4c6c-98f9-2ed629cd78e2.gif)

### Colorado

![ezgif-1-84831d033b](https://user-images.githubusercontent.com/99096893/227790492-529130b1-1d06-49a6-8d88-9fa84f98f796.gif)

