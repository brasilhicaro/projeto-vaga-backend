from flask import app, Flask, request
from src.presentation.controllers.employeer_controller import routes as employeer_routes


app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)