from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/meteo")
def meteo():
    nRandom = random.randint(0,8)
    if nRandom <= 2:
        immagine = "/static/images/pioggia.jpg"
    elif nRandom <= 5:
        immagine = "/static/images/nuvoloso.jpg"
    else:
        immagine = "static/images/sole.webp"
    return render_template("meteo.html", meteo=immagine)

@app.route("/frasicelebri")
def libro():
    return render_template()

@app.route("/quantomanca")
def calendario():
    return render_template()



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)