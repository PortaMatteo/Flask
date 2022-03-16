# Si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta. 
# L'utente deve poter inserire il nome della squadra e la data di fondazione e la città.
# Deve inoltre poter effetturare delle ricerche inserendo uno dei valori delle colonne e ottenendo i dati presenti.

from flask import Flask, render_template, request 
app = Flask(__name__)
import pandas as pd 


@app.route("/", methods=["GET"])
def home():
    return render_template("sceltaes5.html")

@app.route("/inserisci", methods=["GET"])
def inserisci():
    return render_template("inseriscies5.html")

@app.route("/data", methods=["GET"])
def data():
    squadra = request.args["Nome"]
    anno = request.args["Anno"]
    citta = request.args["Citta"]
    df = pd.read_csv("/workspace/Flask/appEs5/templates/dati.csv")
    dUtente = {"Squadra" : squadra, "Anno" : anno, "Citta" : citta}
    df = df.append(dUtente, ignore_index = True)
    df.to_csv("/workspace/Flask/appEs5/templates/dati.csv", index=False)
    return render_template("sceltaes5.html")

@app.route("/ricerca", methods=["GET"])
def ricerca():
    return render_template("ricercaes5.html")

@app.route("/dataRicerca", methods=["GET"])
def datiRic():
    df = pd.read_csv("/workspace/Flask/appEs5/templates/dati.csv")
    df["Anno"] = df["Anno"].astype(str)
    scelta = request.args["Scelta"]
    cerca = request.args["Ricerca"]
    df_result = df[df[scelta] == cerca]
    return df_result.to_html()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)