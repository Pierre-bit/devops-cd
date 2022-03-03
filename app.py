from FLASK  import flask

app=flask(__name__)
PORT= os.environ.get("PORT","80")
HOST= os.environ.get("HOST","0.0.0.0")



@app.route("/")
def hello():
    return "Hello World"

if __name__== "__main__":
    app.run(host=HOST, port=PORT)