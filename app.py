from flask import Flask
from src.presentation.controllers.departament_controller import departament_controller
from src.presentation.controllers.employeer_controller import employeer_controller

app = Flask(__name__)

app.register_blueprint(departament_controller)
app.register_blueprint(employeer_controller)

@app.route("/")
def index():
    return "Bem-vindo à API!"

if __name__ == "__main__":
    app.run(debug=True)