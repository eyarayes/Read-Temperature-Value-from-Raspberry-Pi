# Read-Temperature-Value-from-Raspberry-Pi

** Commandes cmd pour installation des packages **

1) Installer pandas
python -m pip install --upgrade pandas

2) Installer openpyxl
python -m pip install openpyxl


Avec le Raspberry Pi et certains capteurs, il est facile de mesurer la température sans trop d’effort. 
De plus, cependant, l’humidité dans certaines situations ou projets (comme une station météorologique) peut être éclairante. 

 # Enregistrer les données des capteurs Raspberry Pi avec ThingSpeak et les analyser
 Il arrive fréquemment que de nombreuses données soient générées dans des projets qui fonctionnent 24 heures sur 24. 
 Une façon de les conserver en permanence est de stocker les données dans une base de données locale. 
 Cependant,il y a aussi des raisons qui plaident contre cette solution. Pour que les données mesurées 
 (par exemple, celles d’une station météorologique) restent disponibles à l’avenir, il est également possible d’éviter divers services en ligne.

L’un de ces fournisseurs est ThingSpeak. Vous pouvez y créer un compte gratuit pour de petites applications et transférer ses données très facilement. 

## Comment transférer des données de capteurs vers ThingSpeak et les évaluer par la suite?

Avant de commencer, vous devez avoir un compte sur ThingSpeak. 
Créez un compte ici si vous n’en avez pas encore. Ensuite, créez un nouveau canal à https://thingspeak.com/channels.

Ici, vous donnez un nom au canal ainsi que les champs que vous voulez utiliser. Au total, on peut utiliser jusqu’à 8 champs. Les noms donnés n’ont aucune influence sur la transmission des données, car nous spécifions seulement « champ1 », « champ2 », etc. Tous ces noms attribués sont toujours modifiables ultérieurement.
![image](https://user-images.githubusercontent.com/61162446/207810926-15e4b407-03c7-4d57-8de1-f60caa4a5bbb.png)
Après avoir enregistré le canal ci-dessous, vous serez automatiquement redirigé vers l’onglet « Vue privée ». Ici, les champs attribués sont affichés sous forme de diagramme. Plus haut, vous trouverez l' »ID du Canal« . Nous en aurons bientôt besoin.

Ensuite, nous passons à l’onglet « Clés API ». Les deux valeurs « Écrire la clé API » et « Lire la clé API » sont également nécessaires pour que nous puissions écrire ou récupérer des données

## Utilisation de la bibliothèque ThingSpreak de Raspberry Pi
Pour pouvoir utiliser le service, il est possible d’envoyer simplement les données via « POST » ou de les récupérer via « GET ». Les fonctions sont disponibles dans à peu près tous les langages de programmation et avec un peu de connaissances, le transfert de données devrait être rapide. Les réponses sont en principe en JSON.

Si vous n’avez pas assez d’expérience ou si vous n’avez tout simplement pas envie de l’écrire vous-même, vous pouvez également utiliser la bibliothèque ThingSpeak. Pour cela, nous l’installons simplement par pip :
       pip install thingspeak

Alors commençons. Notre script Python devrait lire la température toutes les 15 secondes et les envoyer à notre canal. En outre, les données devraient ensuite être récupérées à nouveau .
Nous allons créer un nouveau fichier,
     thingspeak_example.py


## Obtenir des données dans le Web Panel et via l’API
![image](https://user-images.githubusercontent.com/61162446/207815524-169abf2c-2b50-4110-bbbf-a952b50009f7.png)



