# GUDLFT – Plateforme de réservation (POC)

## Intro

```
Hey,

Je viens de recevoir le rapport de QA pour la phase 1 du projet. Il y a plusieurs bogues, dont un qui fait planter l'application ! 
Malheureusement, je ne suis pas au bureau pour les prochains jours (un de mes enfants est tombé malade ce week-end). 
Je ne sais pas encore quand je pourrai être là dans la semaine. Pourriez-vous prendre en charge la mise en œuvre du projet ? 
Vous devrez régler les bogues de la phase 1 et mettre en œuvre les éléments de la phase 2 (j'ai ajouté le travail de la phase 2 et les bogues de la section “issues” du repo). 

Vous devrez cloner et forker le repo et le mettre en place sur votre machine locale (tout ce dont vous avez besoin se trouve dans le fichier README). 
Ensuite, passez en revue les bogues dans la section des problèmes, puis essayez de reproduire les problèmes sur votre machine locale pour résoudre les bogues et ajouter la gestion des erreurs. 
Pour gagner du temps de configuration, nous utilisons Flask et JSON pour éviter d'utiliser une base de données. 
La plupart des outils dont vous aurez besoin se trouvent dans le fichier requirements.txt dans le repo, 
mais vous devrez installer Flask et notre framework de test préféré, pytest, ainsi que notre outil de test de performance, Locust. 

Vous devrez également préparer un rapport de test et un rapport de performances, 
conformément au guide de développement à la fin des spécifications fonctionnelles ci-jointes. 
Veillez à suivre toutes les directives, car le QA nous reproche de ne pas respecter les normes. 
Vous devez tester de manière approfondie les résultats requis (à la fois les happy paths et les sad paths) pour toutes les fonctionnalités de l'application.  
Je vous encourage également à adopter une approche de TDD, car cela vous aidera à rationaliser votre travail. 

Une fois que vous aurez terminé, nous ferons un examen de ce que vous avez dans la branche QA du code. 
Nous examinerons les rapports et la manière dont vous avez résolu les problèmes, 
nous examinerons votre code et nous testerons la couverture de la nouvelle fonctionnalité. 

Merci !

```

## 1. Pourquoi

Ce projet est une preuve de concept (POC) d'une version allégée de la plateforme de réservation de compétitions. Les secrétaires des clubs se connectent avec leur email et utilisent les points de leur club pour réserver des places : **1 point = 1 place**, avec **12 places au maximum par club et par compétition**.

## 2. Technologies

- Python **3.10 ou plus** : testé sous Windows (Python 3.11) et sous Linux (Python 3.10 et 3.13). macOS utilise les mêmes commandes que Linux, mais le projet n'y a pas été testé.
- [Flask 3.1](https://flask.palletsprojects.com/) : le framework web
- [pytest](https://docs.pytest.org/) et [coverage](https://coverage.readthedocs.io/) : les tests et la couverture de code
- [Selenium](https://www.selenium.dev/documentation/) : les tests fonctionnels (Google Chrome requis)
- [Locust](https://docs.locust.io/) : les tests de performance
- [Flake8](https://flake8.pycqa.org/) et [flake8-html](https://pypi.org/project/flake8-html/) : la qualité du code (PEP 8)

## 3. Installation

```bash
git clone https://github.com/kouakous/Python_Testing_2627.git
cd Python_Testing_2627
```

| Étape | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Créer l'environnement virtuel | `python -m venv venv` | `python3 -m venv venv` |
| L'activer | `venv\Scripts\Activate.ps1` | `source venv/bin/activate` |
| Installer les dépendances | `pip install -r requirements.txt` | `pip install -r requirements.txt` |

- **Windows** : si PowerShell refuse d'activer l'environnement, lancez d'abord `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`.
- `requirements.txt` ne contient que les dépendances directes, avec leur version. pip installe automatiquement les sous-dépendances adaptées à chaque système.

## 4. Lancer l'application

Sur tous les systèmes :

```bash
python server.py
```

Ouvrez ensuite http://127.0.0.1:5000.

Vous pouvez aussi utiliser la commande Flask :

- **Windows** : `$env:FLASK_APP = "server.py"`, puis `flask run`
- **macOS / Linux** : `export FLASK_APP=server.py`, puis `flask run`

**macOS 12 et plus** : le port 5000 est occupé par le récepteur AirPlay. Utilisez `flask run --port 5001`, ou désactivez le récepteur AirPlay dans les réglages du système.

Les emails acceptés à la connexion sont dans `clubs.json` : `john@simplylift.co`, `admin@irontemple.com`, `kate@shelifts.co.uk`.

## 5. Données

- `clubs.json` et `competitions.json` remplacent une base de données.
- Les réservations sont gardées **en mémoire** : elles sont perdues au redémarrage du serveur. C'est volontaire pour ce POC.
- La compétition **Winter Cup** (décembre 2027) a été ajoutée. Les deux compétitions d'origine datent de 2020 et ne sont donc plus réservables.

## 6. Tests

```
tests/
├── conftest.py             fixtures communes : données de test et client Flask
├── unit/                   44 tests : fonctions isolées
│   ├── test_recherche.py       recherche d'un club ou d'une compétition
│   ├── test_validation.py      saisie du nombre de places et règles de réservation
│   ├── test_reservations.py    suivi des places déjà réservées par club
│   ├── test_dates.py           compétitions passées
│   ├── test_tableau_points.py  tableau des points
│   └── test_chargement.py      chargement des fichiers JSON
├── integration/            22 tests : routes Flask avec le client de test
│   ├── test_login.py           connexion, déconnexion, compétition complète
│   ├── test_book.py            page de réservation
│   ├── test_purchase.py        achat de places
│   └── test_points.py          tableau public des points
└── functional/             2 tests : parcours utilisateur dans Chrome (Selenium)
    ├── conftest.py             serveur Flask réel et navigateur
    └── test_parcours.py
```

```bash
python -m pytest                 # tous les tests (68)
python -m pytest tests/unit      # un seul type de tests
```

- Les tests utilisent leurs **propres données** (`tests/conftest.py`), jamais les fichiers JSON. `monkeypatch` les remet en place après chaque test, donc un test ne peut pas influencer le suivant.
- Les tests fonctionnels lancent un vrai serveur Flask sur un port libre et pilotent Chrome sans fenêtre. Si Chrome n'est pas installé, ils sont **ignorés** au lieu d'échouer.
- Le ratio demandé est respecté : **44 tests unitaires**, pour 22 tests d'intégration et 2 tests fonctionnels.
- Approche **TDD** : dans chaque branche de bug, un premier commit ajoute les tests (rouges), un second ajoute la correction (verts).

## 7. Couverture de code

```bash
coverage run -m pytest
coverage report
coverage html -d reports/coverage
```

**Résultat : 99 % de `server.py`** (121 instructions, 1 non couverte : la ligne `app.run()`, exécutée seulement avec `python server.py`). L'objectif du guide est de 60 %.

Rapport détaillé : `reports/coverage/index.html`.

## 8. Tests de performance (Locust)

Exigences : afficher la liste des compétitions en moins de **5 secondes** et mettre à jour les points en moins de **2 secondes**, avec **6 utilisateurs**.

Dans un premier terminal :

```bash
python server.py
```

Dans un second terminal, avec l'environnement virtuel activé :

```bash
locust -f locustfile.py --headless -u 6 -r 6 -t 60s --host http://127.0.0.1:5000 --html reports/performance.html
```

Résultats (6 utilisateurs, 60 secondes, en local) :

| Requête | Requêtes | Échecs | Moyenne | 95 % | Maximum | Exigence |
|---|---|---|---|---|---|---|
| `POST /showSummary` (liste des compétitions) | 109 | 0 | 5 ms | 7 ms | 64 ms | < 5 s ✅ |
| `POST /purchasePlaces` (mise à jour des points) | 36 | 0 | 6 ms | 18 ms | 61 ms | < 2 s ✅ |
| `GET /points` (tableau des points) | 36 | 0 | 6 ms | 47 ms | 57 ms | — |
| **Total** | **181** | **0** | **6 ms** | **7 ms** | **64 ms** | ✅ |

Rapport complet : `reports/performance.html`.

## 9. Rapport Flake8

```bash
python -m flake8
python -m flake8 --format=html --htmldir=reports/flake8
```

- La première commande n'affiche rien : **aucune erreur**.
- Le rapport HTML (`reports/flake8/index.html`) indique : *No flake8 errors found in 15 files scanned.*
- La configuration est dans `.flake8` : 79 caractères maximum, `venv/` et `reports/` exclus.

## 10. Conventions

- **Branches** : `bug/<nom>`, `feature/<nom>` et `amelioration/<nom>`, sans accents pour éviter les problèmes de noms de fichiers sous macOS.
- **Une branche par bug.** Une branche n'est fusionnée dans `main` que si tous les tests passent.
- **Branche `QA`** : créée depuis `main` pour la revue, et jamais fusionnée dans `main`.
- **Tests** : un fichier `test_<sujet>.py` par partie du code, et des fonctions nommées `test_<situation>_<resultat_attendu>`.
- **Code** : PEP 8, vérifié par Flake8.

## 11. Bugs corrigés et fonctionnalités ajoutées

| Problème | Branche |
|---|---|
| Connexion avec un email inconnu : l'application plantait | `bug/email-inconnu` |
| `/book` avec un club ou une compétition inexistants : plantage, et club transmis sous forme de texte | `bug/book-url-invalide` |
| Nombre de places vide ou non numérique : plantage | `bug/places-invalides` |
| Points non déduits après une réservation ; message sans le nombre de places | `bug/deduction-points` |
| `/purchasePlaces` avec un club ou une compétition inconnus : plantage | `bug/purchase-club-competition-inconnus` |
| Réservation acceptée sans assez de points | `bug/points-insuffisants` |
| Plus de 12 places par compétition, y compris en plusieurs fois | `bug/max-12-places` |
| Plus de places que disponibles ; aucun message pour une compétition complète | `bug/places-disponibles` |
| Zéro ou nombre négatif de places accepté | `bug/places-negatives` |
| Réservation possible sur une compétition passée | `bug/competition-passee` |
| Phase 2 : tableau public des points des clubs | `feature/tableau-points` |
| Compatibilité Windows, macOS et Linux ; passage à Flask 3 | `amelioration/multiplateforme` |
| Tests fonctionnels Selenium | `amelioration/tests-fonctionnels` |
| Tests de performance Locust | `amelioration/tests-performance` |
| Style PEP 8, rapports Flake8 et de couverture, README | `amelioration/flake8-et-readme` |

## 12. Limites connues et pistes d'amélioration

- **Pas de vraie session** : une page comme `/book/<compétition>/<club>` est accessible sans connexion, et `/logout` ne fait que rediriger. Piste : gérer la connexion avec `flask.session` ou Flask-Login.
- **Données non persistées** : les JSON ne sont jamais réécrits. Piste : une base de données (SQLite, PostgreSQL).
- **`secret_key` écrite en dur** dans le code. Piste : la lire dans une variable d'environnement.
- **Tout le code est dans `server.py`**, un choix assumé pour un POC. Piste : séparer les données, les règles de réservation et les routes (Blueprints Flask, fonction `create_app()`).
