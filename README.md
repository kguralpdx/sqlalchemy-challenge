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


## Steps to Run the Scripts

The database created for this challenge is called **EmployeeSQL**. To create the tables, run the *schemas.sql* file in the order laid out in the file starting with the **Create tables** section. The table scripts should be run in the following order:
1. departments
2. titles
3. salaries
4. employees
5. dept_emp
6. dept_manager

After that portion of the script has been run, load the tables by importing the CSV files in the following order:
1. departments
2. salaries
3. titles
4. employees
5. dept_emp
6. dept_manager

Once all the data has been loaded into the SQL tables, the rest of the *schemas.sql* script can be run starting with the **Create FKs** section. Then follow that with running the **Create Indexes** section. That should get the tables ready for querying.

The queries in the *queries.sql* file can be run in any order as they are not dependent on one another. They are, however, listed in the order of the questions asked in this challenge.

## Bonus Section

The purpose of the *Bonus* section is to determine if the data is fake or not. To help determine this, a histogram and bar chart were created.

### Requirements

In order for the *Jupyter Notebook* to connect to the *PostgreSQL* database, some steps need to be taken first:
1. The database should be named `EmployeeSQL`.
2. The user name for this database is `postgres` so an account using that name must exist with access to the *EmployeeSQL* database.
3. Create a text file called config.py and save it in the *EmployeeSQL* folder. This file should have an entry of `postgres_key = ` and then the password used by the `postgres` account to connect to the *PostgreSQL* database.

### Analysis

After creating the histogram and seeing that most of the employees' salaries fell within the $40,000 - $50,000 range, which was the lowest salary range, that seemed a little perplexing.

![sql.png](EmployeeSQL/histogram.PNG)

To find out how those salaries broke out by title, a bar chart was then created.

![barchart.png](EmployeeSQL/barchart.PNG)

Based on the results from that, it was concluded that the data was indeed fake as the highest paying jobs were staff positions and senior level positions were making less than their lower level counterparts. This conclusion was reaffirmed after searching for employee number *499942* and finding out that this employee's name is *April Foolsday*.

## Notes

The *barchart.png* and *histogram.png* files saved in the *EmployeeSQL* folder are images from the *Jupyter Notebook* **Bonus** section.

Just used one query to get all the data needed in the **Bonus** section and then used dataframes and groupbys to get what was needed for each chart. Did it with 2 queries originally, which was much faster, but figured I'd work on my *pandas*, *Python*, and *Jupyter Notebook* skills by using just one query and then manipulating that.