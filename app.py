from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    """
    Ruta raíz que devuelve una página HTML con estilo mejorado.
    Utiliza CSS simple y moderno para presentar la información de manera más atractiva,
    centrada y con un tema oscuro.
    """
    styled_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>¡Hola Mundo! - App de Render</title>
    <style>
        /* Estilos base para un diseño moderno y oscuro (Catppuccin Macchiato palette) */
        body {
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1e1e2e; /* Fondo oscuro */
            color: #cdd6f4; /* Texto principal claro */
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            transition: background-color 0.3s ease;
        }
        .container {
            background-color: #313244; /* Fondo de la tarjeta */
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            text-align: center;
            max-width: 90%;
            width: 450px;
            border-top: 6px solid #89b4fa; /* Color de acento (azul) */
            animation: slideIn 0.8s ease-out;
        }
        h1 {
            color: #a6e3a1; /* Color de acento para el título (verde) */
            font-size: 2.8em;
            margin-bottom: 5px;
            font-weight: 700;
        }
        h2 {
            font-size: 1.1em;
            font-weight: 400;
            margin-top: 0;
            padding-bottom: 20px;
            border-bottom: 1px dashed #45475a;
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
            color: #fab387; /* Color de acento para los valores (naranja) */
            font-weight: 600;
            margin-bottom: 15px;
            padding: 5px 0;
        }
        
        /* Animación sutil para la entrada del contenedor */
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(-50px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Responsividad básica */
        @media (max-width: 600px) {
            .container {
                padding: 30px 20px;
            }
            h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Hola Mundo!</h1>
        
        <!-- Datos mostrados con mejor formato -->
        <span class="data-label">Alumno:</span>
        <div class="data-value">Julio Emmanuel Romero Beltrán</div>
        
        <span class="data-label">Matrícula:</span>
        <div class="data-value">22031467</div>
        
        <p style="color: #a6e3a1; font-style: italic; margin-top: 30px;">
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
    Ruta que devuelve la respuesta JSON. Mantiene la funcionalidad original.
    """
    return jsonify({
        "mensaje": "Hola Mundo",
        "nombre": "Julio Emmanuel Romero Beltrán",
        "matricula": "22031467"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


