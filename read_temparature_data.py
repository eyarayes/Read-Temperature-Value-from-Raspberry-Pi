from ast import For
import os
from time import sleep
import pandas as pandas
import datetime


# Vérifier si le fichier de données existe
def CheckFileExistance(file):
    if os.path.exists(file): 
        print(file + " existe.")
        return True
    else:
        print(file + " n'existe pas.")
        return False   

# Lire les données du fichier
def ReadData(file):
    data = pandas.read_excel(file)
    print(data)


# Traitement
fileExists = CheckFileExistance("valeurs.xlsx")
if (fileExists):
    ReadData("valeurs.xlsx")        