from flask import Blueprint, request, jsonify
from app import db
from app.models.etudiant import Etudiant

etudiant_bp = Blueprint('etudiants', __name__)

@etudiant_bp.route('/', methods=['GET'])
def list_etudiants():
    etudiants = Etudiant.query.all()
    return jsonify([{'matricule': e.matricule, 'nom': e.nom, 'email': e.email, 'promotion':e.promotion, 'filiere':e.filiere} for e in etudiants])

@etudiant_bp.route('/<matricule>', methods=['GET'])
def get_etudiant(matricule):
    etudiant = Etudiant.query.filter_by(matricule=matricule).first()
    if etudiant:
        return jsonify({'matricule': etudiant.matricule, 'nom': etudiant.nom, 'email': etudiant.email})
    return jsonify({'message': 'Étudiant non trouvé'}), 404

@etudiant_bp.route('/promotion/<promotion>', methods=['GET'])
def get_etudiants_by_promotion(promotion):
    etudiants = Etudiant.query.filter_by(promotion=promotion).all()
    if etudiants:
        return jsonify([{'matricule': e.matricule, 'nom': e.nom, 'email': e.email} for e in etudiants])
    return jsonify({'message': 'Aucun étudiant trouvé pour cette promotion'}), 404

@etudiant_bp.route('/filiere/<filiere>', methods=['GET'])
def get_etudiants_by_filiere(filiere):
    etudiants = Etudiant.query.filter_by(filiere=filiere).all()
    if etudiants:
        return jsonify([{'matricule': e.matricule, 'nom': e.nom, 'email': e.email} for e in etudiants])
    return jsonify({'message': 'Aucun étudiant trouvé pour cette filière'}), 404

@etudiant_bp.route('/promotion/<promotion>/filiere/<filiere>', methods=['GET'])
def get_etudiants_by_promotion_and_filiere(promotion, filiere):
    etudiants = Etudiant.query.filter_by(promotion=promotion, filiere=filiere).all()
    if etudiants:
        return jsonify([{'matricule': e.matricule, 'nom': e.nom, 'email': e.email} for e in etudiants])
    return jsonify({'message': 'Aucun étudiant trouvé pour cette promotion et filière'}), 404
