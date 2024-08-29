# VPO_Project - Analyse d'Images avec YOLOv5

## Description
VPO_Project est une application web simple permettant de réaliser une analyse d'images en utilisant le modèle YOLOv5. L'application permet de téléverser une image via une interface web, puis d'afficher les objets détectés dans l'image avec leur niveau de confiance.

## Structure du Projet
La structure du projet est organisée comme suit :

VPO_Project/
│
├── static/
│   ├── css/
│   │   └── style.css           # Feuille de style CSS pour la page HTML
│   └── js/
│       └── script.js           # JavaScript pour gérer l'interaction de l'interface
│
├── templates/
│   └── index.html              # Page HTML principale
│
├── visionPatOrdinateurCam.py   # Script Python pour la vision par ordinateur avec YOLOv5
│
├── app.py                      # Script principal qui lance le serveur Flask
│
├── requirements.txt            # Liste des dépendances Python du projet
│
└── README.md                   # Documentation du projet

## Prérequis
Assurez-vous d'avoir Python 3.9 ou une version supérieure installée ainsi que les packages suivants :

- Flask
- torch
- torchvision
- Pillow
- OpenCV (cv2)

Vous pouvez installer les dépendances avec la commande suivante :

```bash
pip install -r requirements.txt

## Installation
  Clonez ce dépôt sur votre machine locale :
  git clone https://votre-repo.git

  Accédez au répertoire du projet :
  cd VPO_Project

  Installez les dépendances nécessaires :
  pip install -r requirements.txt

## Utilisation
  Exécutez le script app.py pour démarrer le serveur Flask :
  python app.py

  Ouvrez votre navigateur web et accédez à l'adresse suivante :
  http://127.0.0.1:5000

  Téléversez une image en utilisant l'interface web et cliquez sur "Analyser". Les objets détectés dans l'image seront affichés avec leur niveau de confiance.

## Fichiers Importants
1. app.py
C'est le script principal qui lance l'application Flask. Il gère les routes, notamment la page principale et la route /analyze qui reçoit l'image uploadée et renvoie les résultats de l'analyse.

2. visionPatOrdinateurCam.py
Ce fichier contient la logique de vision par ordinateur. Il utilise le modèle YOLOv5 pour détecter les objets dans les images.

3. index.html
Le fichier HTML qui contient la structure de la page web. Il inclut un formulaire pour téléverser des images, un bouton pour lancer l'analyse, et une section pour afficher les résultats.

4. style.css
Le fichier CSS pour styliser la page HTML. Il est inclus via le dossier static/css/.

5. script.js
Le fichier JavaScript qui gère l'interaction utilisateur. Il traite l'image téléversée, envoie une requête POST au serveur Flask, et affiche les résultats retournés par le serveur.

Avertissements
Cette application utilise un serveur Flask en mode développement. Pour déployer l'application en production, veuillez utiliser un serveur WSGI tel que Gunicorn ou uWSGI.

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Conclusion
Cette documentation fournit toutes les informations nécessaires pour installer, configurer, et utiliser le projet VPO_Project. Assurez-vous de suivre les étapes décrites pour garantir le bon fonctionnement de l'application.