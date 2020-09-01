import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
Station = Base.classes.station
Measurement = Base.classes.measurement
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<strong>Available Routes:</strong><br/>"
        f"<li><a href='/api/v1.0/precipitation'>Precipitation</a></li><br/>"
        f"<li><a href='/api/v1.0/stations'>Stations</a></li><br/>"
        f"<li><a href='/api/v1.0/tobs/USC00519281'>Station USC00519281 Temperatures for most recent 12 months</a></li><br/>"
        f"<li><a href='/api/v1.0/<start>'>Min, Avg, Max Temperature Stats (Start Date) - replace 'start' in URL with start date in yyyy-mm-dd format</a></li><br/>"
        f"<li><a href='/api/v1.0/<start>/<end>'>Min, Avg, Max Temperature Stats (Start and End Dates) - replace 'start' and 'end' in URL with dates in yyyy-mm-dd format</a></li><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query precipiation data for the last year of available data
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').filter(Measurement.prcp != "None").order_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_results
    all_results = []
    for item in results:
        item_dict = {}
        item_dict["date"] = item[0]
        item_dict["prcp"] = item[1] #float(item[1])
        all_results.append(item_dict)

    return jsonify(all_results)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations in Station
    results = session.query(Station.name).group_by(Station.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)

@app.route("/api/v1.0/tobs/<value>")
def tobs(value):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all datas and temperatures of the most active station for the last year of data
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= "2016-08-18").filter(Measurement.station == value).order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into a normal list
    all_results = list(np.ravel(results))

    #all_results = []
    #for date, tobs in results:
    #    precipitation_dict = {}
    #    precipitation_dict["date"] = date
    #    precipitation_dict["tobs"] = tobs
    #    all_results.append(precipitation_dict)

    return jsonify(all_results)

@app.route("/api/v1.0/<start>", defaults={'end': None})
@app.route("/api/v1.0/<start>/<end>")

def tobssumstats(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    # Got help with the default in the app.route from Audrius Kažukauskas' reply at https://stackoverflow.com/questions/14032066/can-flask-have-optional-url-parameters?rq=1
    # Got the idea for splitting up the query from padamsethia's reply at https://www.reddit.com/r/flask/comments/8y92c0/help_sqlalchemy_multiple_filter_queries/

    query = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start)
    
    if end:
        query = query.filter(Measurement.date <= end)
    
    results = query.all()

    #results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)

if __name__ == '__main__':
    app.run(debug=True)
