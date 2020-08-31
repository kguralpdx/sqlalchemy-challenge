## sqlalchemy-challenge
# A Well-Timed Trip to Hawaii

## Overview

Time to take a trip to Hawaii! To help figure out the best time of year to go weather-wise, climate data gathered over several years is analyzed. Then a Flask API is created to quickly query the data.

Then as a bonus, further analysis of the temperature and precipitation data is performed.

### Files and Folders

* **Jupyter Notebook** (climate_starter.jpynb) - The Jupyter Notebook file that contains the scripts, plot, histogram, and analysis for the main challenge and a bar chart for the **BONUS** section
* [Flask API](app.py) - this file is the script for the Flask API. It contains the various routes to query the data
* [Resources](Resources/) - this folder contains the date source files
    * **hawaii.sqlite** - the sqlite file used to source the Jupyter Notebook and for the analysis
    * [Hawaii Measurements](Resources/hawaii_measurements.csv) - contains the precipitation and temperature data for each station over several years. *Not used as a data source for this challenge; only used for validation.*
    * [Hawaii Stations](Resources/hawaii_stations.csv) - contains the details about each station. *Not used as a data source for this challenge; used only for validation.*

### Analysis

After loading the climate data from the *hawaii.sqlite* file, I need to see what was actually in there in regards to tables/classes, columns, data types and data itself. Ran the Inspector to see column names and data types in both tables (*measurement* and *station*). Then queried the tables to take a look at the data. 

## Notes

The query for **** in the Jupyter Notebook isn't exactly the same as the one used in the *app.py* file. I wasn't sure if the approach I used in the Jupyter Notebook would work in with the API so I revised my query for the API. Both returned the same results and I got to use two different approaches to pull the data so I kept them both.


Just used one query to get all the data needed in the **Bonus** section and then used dataframes and groupbys to get what was needed for each chart. Did it with 2 queries originally, which was much faster, but figured I'd work on my *pandas*, *Python*, and *Jupyter Notebook* skills by using just one query and then manipulating that.