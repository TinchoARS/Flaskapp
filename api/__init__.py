from flask import Flask, jsonify, request
from config import Config
from .database import DatabaseConnection
from .routes.tarea_bp import tarea_bp


def init_app():
    """Crea y configura la aplicación FLask."""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    app.register_blueprint(tarea_bp)
    
   
    @app.route('/')
    def hello_world():
        return 'Bienvenidos!'
    
    return app