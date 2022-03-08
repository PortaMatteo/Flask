# Realizzare un server web che permetta di effettuare il login 
# L'utente inserisce lo username e la password
# Se l'username è admin e se la password è xxx123## il sito ci saluta con un messaggio di benvenuto 
# Altrimenti ci da un messaggio di errore 

from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("es1login.html")

@app.route("/data", methods={"GET"})
def data():
    username = request.args["Username"]
    password = request.args['Password']
    if username == "admin" and password == "xxx123##":
        return render_template("welcomes1.html", Username = username)
    else:
        return "<h1>Errore</h1>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)