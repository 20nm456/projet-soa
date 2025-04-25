from flask import Blueprint, request, jsonify
from app import db
from app.models.note import Note

note_bp = Blueprint('notes', __name__)

@note_bp.route('/<matricule>', methods=['GET'])
def get_notes_by_etudiant(matricule):
    notes = Note.query.filter_by(matricule_etudiant=matricule).all()
    return jsonify([{'matiere': n.matiere, 'note': n.note, 'type': n.type} for n in notes])

@note_bp.route('/<matricule>/<matiere>', methods=['GET'])
def get_note_by_etudiant_and_matiere(matricule, matiere):
    note = Note.query.filter_by(matricule_etudiant=matricule, matiere=matiere).first()
    if note:
        return jsonify({'matricule': note.matricule_etudiant, 'matiere': note.matiere, 'note': note.note, 'type': note.type})
    return jsonify({'message': 'Note non trouvée'}), 404

@note_bp.route('/', methods=['GET'])
def list_notes():
    notes = Note.query.all()
    return jsonify([{'matricule': n.matricule_etudiant, 'matiere': n.matiere, 'note': n.note, 'type': n.type} for n in notes])
