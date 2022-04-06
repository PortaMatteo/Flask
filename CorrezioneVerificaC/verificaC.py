from flask import Flask, render_template, request, Response, redirect, url_for
app = Flask(__name__)

import io
import pandas as pd
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

quartieri = gpd.read_file("/workspace/Flask/appEs6/static/files/ds964_nil_wm.zip")
linee = gpd.read_file("https://dati.comune.milano.it/dataset/8bfe2015-2669-4796-9940-36b3c155b258/resource/b5acc06f-65fb-4481-9428-347fd1c18096/download/tpl_percorsi.geojson")

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/selezione", methods=["GET"])
def selezione():
    scelta = request.args["scelta"]
    if scelta == "es1":
        return redirect(url_for("input"))
    elif scelta == "es2":
        return redirect(url_for("ricerca"))
    else:
        return redirect(url_for("mappa"))

@app.route("/input", methods=["GET"])
def input():
    return render_template("input.html")

@app.route("/elenco", methods=["GET"])
def elenco():
    Min = min(request.args["val1"], request.args["val2"])
    Max = max(request.args["val1"], request.args["val2"])
    linee_distanza = linee[(linee["lung_km"] > Min) & (linee["lung_km"] < Max)].sort_values("linea")
    return render_template("elenco.html", tabella = linee_distanza.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)