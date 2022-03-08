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
        utente = {"Nome" : nome, "Username" : username, "Sex" : sesso, "Password" : password}
        lista.append(utente)
        print(lista)
        if sesso == "M":
            saluto = "Benvenuto"
        elif sesso == "F":
            saluto = "Benvenuta"
        else:
            saluto = "Benvenut*"
        return render_template("welcomeses2.html", benvenuto = saluto)
    else:
        return "<h1>Errore</h1>"

@app.route("/login", methods=["GET"])
def login():
    return render_template("es2login.html")

@app.route("/datalog", methods=["GET"])
def datalog():
    username = request.args["Username"]
    password = request.args['Password']
    for i in range(len(lista)):
        if username == lista[i]["Username"]
        





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)