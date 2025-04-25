from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///etudiants.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.etudiant_routes import etudiant_bp
    from app.routes.note_routes import note_bp

    app.register_blueprint(etudiant_bp, url_prefix='/etudiants')
    app.register_blueprint(note_bp, url_prefix='/notes')

    return app