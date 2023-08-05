from flask import Flask

def create_app():
    """ Factorie Inicial"""
    app = Flask(__name__)
    return app