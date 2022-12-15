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

## Comment transférer des données de capteurs vers ThingSpeak et les évaluer par la suite.
