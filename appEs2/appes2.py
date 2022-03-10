# Realizzare un sito web che permetta la registrazione degli utenti 
# L'utente inserisce il nome, uno username un password 
# La conferma della password e il sesso
# Se le informazioni sono corrette il sito slava le informazioni in una struttura dati opportuna (lista di dizionari)

# Prevedere la possibilità di fare il login inserendo username e password
# Se sono corrette fornire un messaggio di benvenuto diverso a secondo del sesso 

from flask import Flask, render_template, request 
app = Flask(__name__)

lista = []

@app.route("/", methods=["GET"])
def home():
    return render_template("es2Reg.html")

@app.route("/data", methods={"GET"})
def data():
    nome = request.args["Name"]
    username = request.args["Username"]
    sesso = request.args["Sex"]
    password = request.args['Password']
    passwordConf = request.args['PasswordConf']
    if password == passwordConf:
        lista.append({"Nome" : nome, "Username" : username, "Sex" : sesso, "Password" : password})
        print(lista)
        return render_template("es2login.html")
    else:
        return "<h1>Errore</h1>"


@app.route("/login", methods=["GET"])
def login():
    return render_template("es2login.html")

@app.route("/datalog", methods=["GET"])
def datalog():
    username = request.args["Username"]
    password = request.args['Password']
    for utente in lista:
        if username == utente["Username"] and password == utente["Password"]:
            if utente["Sex"] == "M":
                saluto = "Benvenuto"
                color = "#0000FF"
            elif utente["Sex"] == "F":
                saluto = "Benvenuta"
                color = "#ffc0cb"
            else:
                saluto = "Benvenut*"
                color = "#ffff00"
            return render_template("welcomeses2.html", benvenuto = saluto, nome = utente["Nome"], colore = color)
    return "<h1>Errore</h1>"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)