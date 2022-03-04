from flask import Flask
import os

app=Flask(__name__)

#récupérsation des ENV
PORT= os.environ.get("PORT","80")
HOST= os.environ.get("HOST","0.0.0.0")

def test():
    pass

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