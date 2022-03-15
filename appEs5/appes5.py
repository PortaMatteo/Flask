# Si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta. 
# L'utente deve poter inserire il nome della squadra e la data di fondazione e la città.
# Deve inoltre poter effetturare delle ricerche inserendo uno dei valori delle colonne e ottenendo i dati presenti.

from flask import Flask, render_template, request 
app = Flask(__name__)
import pandas as pd 

@app.route("/", methods=["GET"])
def home():
    return render_template("homees5.html")

@app.route("/data", methods=["GET"])
def data():
    squadra = request.args["Nome"]
    anno = request.args["Anno"]
    citta = request.args["Citta"]
    df = pd.read_csv("/workspace/Flask/appEs5/templates/dati.csv")
    df2 = {"Squadra" : squadra, "Anno" : anno, "Città" : citta}
    df = df.append(df2, ignore_index = True)
    return df.to_html()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)