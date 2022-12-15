# Read-Temperature-Value-from-Raspberry-Pi

** Commandes cmd pour installation des packages **

1) Installer pandas
python -m pip install --upgrade pandas

2) Installer openpyxl
python -m pip install openpyxl


Avec un Raspberry Pi et quelques capteurs, vous pouvez facilement mesurer la température sans aucun tracas.
Cependant, il peut également révéler de l'humidité dans certaines situations et projets (comme les stations météorologiques). 

 # Utilisez ThingSpeak pour enregistrer et analyser les données du capteur Raspberry Pi
Les projets qui tournent 24 heures sur 24 génèrent souvent beaucoup de données.
Une façon de les garder persistants consiste à stocker les données dans une base de données locale.
Mais il y a aussi des raisons contre cette solution. Les données mesurées sont donc
(par exemple ceux des stations météorologiques) continueront d'être disponibles à l'avenir, et divers services en ligne pourraient ne plus être nécessaires.
L'un de ces fournisseurs est ThingSpeak. Vous pouvez y créer un compte gratuit pour les petites applications et transférer facilement vos données.

 ## Comment puis-je transférer les données des capteurs vers ThingSpeak pour évaluation ?
Avant de commencer, vous avez besoin d'un compte ThingSpeak.
Si vous n'avez pas encore de compte, créez-en un ici. Créez ensuite une nouvelle chaîne sous
https://thingspeak.com/channels.

Ici, vous donnez un nom au canal et les champs que vous souhaitez utiliser. Un total de 8 champs sont autorisés. Les noms spécifiés n'ont aucun effet sur le transfert de données, car vous ne spécifiez que "field1", "field2", etc. Vous pouvez toujours modifier ces noms attribués ultérieurement.
![image](https://user-images.githubusercontent.com/61162446/207810926-15e4b407-03c7-4d57-8de1-f60caa4a5bbb.png)
Abonnez-vous aux chaînes ci-dessous et vous serez automatiquement redirigé vers l'onglet Vue privée. Les champs attribués sont représentés ici sous forme de diagramme. En haut se trouve le "ID de chaîne". vous en aurez besoin bientôt.
Passons maintenant à l'onglet "Clés API". Pour écrire et récupérer des données, vous avez également besoin de deux valeurs : "Write API Key" et "Read API Key".

 ## Utilisation de la bibliothèque ThingSpreak sur Raspberry Pi
Pour utiliser ce service, il suffit d'envoyer des données avec "POST" ou de récupérer des données avec "GET". Les fonctions sont disponibles dans presque tous les langages de programmation et, avec un peu de connaissances, le transfert de données peut être effectué rapidement. Les réponses sont généralement JSON.
Vous pouvez également utiliser la bibliothèque ThingSpeak si vous n'avez pas assez d'expérience ou si vous ne voulez pas écrire la vôtre. Pour ce faire, installez simplement via pip.
    Pip install Thingspeak

 Commençons. Le script Python doit lire la température toutes les 15 secondes et l'envoyer au canal. De plus, les données doivent être récupérées à nouveau. créer un nouveau fichier,
trucs_parle_exemple.py
     thingspeak_example.py


## Obtenir des données dans le Web Panel et via l’API
![image](https://user-images.githubusercontent.com/61162446/207815524-169abf2c-2b50-4110-bbbf-a952b50009f7.png)



