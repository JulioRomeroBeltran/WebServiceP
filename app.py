from flask import Flask, jsonify
import os  

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hola Mundo</h1>
    <h2>Julio Emmanuel Romero Beltrán - 22031467</h2>
    """

@app.route("/json")
def json_response():
    return jsonify({
        "mensaje": "Hola Mundo",
        "nombre": "Julio Emmanuel Romero Beltrán",
        "matricula": "22031467"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
