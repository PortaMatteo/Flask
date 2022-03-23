# Realizzare un sito web che restituisca la mappa dei quartieri di milano .
# Ci deve essere una home page con un link "quartieri di milano": cliccando su questo link si deve visualizzare la mappa dei quartieri di milano

from flask import Flask, render_template, request, Response
app = Flask(__name__)

import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

quartieri = gpd.read_file("/workspace/Flask/appEs6/static/files/ds964_nil_wm.zip")
fontanelle = gpd.read_file("/workspace/Flask/appEs6/static/files/Fontanelle.zip")

@app.route("/", methods=["GET"])
def home():
    return render_template("homees6.html")

@app.route("/visualizza.png", methods=["GET"])
def visualizzaRes():
    fig, ax = plt.subplots(figsize = (12,8))

    quartieri.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/visualizza', methods=("POST", "GET"))
def visualizza():
    return render_template('visualizza.html', PageTitle = "Matplotlib")

@app.route("/ricerca.png", methods=["GET"])
def ricercaRes():
    fig, ax = plt.subplots(figsize = (12,8))

    imgUtente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/ricerca', methods=("POST", "GET"))
def ricerca():
    return render_template('ricerca.html')

@app.route('/ricercares', methods=("POST", "GET"))
def Ricerca():
    global imgUtente
    quartiereUtente = request.args["Quartiere"]
    imgUtente = quartieri[quartieri["NIL"] == quartiereUtente]
    if len(imgUtente) == 0:
        return "<h1>Il quartiere inserito non esiste</h1>"
    else:
        return render_template('ricercares.html', PageTitle = "Matplotlib", quartiere=quartiereUtente)

@app.route('/scelta', methods=("POST", "GET"))
def scelta():
    return render_template('scelta.html', quartieri= quartieri["NIL"])


@app.route("/fontanelle", methods=["GET"])
def fontanelle1():
    return render_template("fontanelle.html", quartieri= quartieri["NIL"])

@app.route('/fontanelleres', methods=("POST", "GET"))
def fontanelleRes():
    global imgUtente, fontQuart
    
    quartiereUtente = request.args["Quartiere"]
    imgUtente = quartieri[quartieri["NIL"] == quartiereUtente]
    fontQuart = fontanelle[fontanelle.within(imgUtente.geometry.squeeze())]
    print(fontQuart)
    return render_template('fontanelleres.html', PageTitle = "Matplotlib", quartiere=quartiereUtente, tabella = fontQuart.to_html())

@app.route("/fontanelle.png", methods=["GET"])
def Fontanelle():
    fig, ax = plt.subplots(figsize = (12,8))

    imgUtente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    fontQuart.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)