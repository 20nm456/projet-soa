from app import db

class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.String(50), unique=True, nullable=False)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    filiere = db.Column(db.String(100), nullable=False)
    promotion = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Note', backref='etudiant', lazy=True)