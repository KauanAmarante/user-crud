from flask import Flask
from .models import db
from .routes import user_bp
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    app.register_blueprint(user_bp)
    
    return app