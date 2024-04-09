from flask import Flask
""" This is a simple Flask application
that returns a string when the root URL
is accessed."""

def create_app():
    """ Create a Flask application."""
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, World!'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()