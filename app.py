from flask import Flask, render_template
import getelekter
import numpy as np
import plotly
import plotly.express as px
import pandas as pd
import json

app = Flask(__name__)

data = getelekter.get_data()
format_data = getelekter.format_data(data)

@app.route("/")
def electricity_prices():
    price_points = [item["price"] for item in format_data]
    
    min_price = np.min(price_points)
    average_price = np.mean(price_points)
    max_price = np.max(price_points)

    stats = [min_price, average_price, max_price]
 
    return render_template("displaysite.html", items=format_data, stats=stats)

@app.route("/graph")
def graph():
    df = pd.DataFrame(data=format_data)
    mean = df["price"].mean()
    fig = px.line(df, x="timestamp", y="price", labels={"timestamp": "Kellaaeg", "price":"Hind (EUR/MWh)"})
    fig.add_hline(mean, line_color="orange", line_dash="dash", annotation_text="Keskmine", annotation_position="top left")
    json_dump = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('pxplot.html', graphJSON=json_dump, header="Elektrihinnad järgmise 24h jooksul")