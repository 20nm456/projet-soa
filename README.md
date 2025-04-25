# Gestion des Étudiants et Notes

Ce projet est une application Flask qui permet de gérer des étudiants et leurs notes. Elle expose des API REST pour effectuer des opérations CRUD sur les étudiants et les notes.

## Prérequis

- Python 3.11 ou supérieur
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <url-du-repo>
   cd etudiants
2. lancer l'application
   python run.py

3.Utilisation des API
  A)Endpoints pour les étudiants
  -Lister tous les étudiants
  GET /etudiants/
  -Récupérer un étudiant par matricule
   GET /etudiants/<matricule>
   -Lister les étudiants par promotion
  GET /etudiants/promotion/<promotion>
  
  -Lister les étudiants par filière
  GET /etudiants/filiere/<filiere>

B)Endpoints pour les notes
-Lister toutes les notes
GET /notes/

-Lister les notes d'un étudiant
GET /notes/<matricule>

-Récupérer une note spécifique d'un étudiant pour une matière
GET /notes/<matricule>/<matiere>

Auteur
Nom: NGOIE MUNUNGA Cadet
Contact : 20nm456@esisalama.org



  
