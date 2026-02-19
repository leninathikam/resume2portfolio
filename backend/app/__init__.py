from flask import Flask
from flask_cors import CORS
from config import config
import os

def create_app(config_name=None):
    """Application factory"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Enable CORS
    CORS(app, origins=[os.getenv('FRONTEND_URL', 'http://localhost:3000')])
    
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Register blueprints
    from app.routes import upload_bp
    app.register_blueprint(upload_bp)
    
    return app
