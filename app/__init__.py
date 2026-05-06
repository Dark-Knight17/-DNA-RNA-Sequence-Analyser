from flask import Flask
import os
from database.db_manager import init_db

def create_app():
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')

    app.secret_key = 'development_key'
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Initialize Database
    init_db()

    # Register Blueprints
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
