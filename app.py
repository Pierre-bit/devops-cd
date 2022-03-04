from flask import Flask
import os

app=Flask(__name__)

#récupérsation des ENV
PORT= os.environ.get("PORT","80")
HOST= os.environ.get("HOST","0.0.0.0")

@app.route("/bye")
def bye():
    return "Bye"

@app.route("/bonjour")
def bonjour():
    return "salut a tous"

@app.route("/test")
def test():
    return "test"

@app.route("/")
def hello():
    '''
    Fonction appelé pour le chemin par défaut

    Returns:
        str: un message de la plus grande importance
    '''
    return "Hello World !"

if __name__== "__main__":
    app.run(host=HOST, port=PORT)