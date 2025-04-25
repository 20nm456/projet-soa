from app import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matiere = db.Column(db.String(100), nullable=False)
    note = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # examen, semestre, etc.
    matricule_etudiant = db.Column(db.String(50), db.ForeignKey('etudiant.matricule'), nullable=False)