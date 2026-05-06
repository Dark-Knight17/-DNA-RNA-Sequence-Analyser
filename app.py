from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
from app.routes.main import main_bp

app = Flask(__name__, 
            template_folder='app/templates',
            static_folder='app/static')

app.secret_key = 'development_key' # Replace with env var in production
app.config['UPLOAD_FOLDER'] = 'app/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB limit

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Register Blueprints
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
