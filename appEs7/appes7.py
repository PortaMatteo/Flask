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

regioni = gpd.read_file("/workspace/Flask/appEs7/static/files/Regioni.zip")
province = gpd.read_file("/workspace/Flask/appEs7/static/files/Province.zip")
comuni = gpd.read_file("/workspace/Flask/appEs7/static/files/Province.zip")

print(province)

@app.route("/", methods=["GET"])
def home():
    return render_template("radReg.html", regioni = regioni["DEN_REG"])

@app.route("/radreg", methods=["GET"])
def radreg():
    regione = request.args["regione"]
    regioneUtente = regioni[regioni["DEN_REG"] == regione]
    provReg = province[province.within(regioneUtente.geometry.squeeze())]
    return render_template("radProv.html", regione = regione, province = provReg["DEN_UTS"])

@app.route("/radprov", methods=["GET"])
def radprov():
    provincia = request.args["provincia"]
    provinciaUtente = province[province["DEN_UTS"] == provincia]
    comProv = comuni[comuni.within(provinciaUtente.geometry.squeeze())][""]
    return render_template("result.html", provincia = provincia, tabella = comProv.to_html)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)