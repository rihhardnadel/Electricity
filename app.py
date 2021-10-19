from flask import Flask, render_template
import getelekter
import numpy as np

app = Flask(__name__)



@app.route("/")
def electricity_prices():

    data = getelekter.get_data()
    format_data = getelekter.format_data(data)

    price_points = [item["price"] for item in format_data]
    
    min_price = np.min(price_points)
    average_price = np.mean(price_points)
    max_price = np.max(price_points)

    stats = [min_price, average_price, max_price]

    return render_template("displaysite.html", items=format_data, stats=stats)
