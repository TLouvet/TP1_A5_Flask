## Comment on installe le projet ?

- optionnel: Créer un venv avec python -m venv .venv
- optionnel: Activer le venv:
  - Linux & Mac: `source .venv/bin/activate sous Mac/Linux`
  - Window: `.venv\Scripts\activate`
- pip install -r requirements.txt

## Mise en place

- Créer un .flaskenv
- Renseigner les variables suivantes:
  - FLASK_DEBUG= 0 ou 1 pour le hot reload
  <!-- le fichier qui doit lancer l'application | mettre la valeur ici est ok exceptionnellement -->
  - FLASK_APP=main

## Lancement du projet

- flask run

Le Hello World de l'api devrait être appelable depuis http://localhost:5000

## Routes

GET /tasks
GET /tasks/:uuid
POST /tasks
PUT /tasks/:uuid
PATCH /tasks/:uuid
DELETE /tasks/:uuid

GET /admin
