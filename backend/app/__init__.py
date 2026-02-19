from flask import Flask, jsonify
from flask_cors import CORS
from config import config
import os

def create_app(config_name=None):
    """Application factory"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Enable CORS with multiple origins
    allowed_origins = [
        'http://localhost:3000',
        'http://localhost:5000',
        'https://leninathikam.github.io',
        os.getenv('FRONTEND_URL', 'http://localhost:3000')
    ]
    CORS(app, origins=allowed_origins)
    
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Health check endpoint
    @app.route('/', methods=['GET', 'HEAD'])
    def health_check():
        return jsonify({'status': 'ok', 'service': 'resume-to-portfolio-api'}), 200
    
    # Register blueprints
    from app.routes import upload_bp
    app.register_blueprint(upload_bp)
    
    return app
