# Système Bancaire avec Django

Un système bancaire complet développé avec Django, incluant la gestion des clients, des comptes, des transactions et des guichets automatiques bancaires (GAB).

## Fonctionnalités

### Fonctionnalités Obligatoires
- Inscription des clients avec validation
- Dépôts et retraits sur comptes
- Gestion des GAB (localisation, état, rechargement)

### Fonctionnalités Enrichissantes
- Virements entre comptes
- Tableau de bord administrateur
- Historique des transactions
- Interface responsive avec Bootstrap

## Installation

1. Cloner le repository
2. Créer un environnement virtuel : `python3 -m venv venv`
3. Activer l'environnement : `source venv/bin/activate`
4. Installer les dépendances : `pip install -r requirements.txt`
5. Appliquer les migrations : `python manage.py migrate`
6. Créer un superutilisateur : `python manage.py createsuperuser`
7. Lancer le serveur : `python manage.py runserver`

## Utilisation

- Accéder à l'application à http://127.0.0.1:8000/
- Inscription pour les nouveaux clients
- Connexion pour accéder au tableau de bord
- Administration via /admin/ pour les gestionnaires

## Technologies
- Backend : Django 6.0
- Base de données : SQLite (développement) / PostgreSQL (production)
- Frontend : Templates Django + Bootstrap 5