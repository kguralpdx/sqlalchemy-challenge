import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

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
        f"Available Routes:<br/>"
        f"<a href='//api/v1.0/precipitation'>precipitation</a><br/>"
        f"<a href='/api/v1.0/stations'>stations</a><br/>"
        f"<a href='/api/v1.0/tobs/USC00519281'>tobs/USC00519281</a><br/>"
        f"<a href='/api/v1.0/countryitemtotals/USA'>countryitemtotals/USA</a><br/>"
        f"<a href='/api/v1.0/postcodeitemtotals/USA'>postcodeitemtotals/USA</a><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all countries in billing history
   # results = session.query(Measurement.BillingCountry).group_by(Measurement.BillingCountry).all()


    session.close()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations in Station
    results = session.query(Station.station).group_by(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)

@app.route("/api/v1.0/tobs/<value>")
def tobs(value):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all datas and temperatures of the most active station for the last year of data
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= "2019-08-18").filter(Measurement.station == value).order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into a normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)

    ## Create a dictionary from the row data and append to a list of all_results
    ##all_results = []
    ##for item in results:
    ##    item_dict = {}
    ##    item_dict["date"] = item[0]
    ##    item_dict["tobs"] = item[1]
    ##    all_results.append(item_dict)

    ##return jsonify(all_results)


@app.route("/api/v1.0/countryitemtotals/<value>")
def countryitemtotals(value):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all countries' invoice totals
    results = session.query(func.sum(Items.UnitPrice * Items.Quantity)).filter(Invoices.InvoiceId == Items.InvoiceId).filter(Invoices.BillingCountry == value).scalar()

    session.close()

    # Create a dictionary from the results
    item_dict = {'country':value, 'total':float(results)}

    return jsonify([item_dict])

@app.route("/api/v1.0/postcodeitemtotals/<value>")
def postcodeitemtotals(value):
    session = Session(engine)
    results = session.query(Invoices.BillingPostalCode, func.sum(Items.UnitPrice * Items.Quantity)).filter(Invoices.InvoiceId == Items.InvoiceId).filter(Invoices.BillingCountry == value).group_by(Invoices.BillingPostalCode).order_by(func.sum(Items.UnitPrice * Items.Quantity).desc()).all()
    session.close()
    all_results = []
    for item in results:
        item_dict = {}
        item_dict["postcode"] = item[0]
        item_dict["total"] = float(item[1])
        all_results.append(item_dict)

    return jsonify(all_results)

if __name__ == '__main__':
    app.run(debug=True)
