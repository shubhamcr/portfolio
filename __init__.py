from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

from portfolio import views