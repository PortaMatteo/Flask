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

regioni = gpd.read_file("/workspace/Flask/CorrezioneVerificaB2/static/files/Regioni.zip")
province = gpd.read_file("/workspace/Flask/CorrezioneVerificaB2/static/files/Province.zip")
ripartizioni = gpd.read_file("/workspace/Flask/CorrezioneVerificaB2/static/files/RipGeo.zip")


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/input", methods=["GET"])
def input():
    return render_template("input.html")

@app.route("/risultato", methods=["GET"])
def risutlato():
    global regione
    regioneUtente = request.args["regione"]
    regione = regioni[regioni["DEN_REG"] == regioneUtente]
    province_regione = province[province.within(regione.geometry.squeeze())]
    lunghezza = regione.geometry.length
    return render_template("risultato.html", tabella = province_regione[["DEN_UTS","Shape_Area"]].reset_index().to_html(), lunghezza=lunghezza)
    
@app.route("/mappa.png", methods=["GET"])
def mappa():
    fig, ax = plt.subplots(figsize = (12,8))

    regione.to_crs(epsg=3857).plot(ax=ax, edgecolor="red", facecolor="none")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/dropdown", methods=["GET"])
def dropdown():
    return render_template("dropdown.html", ripartizioni = ripartizioni["DEN_RIP"])

@app.route("/radio", methods=["GET"])
def radio():
    ripartizioneUtente = request.args["ripartizione"]
    ripartizione = ripartizioni[ripartizioni["DEN_RIP"] == ripartizioneUtente]
    reg_ripartizione = regioni[regioni.within(ripartizione.geometry.squeeze())]
    return render_template("radio.html", regioni = reg_ripartizione["DEN_REG"].sort_values())

@app.route("/linkpart", methods=["GET"])
def linkpart():
    return render_template("linkpart.html", ripartizioni = ripartizioni["DEN_RIP"])

@app.route("/linkreg/<valore>", methods=["GET"])
def linkreg(valore):
    ripartizione = ripartizioni[ripartizioni["DEN_RIP"] == valore]
    reg_ripartizione = regioni[regioni.within(ripartizione.geometry.squeeze())]
    return render_template("linkreg.html", regioni = reg_ripartizione["DEN_REG"].sort_values())

@app.route("/resreg/<val>", methods=["GET"])
def resreg(val):
    regioneUtente = val
    return redirect(url_for("risultato"))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)