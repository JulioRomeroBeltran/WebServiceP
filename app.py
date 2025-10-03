from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    """
    Ruta raíz que devuelve una página HTML con estilo mejorado.
    Ahora incluye un input para enviar un texto y mostrarlo en JSON.
    """
    styled_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>¡Hola Mundo! - App de Render</title>
    <style>
        body {
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1e1e2e;
            color: #cdd6f4;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #313244;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            text-align: center;
            max-width: 90%;
            width: 450px;
            border-top: 6px solid #89b4fa;
        }
        h1 {
            color: #a6e3a1;
            font-size: 2.8em;
            margin-bottom: 5px;
            font-weight: 700;
        }
        .data-label {
            display: block;
            margin-top: 20px;
            font-size: 0.9em;
            color: #bac2de;
            font-weight: 300;
        }
        .data-value {
            font-size: 1.1em;
            color: #fab387;
            font-weight: 600;
            margin-bottom: 15px;
            padding: 5px 0;
        }
        input[type="text"] {
            padding: 10px;
            border-radius: 6px;
            border: none;
            margin-top: 15px;
            width: 80%;
            text-align: center;
        }
        button {
            margin-top: 15px;
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            background-color: #89b4fa;
            color: #1e1e2e;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background-color: #74c7ec;
        }
        .note {
            color: #a6e3a1;
            font-style: italic;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Hola Mundo!</h1>
        
        <span class="data-label">Alumno:</span>
        <div class="data-value">Julio Emmanuel Romero Beltrán</div>
        
        <span class="data-label">Matrícula:</span>
        <div class="data-value">22031467</div>
        
        <form action="/json" method="get">
            <label class="data-label" for="texto">Escribe algo para enviarlo en JSON:</label>
            <input type="text" id="texto" name="texto" placeholder="Tu mensaje aquí...">
            <br>
            <button type="submit">Enviar</button>
        </form>

        <p class="note">
            ¡La ruta /json devuelve tu información en formato API!
        </p>
    </div>
</body>
</html>
    """
    return styled_html

@app.route("/json")
def json_response():
    """
    Ruta que devuelve la respuesta JSON con el parámetro 'texto' si se pasa en la URL.
    """
    texto = request.args.get("texto", "Nada recibido")

    return jsonify({
        "mensaje": "Hola Mundo",
        "nombre": "Julio Emmanuel Romero Beltrán",
        "matricula": "22031467",
        "texto": texto
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
