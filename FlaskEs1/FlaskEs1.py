from flask import Flask, render_template
import random
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/meteo")
def meteo():
    nRandom = random.randint(0,8)
    if nRandom <= 2:
        meteo = "PIOGGIA"
        immagine = "/static/images/pioggia.jpg"
    elif nRandom <= 5:
        meteo = "NUVOLOSO"
        immagine = "/static/images/nuvoloso.jpg"
    else:
        meteo = "SOLEGGIATO"
        immagine = "static/images/sole.jpg"
    return render_template("meteo.html", meteo = meteo ,meteo_img=immagine)

@app.route("/frasicelebri")
def libro():
    frasi = [{"Autore": "Frida Kahlo" , "Frase": "Innamorati di te, della vita e dopo di chi vuoi." },
    {"Autore": "Dietrich Bonhoeffer" , "Frase": "Contro la stupidità non abbiamo difese."},
    {"Autore": "Charlie Chaplin" , "Frase": "Un giorno senza un sorriso è un giorno perso."},{"Autore": "Francesco Bacone" , "Frase": "Sapere è potere."},
    {"Autore": "Italo Calvino" , "Frase": "Il divertimento è una cosa seria."},{"Autore": "Lewis Carroll" , "Frase": "Qui siamo tutti matti."},
    {"Autore": "Johann Wolfgang von Goethe", "Frase": "Il dubbio cresce con la conoscenza."},{"Autore": "Luis Sepùlveda" , "Frase": "Vola solo chi osa farlo."},
    {"Autore": "Lucio Anneo Seneca", "Frase": "Se vuoi essere amato, ama."},{"Autore": "Voltaire", "Frase": "Chi non ha bisogno di niente non è mai povero."}]
    fRandom = random.randint(0,9)
    return render_template("frasicelebri.html", autore = frasi[fRandom]["Autore"], frase = frasi[fRandom]["Frase"])

@app.route("/quantomanca")
def calendario():
    now = datetime.now()
    school = datetime(2022,6,8)
    return render_template("calendario.html", data = (school - now).days)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)