from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hola Mundo</h1>","<h1>Julio Emmanuel Romero Beltrán - 22031467</h1>"

@app.route("/json")
def json_response():
    return jsonify({"mensaje": "Hola Mundo","nombre":"Julio Emmanuel Romero Beltran", "matricula": "22031467"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
