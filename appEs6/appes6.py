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

@app.route("/", methods=["GET"])
def home():
    return render_template("homees6.html")

@app.route("/plot.png", methods=["GET"])
def result():
    fig, ax = plt.subplots(figsize = (12,8))

    imgUtente.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor="k")
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot', methods=("POST", "GET"))
def mpl():
    global imgUtente
    quartiereUtente = request.args["Quartiere"]
    imgUtente = quartieri[quartieri["NIL"] == quartiereUtente]
    return render_template('plot.html', PageTitle = "Matplotlib")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)